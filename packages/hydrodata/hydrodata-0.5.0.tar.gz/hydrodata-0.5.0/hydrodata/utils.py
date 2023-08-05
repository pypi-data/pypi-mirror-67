#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some utilities for Hydrodata"""

import os
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio as rio
import rasterio.features as rio_features
import rasterio.warp as rio_warp
from hydrodata import helpers
from owslib.wms import WebMapService
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    RequestException,
    RetryError,
    Timeout,
)
from shapely.geometry import box, mapping


def retry_requests(
    retries=3,
    backoff_factor=0.5,
    status_to_retry=(500, 502, 504),
    prefixes=("http://", "https://"),
):
    """Configures the passed-in session to retry on failed requests.

    The fails can be due to connection errors, specific HTTP response
    codes and 30X redirections. The original code is taken from:
    https://github.com/bustawin/retry-requests

    Parameters
    ----------
    retries : int
        The number of maximum retries before raising an exception.
    backoff_factor : float
        A factor used to compute the waiting time between retries.
    status_to_retry : tuple of ints
        A tuple of status codes that trigger the reply behaviour.

    Returns
    -------
    session
        A session object with retry configurations.
    """

    import requests
    from requests.adapters import HTTPAdapter
    from urllib3 import Retry

    session = requests.Session()

    r = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_to_retry,
        method_whitelist=False,
    )
    adapter = HTTPAdapter(max_retries=r)
    for prefix in prefixes:
        session.mount(prefix, adapter)
    session.hooks = {"response": lambda r, *args, **kwargs: r.raise_for_status()}

    return session


def get_url(session, url, payload=None):
    """Retrieve data from a url by GET using a requests session"""
    try:
        return session.get(url, params=payload)
    except (ConnectionError, HTTPError, RequestException, RetryError, Timeout):
        raise


def post_url(session, url, payload=None):
    """Retrieve data from a url by POST using a requests session"""
    try:
        return session.post(url, data=payload)
    except (ConnectionError, HTTPError, RequestException, RetryError, Timeout):
        raise


def onlyIPv4():
    """disable IPv6 and only use IPv4"""
    import socket
    from unittest.mock import patch

    orig_getaddrinfo = socket.getaddrinfo

    def getaddrinfoIPv4(host, port, family=0, type=0, proto=0, flags=0):
        return orig_getaddrinfo(
            host=host,
            port=port,
            family=socket.AF_INET,
            type=type,
            proto=proto,
            flags=flags,
        )

    return patch("socket.getaddrinfo", side_effect=getaddrinfoIPv4)


def check_dir(fpath):
    """Create parent directory for a file if doesn't exist"""
    parent = Path(fpath).parent
    if not parent.is_dir():
        try:
            os.makedirs(parent)
        except OSError:
            raise OSError(f"Parent directory cannot be created: {parent}")


def daymet_dates(start, end):
    """Correct dates for Daymet when leap years.

    Daymet doesn't account for leap years and removes
    Dec 31 when it's leap year. This function returns all
    the dates in the Daymet database within the provided date range.
    """

    period = pd.date_range(start, end)
    nl = period[~period.is_leap_year]
    lp = period[
        (period.is_leap_year) & (~period.strftime("%Y-%m-%d").str.endswith("12-31"))
    ]
    period = period[(period.isin(nl)) | (period.isin(lp))]
    years = [period[period.year == y] for y in period.year.unique()]
    return [(y[0], y[-1]) for y in years]


def get_ssebopeta_urls(start=None, end=None, years=None):
    """Get list of URLs for SSEBop dataset within a period"""
    if years is None and start is not None and end is not None:
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        if start < pd.to_datetime("2000-01-01") or end > pd.to_datetime("2018-12-31"):
            raise ValueError("SSEBop database ranges from 2000 till 2018.")
        dates = pd.date_range(start, end)
    elif years is not None and start is None and end is None:
        years = years if isinstance(years, list) else [years]
        seebop_yrs = np.arange(2000, 2019)

        if any(y not in seebop_yrs for y in years):
            raise ValueError("SSEBop database ranges from 2000 till 2018.")

        d_list = [pd.date_range(f"{y}0101", f"{y}1231") for y in years]
        dates = d_list[0] if len(d_list) == 1 else d_list[0].union_many(d_list[1:])
    else:
        raise ValueError("Either years or start and end arguments should be provided.")

    base_url = (
        "https://edcintl.cr.usgs.gov/downloads/sciweb1/"
        + "shared/uswem/web/conus/eta/modis_eta/daily/downloads"
    )
    f_list = [
        (d, f"{base_url}/det{d.strftime('%Y%j')}.modisSSEBopETactual.zip")
        for d in dates
    ]

    return f_list


def elevation_byloc(lon, lat):
    """Get elevation from USGS 3DEP service for a coordinate.

    Parameters
    ----------
    lon : float
        Longitude
    lat : float
        Latitude

    Returns
    -------
    float
        Elevation in meter
    """

    url = "https://nationalmap.gov/epqs/pqs.php"
    session = retry_requests()
    payload = {"output": "json", "x": lon, "y": lat, "units": "Meters"}
    r = get_url(session, url, payload)
    root = r.json()["USGS_Elevation_Point_Query_Service"]
    elevation = root["Elevation_Query"]["Elevation"]
    if elevation == -1000000:
        raise ValueError(
            f"The altitude of the requested coordinate ({lon}, {lat}) cannot be found."
        )
    else:
        return elevation


def elevation_bybbox(bbox, resolution, coords, crs="epsg:4326"):
    """Get elevation from DEM data for a list of coordinates.

    This function is intended for getting elevations for a gridded dataset.

    Parameters
    ----------
    bbox : list or tuple
        Bounding box with coordinates in [west, south, east, north] format.
    resolution : float
        Gridded data resolution in arc-second
    coords : list of tuples
        A list of coordinates in (lon, lat) format to extract the elevations.
    crs : string, optional
        The spatial reference system of the input region, defaults to
        epsg:4326.

    Returns
    -------
    numpy.ndarray
        An array of elevations in meters
    """
    import pyproj
    import shapely.ops as ops

    if isinstance(bbox, list) or isinstance(bbox, tuple):
        if len(bbox) != 4:
            raise TypeError(
                "The bounding box should be a list or tuple of length 4: [west, south, east, north]"
            )
    else:
        raise TypeError(
            "The bounding box should be a list or tuple of length 4: [west, south, east, north]"
        )

    url = "https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer"
    layers = ["3DEPElevation:None"]
    version = "1.3.0"

    if crs != "epsg:4326":
        prj = pyproj.Transformer.from_crs(crs, "epsg:4326", always_xy=True)
        _bbox = ops.transform(prj.transform, box(*bbox))
        res_bbox = _bbox.bounds
    else:
        res_bbox = bbox

    west, south, east, north = res_bbox
    width = int((east - west) * 3600 / resolution)
    height = int(abs(north - south) / abs(east - west) * width)

    wms = WebMapService(url, version=version)
    img = wms.getmap(
        layers=layers, srs=crs, bbox=bbox, size=(width, height), format="image/geotiff",
    )

    with rio.MemoryFile() as memfile:
        memfile.write(img.read())
        with memfile.open() as src:
            elevations = np.array([e[0] for e in src.sample(coords)], dtype=np.float32)

    return elevations


def pet_fao_byloc(df, lon, lat):
    """Compute Potential EvapoTranspiration using Daymet dataset for a single location.

    The method is based on `FAO-56 <http://www.fao.org/docrep/X0490E/X0490E00.htm>`.

    Parameters
    ----------
    df : DataFrame
        A dataframe with columns named as follows:
        ``tmin (deg c)``, ``tmax (deg c)``, ``vp (Pa)``, ``srad (W/m^2)``, ``dayl (s)``
    lon : float
        Longitude of the location of interest
    lat : float
        Latitude of the location of interest

    Returns
    -------
    DataFrame
        The input DataFrame with an additional column named ``pet (mm/day)``
    """

    keys = [v for v in df.columns]
    reqs = ["tmin (deg c)", "tmax (deg c)", "vp (Pa)", "srad (W/m^2)", "dayl (s)"]

    check_requirements(reqs, keys)

    dtype = df.dtypes[0]
    df["tmean (deg c)"] = 0.5 * (df["tmax (deg c)"] + df["tmin (deg c)"])
    Delta = (
        4098
        * (
            0.6108
            * np.exp(
                17.27 * df["tmean (deg c)"] / (df["tmean (deg c)"] + 237.3), dtype=dtype
            )
        )
        / ((df["tmean (deg c)"] + 237.3) ** 2)
    )
    elevation = elevation_byloc(lon, lat)

    P = 101.3 * ((293.0 - 0.0065 * elevation) / 293.0) ** 5.26
    gamma = P * 0.665e-3

    G = 0.0  # recommended for daily data
    df["vp (Pa)"] = df["vp (Pa)"] * 1e-3

    e_max = 0.6108 * np.exp(
        17.27 * df["tmax (deg c)"] / (df["tmax (deg c)"] + 237.3), dtype=dtype
    )
    e_min = 0.6108 * np.exp(
        17.27 * df["tmin (deg c)"] / (df["tmin (deg c)"] + 237.3), dtype=dtype
    )
    e_s = (e_max + e_min) * 0.5
    e_def = e_s - df["vp (Pa)"]

    u_2 = 2.0  # recommended when no data is available

    jday = df.index.dayofyear
    R_s = df["srad (W/m^2)"] * df["dayl (s)"] * 1e-6

    alb = 0.23

    jp = 2.0 * np.pi * jday / 365.0
    d_r = 1.0 + 0.033 * np.cos(jp, dtype=dtype)
    delta = 0.409 * np.sin(jp - 1.39, dtype=dtype)
    phi = lat * np.pi / 180.0
    w_s = np.arccos(-np.tan(phi, dtype=dtype) * np.tan(delta, dtype=dtype))
    R_a = (
        24.0
        * 60.0
        / np.pi
        * 0.082
        * d_r
        * (
            w_s * np.sin(phi, dtype=dtype) * np.sin(delta, dtype=dtype)
            + np.cos(phi, dtype=dtype)
            * np.cos(delta, dtype=dtype)
            * np.sin(w_s, dtype=dtype)
        )
    )
    R_so = (0.75 + 2e-5 * elevation) * R_a
    R_ns = (1.0 - alb) * R_s
    R_nl = (
        4.903e-9
        * (
            ((df["tmax (deg c)"] + 273.16) ** 4 + (df["tmin (deg c)"] + 273.16) ** 4)
            * 0.5
        )
        * (0.34 - 0.14 * np.sqrt(df["vp (Pa)"]))
        * ((1.35 * R_s / R_so) - 0.35)
    )
    R_n = R_ns - R_nl

    df["pet (mm/day)"] = (
        0.408 * Delta * (R_n - G)
        + gamma * 900.0 / (df["tmean (deg c)"] + 273.0) * u_2 * e_def
    ) / (Delta + gamma * (1 + 0.34 * u_2))
    df["vp (Pa)"] = df["vp (Pa)"] * 1.0e3

    return df


def pet_fao_gridded(ds):
    """Compute Potential EvapoTranspiration using Daymet dataset.

    The method is based on `FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`.
    The following variables are required:
    tmin (deg c), tmax (deg c), lat, lon, vp (Pa), srad (W/m2), dayl (s/day)
    The computed PET's unit is mm/day.

    Parameters
    ----------
    ds : xarray.DataArray
        The dataset should include the following variables:
        ``tmin``, ``tmax``, ``lat``, ``lon``, ``vp``, ``srad``, ``dayl``

    Returns
    -------
    xarray.DataArray
        The input dataset with an additional variable called ``pet``.
    """

    keys = [v for v in ds.keys()]
    reqs = ["tmin", "tmax", "lat", "lon", "vp", "srad", "dayl"]

    check_requirements(reqs, keys)

    dtype = ds.tmin.dtype
    dates = ds["time"]
    ds["tmean"] = 0.5 * (ds["tmax"] + ds["tmin"])
    ds["tmean"].attrs["units"] = "degree C"
    ds["delta"] = (
        4098
        * (0.6108 * np.exp(17.27 * ds["tmean"] / (ds["tmean"] + 237.3), dtype=dtype))
        / ((ds["tmean"] + 237.3) ** 2)
    )

    if "elevation" not in keys:
        coords = [
            (i, j)
            for i, j in zip(
                ds.sel(time=ds["time"][0]).lon.values.flatten(),
                ds.sel(time=ds["time"][0]).lat.values.flatten(),
            )
        ]
        margine = 0.05
        bbox = [
            ds.lon.min().values - margine,
            ds.lat.min().values - margine,
            ds.lon.max().values + margine,
            ds.lat.max().values + margine,
        ]
        resolution = (3600.0 * 180.0) / (6371000.0 * np.pi) * ds.res[0] * 1e3
        elevation = elevation_bybbox(bbox, resolution, coords).reshape(
            ds.dims["y"], ds.dims["x"]
        )
        ds["elevation"] = ({"y": ds.dims["y"], "x": ds.dims["x"]}, elevation)
        ds["elevation"].attrs["units"] = "m"

    P = 101.3 * ((293.0 - 0.0065 * ds["elevation"]) / 293.0) ** 5.26
    ds["gamma"] = P * 0.665e-3

    G = 0.0  # recommended for daily data
    ds["vp"] *= 1e-3

    e_max = 0.6108 * np.exp(17.27 * ds["tmax"] / (ds["tmax"] + 237.3), dtype=dtype)
    e_min = 0.6108 * np.exp(17.27 * ds["tmin"] / (ds["tmin"] + 237.3), dtype=dtype)
    e_s = (e_max + e_min) * 0.5
    ds["e_def"] = e_s - ds["vp"]

    u_2 = 2.0  # recommended when no wind data is available

    lat = ds.sel(time=ds["time"][0]).lat
    ds["time"] = pd.to_datetime(ds.time.values).dayofyear.astype(dtype)
    R_s = ds["srad"] * ds["dayl"] * 1e-6

    alb = 0.23

    jp = 2.0 * np.pi * ds["time"] / 365.0
    d_r = 1.0 + 0.033 * np.cos(jp, dtype=dtype)
    delta = 0.409 * np.sin(jp - 1.39, dtype=dtype)
    phi = lat * np.pi / 180.0
    w_s = np.arccos(-np.tan(phi, dtype=dtype) * np.tan(delta, dtype=dtype))
    R_a = (
        24.0
        * 60.0
        / np.pi
        * 0.082
        * d_r
        * (
            w_s * np.sin(phi, dtype=dtype) * np.sin(delta, dtype=dtype)
            + np.cos(phi, dtype=dtype)
            * np.cos(delta, dtype=dtype)
            * np.sin(w_s, dtype=dtype)
        )
    )
    R_so = (0.75 + 2e-5 * ds["elevation"]) * R_a
    R_ns = (1.0 - alb) * R_s
    R_nl = (
        4.903e-9
        * (((ds["tmax"] + 273.16) ** 4 + (ds["tmin"] + 273.16) ** 4) * 0.5)
        * (0.34 - 0.14 * np.sqrt(ds["vp"]))
        * ((1.35 * R_s / R_so) - 0.35)
    )
    ds["R_n"] = R_ns - R_nl

    ds["pet"] = (
        0.408 * ds["delta"] * (ds["R_n"] - G)
        + ds["gamma"] * 900.0 / (ds["tmean"] + 273.0) * u_2 * ds["e_def"]
    ) / (ds["delta"] + ds["gamma"] * (1 + 0.34 * u_2))
    ds["pet"].attrs["units"] = "mm/day"

    ds["time"] = dates
    ds["vp"] *= 1.0e3

    ds = ds.drop_vars(["delta", "gamma", "e_def", "R_n"])

    return ds


def mean_monthly(daily):
    """Compute monthly mean for the regime curve."""
    import calendar

    d = dict(enumerate(calendar.month_abbr))
    mean_month = daily.groupby(daily.index.month).mean()
    mean_month.index = mean_month.index.map(d)
    return mean_month


def exceedance(daily):
    """Compute Flow duration (rank, sorted obs).

    The zero discharges are handled by dropping since log 0 is undefined.
    """

    if not isinstance(daily, pd.Series):
        msg = "The input should be of type pandas Series."
        raise TypeError(msg)

    rank = daily.rank(ascending=False, pct=True) * 100
    fdc = pd.concat([daily, rank], axis=1)
    fdc.columns = ["Q", "rank"]
    fdc.sort_values(by=["rank"], inplace=True)
    fdc.set_index("rank", inplace=True, drop=True)
    return fdc


def interactive_map(bbox):
    """An interactive map including all USGS stations within a bounding box.

    Only stations that record(ed) daily streamflow data are included.

    Parameters
    ----------
    bbox : list
        List of corners in this order [west, south, east, north]

    Returns
    -------
    folium.Map
    """
    import folium
    import hydrodata.datasets as hds

    if not isinstance(bbox, list):
        raise ValueError("bbox should be a list: [west, south, east, north]")

    df = hds.nwis_siteinfo(bbox=bbox)
    df = df[
        [
            "site_no",
            "station_nm",
            "dec_lat_va",
            "dec_long_va",
            "alt_va",
            "alt_datum_cd",
            "huc_cd",
            "begin_date",
            "end_date",
            "hcdn_2009",
        ]
    ]
    df["coords"] = [
        (lat, lon)
        for lat, lon in df[["dec_lat_va", "dec_long_va"]].itertuples(
            name=None, index=False
        )
    ]
    df["altitude"] = (
        df["alt_va"].astype(str) + " ft above " + df["alt_datum_cd"].astype(str)
    )
    df = df.drop(columns=["dec_lat_va", "dec_long_va", "alt_va", "alt_datum_cd"])

    dr = hds.nwis_siteinfo(bbox=bbox, expanded=True)[
        ["site_no", "drain_area_va", "contrib_drain_area_va"]
    ]
    df = df.merge(dr, on="site_no").dropna()

    df["drain_area_va"] = df["drain_area_va"].astype(str) + " square miles"
    df["contrib_drain_area_va"] = (
        df["contrib_drain_area_va"].astype(str) + " square miles"
    )

    df = df[
        [
            "site_no",
            "station_nm",
            "coords",
            "altitude",
            "huc_cd",
            "drain_area_va",
            "contrib_drain_area_va",
            "begin_date",
            "end_date",
            "hcdn_2009",
        ]
    ]
    df.columns = [
        "Site No.",
        "Station Name",
        "Coordinate",
        "Altitude",
        "HUC8",
        "Drainage Area",
        "Contributing Drainga Area",
        "Begin date",
        "End data",
        "HCDN 2009",
    ]

    msgs = []
    for row in df.itertuples(index=False):
        msg = ""
        for col in df.columns:
            msg += "".join(
                ["<strong>", col, "</strong> : ", f"{row[df.columns.get_loc(col)]}<br>"]
            )
        msgs.append(msg[:-4])

    df["msg"] = msgs
    df = df[["Coordinate", "msg"]]

    west, south, east, north = bbox
    lon = (west + east) * 0.5
    lat = (south + north) * 0.5

    m = folium.Map(location=(lat, lon), tiles="Stamen Terrain", zoom_start=12)

    for coords, msg in df.itertuples(name=None, index=False):
        folium.Marker(
            location=coords, popup=folium.Popup(msg, max_width=250), icon=folium.Icon()
        ).add_to(m)

    return m


def prepare_nhdplus(
    fl,
    min_network_size,
    min_path_length,
    min_path_size=0,
    purge_non_dendritic=True,
    warn=True,
):
    """Cleaning up and fixing issue in NHDPlus flowline database.

    Ported from `nhdplusTools <https://github.com/USGS-R/nhdplusTools>`_

    Parameters
    ----------
    fl : (Geo)DataFrame
        NHDPlus flowlines with at least the following columns:
        COMID, LENGTHKM, FTYPE, TerminalFl, FromNode, ToNode, TotDASqKM,
        StartFlag, StreamOrde, StreamCalc, TerminalPa, Pathlength,
        Divergence, Hydroseq, LevelPathI
    min_network_size : float
        Minimum size of drainage network in sqkm
    min_path_length : float
        Minimum length of terminal level path of a network in km.
    min_path_size : float
        Minimum size of outlet level path of a drainage basin in km.
        Drainage basins with an outlet drainage area smaller than
        this value will be removed.
    purge_non_dendritic : bool
        Whether to remove non dendritic paths.
    warn : bool
        Whether to show a message about the removed features, defaults to True.

    Returns
    -------
    (Geo)DataFrame
        With an additional column named ``tocomid`` that represents downstream
        comid of features.
    """
    req_cols = [
        "comid",
        "lengthkm",
        "ftype",
        "terminalfl",
        "fromnode",
        "tonode",
        "totdasqkm",
        "startflag",
        "streamorde",
        "streamcalc",
        "terminalpa",
        "pathlength",
        "divergence",
        "hydroseq",
        "levelpathi",
    ]
    fl.columns = map(str.lower, fl.columns)
    if any(c not in fl.columns for c in req_cols):
        msg = "The required columns are not in the provided flowline dataframe."
        msg += f" The required columns are {', '.join(c for c in req_cols)}"
        raise ValueError(msg)

    extra_cols = ["comid"] + [c for c in fl.columns if c not in req_cols]
    int_cols = [
        "comid",
        "terminalfl",
        "fromnode",
        "tonode",
        "startflag",
        "streamorde",
        "streamcalc",
        "terminalpa",
        "divergence",
        "hydroseq",
        "levelpathi",
    ]
    for c in int_cols:
        fl[c] = fl[c].astype("Int64")

    fls = fl[req_cols].copy()
    if not any(fls.terminalfl == 1):
        if all(fls.terminalpa == fls.terminalpa.iloc[0]):
            fls.loc[fls.hydroseq == fls.hydroseq.min(), "terminalfl"] = 1
        else:
            raise ValueError("No terminal flag were found in the dataframe.")

    if purge_non_dendritic:
        fls = fls[
            ((fls.ftype != "Coastline") | (fls.ftype != 566))
            & (fls.streamorde == fls.streamcalc)
        ]
    else:
        fls = fls[(fls.ftype != "Coastline") | (fls.ftype != 566)]
        fls.loc[fls.divergence == 2, "fromnode"] = pd.NA

    if min_path_size > 0:
        short_paths = fls.groupby("levelpathi").apply(
            lambda x: (x.hydroseq == x.hydroseq.min())
            & (x.totdasqkm < min_path_size)
            & (x.totdasqkm >= 0)
        )
        short_paths = short_paths.index.get_level_values("levelpathi")[
            short_paths
        ].tolist()
        fls = fls[~fls.levelpathi.isin(short_paths)]
    terminal_filter = (fls.terminalfl == 1) & (fls.totdasqkm < min_network_size)
    start_filter = (fls.startflag == 1) & (fls.pathlength < min_path_length)
    if any(terminal_filter.dropna()) or any(start_filter.dropna()):
        tiny_networks = fls[terminal_filter].append(fls[start_filter])
        fls = fls[~fls.terminalpa.isin(tiny_networks.terminalpa.unique())]

    n_rm = fl.shape[0] - fls.shape[0]
    if n_rm > 0:
        print(f"Removed {n_rm} rows from the flowlines database.")

    if fls.shape[0] > 0:
        fl_gr = fls.groupby("terminalpa")
        fl_li = [fl_gr.get_group(g) for g in fl_gr.groups]

        def tocomid(ft):
            def toid(row):
                try:
                    return ft[ft.fromnode == row.tonode].comid.values[0]
                except IndexError:
                    return pd.NA

            return ft.apply(toid, axis=1)

        fls["tocomid"] = pd.concat(map(tocomid, fl_li))

    return gpd.GeoDataFrame(pd.merge(fls, fl[extra_cols], on="comid", how="left"))


def traverse_json(obj, path):
    """Extracts an element from a JSON file along a specified path.

    Notes
    ----
    From `bcmullins <https://bcmullins.github.io/parsing-json-python/>`_

    Parameters
    ----------
    obj : dict
        The input json dictionary
    path : list of strings
        The path to the requested element

    Returns
    -------
    list
    """

    def extract(obj, path, ind, arr):
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr

    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr


def cover_statistics(ds):
    """Percentages of the categorical NLCD cover data

    Parameters
    ----------
    ds : xarray.Dataset

    Returns
    -------
    dict
        Percentages of classes and categories
    """
    nlcd_meta = helpers.nlcd_helper()
    cover_arr = ds.values
    total_pix = np.count_nonzero(~np.isnan(cover_arr))

    class_percentage = dict(
        zip(
            list(nlcd_meta["classes"].values()),
            [
                cover_arr[cover_arr == int(cat)].shape[0] / total_pix * 100.0
                for cat in list(nlcd_meta["classes"].keys())
            ],
        )
    )

    cat_list = (
        np.array([np.count_nonzero(cover_arr // 10 == c) for c in range(10) if c != 6])
        / total_pix
        * 100.0
    )

    category_percentage = dict(zip(list(nlcd_meta["categories"].keys()), cat_list))

    return {"classes": class_percentage, "categories": category_percentage}


def create_dataset(content, mask, transform, width, height, name, fpath):
    """Create dataset from a response clipped by a geometry

    Parameters
    ---------
    content : requests.Response
        The response to be processed
    mask : numpy.ndarray
        The mask to clip the data
    transform : tuple
        Transform of the mask
    width : int
        x-dimension of the data
    heigth : int
        y-dimension of the data
    name : string
        Variable name in the dataset
    fpath : string or Path
        The path save the file

    Returns
    -------
    xarray.Dataset
    """
    import xarray as xr

    with rio.MemoryFile() as memfile:
        memfile.write(content)
        with memfile.open() as src:
            if src.nodata is None:
                try:
                    nodata = np.iinfo(src.dtypes[0]).max
                except ValueError:
                    nodata = np.nan
            else:
                nodata = np.dtype(src.dtypes[0]).type(src.nodata)

            meta = src.meta
            meta.update(
                {
                    "width": width,
                    "height": height,
                    "transform": transform,
                    "nodata": nodata,
                }
            )

            if fpath is not None:
                with rio.open(fpath, "w", **meta) as dest:
                    dest.write_mask(~mask)
                    dest.write(src.read())

            with rio.vrt.WarpedVRT(src, **meta) as vrt:
                ds = xr.open_rasterio(vrt)
                try:
                    ds = ds.squeeze("band", drop=True)
                except ValueError:
                    pass
                ds = ds.where(~mask, other=vrt.nodata)
                ds.name = name

                ds.attrs["transform"] = transform
                ds.attrs["res"] = (transform[0], transform[4])
                ds.attrs["bounds"] = tuple(vrt.bounds)
                ds.attrs["nodatavals"] = vrt.nodatavals
                ds.attrs["crs"] = vrt.crs.to_string()
    return ds


def geom_mask(
    geometry, width, height, geo_crs="epsg:4326", ds_crs="epsg:4326", all_touched=True
):
    """Create a mask array and transform for a given geometry.

    Parameters
    ----------
    geometry : Polygon
        A shapely Polygon geometry
    width : int
        x-dimension of the data
    heigth : int
        y-dimension of the data
    geo_crs : string, CRS
        CRS of the geometry, defaults to epsg:4326
    ds_crs : string, CRS
        CRS of the dataset to be masked, defaults to epsg:4326
    all_touched : bool
        Wether to include all the elements where the geometry touchs
        rather than only the element center, defaults to True

    Returns
    -------
    (numpy.ndarray, tuple)
        mask, transform
    """
    if geo_crs != ds_crs:
        geom = rio_warp.transform_geom(geo_crs, ds_crs, mapping(geometry))
        bnds = rio_warp.transform_bounds(geo_crs, ds_crs, *geometry.bounds)
    else:
        geom = geometry
        bnds = geometry.bounds

    transform, _, _ = rio_warp.calculate_default_transform(
        ds_crs, ds_crs, width, height, *bnds
    )
    mask = rio_features.geometry_mask(
        [geom], (height, width), transform, all_touched=all_touched
    )
    return mask, transform


def check_requirements(reqs, cols):
    """Check for all the required data.

    Parameters
    ----------
    reqs : list
        A list of required data names as strings
    cols : list
        A list of data names as strings
    """
    if not isinstance(reqs, list) or not isinstance(cols, list):
        raise ValueError("Inputs should be list of strings")

    missing = [r for r in reqs if r not in cols]
    if len(missing) > 1:
        msg = "The following required data are missing:\n"
        msg += ", ".join(m for m in missing)
        raise ValueError(msg)


def topoogical_sort(network):
    """Topological sorting of a network.

    Parameters
    ----------
    network : pandas.DataFrame
        A dataframe with columns ID and toID

    Returns
    -------
    (list, dict)
        A list of topologically sorted IDs and a dictionary
        with keys as IDs and values as its upstream nodes.
        Note that the terminal node ID is set to pd.NA.
    """
    import networkx as nx

    upstream_nodes = {
        i: network[network.toID == i].ID.tolist() for i in network.ID.tolist()
    }
    upstream_nodes[pd.NA] = network[network.toID.isna()].ID.tolist()

    G = nx.from_pandas_edgelist(
        network[["ID", "toID"]], source="ID", target="toID", create_using=nx.DiGraph,
    )
    topo_sorted = list(nx.topological_sort(G))
    return topo_sorted, upstream_nodes


def vector_accumulation(
    flowlines, func, col_names, nt, id_name="comid", toid_name="tocomid"
):
    """Flow accumulation using vector river network.

    Parameters
    ----------
    flowlines : pandas.DataFrame
        A dataframe containing comid, tocomid, and all the columns
        that ara required for passing to ``func``.
    func : function
        The function that routes the flow in a signle river segment
    col_names : list of strings
        List of the flowlines columns that contain all the required
        data for a routing a single river segment such as slope, length,
        lateral flow, etc.
    nt : int
        Total number of time steps
    id_name : string, optional
        Name of the flowlines column containing IDs, defaults to comid
    toid_name : string, optional
        Name of the flowlines column containing toIDs, defaults to tocomid

    Returns
    -------
    dict
        Accumulated flow at all the nodes. The keys are the IDs and the values
        are the time series as `numpy.ndarray`s. The outlet node is called `out`.
    """
    topo_sorted, upstream_nodes = topoogical_sort(
        flowlines[[id_name, toid_name]].rename(
            columns={id_name: "ID", toid_name: "toID"}
        )
    )

    zero_arr = np.zeros(nt)

    upstream_nodes.update({k: [0] for k, v in upstream_nodes.items() if len(v) == 0})
    q = {i: zero_arr for i in flowlines.comid.to_list()}
    q[0] = zero_arr

    for i in topo_sorted[:-1]:
        q[i] = func(
            np.sum([q[u] for u in upstream_nodes[i]], axis=0),
            *flowlines.loc[flowlines[id_name] == i, col_names].values[0],
        )

    q["out"] = q[topo_sorted[-2]]
    q.pop(0)
    return q
