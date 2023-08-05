#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Accessing data from the supported databases through their APIs."""

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio as rio
from hydrodata import helpers, services, utils
from pqdm.threads import pqdm
from shapely.geometry import Polygon

import xarray as xr


def nwis_streamflow(station_ids, start, end, raw=False):
    """Get daily streamflow observations from USGS.

    Parameters
    ----------
    station_ids : string, list
        The gage ID(s)  of the USGS station
    start : string or datetime
        Start date
    end : string or datetime
        End date
    raw : bool
        Whether to return the raw data without cleanup as a Dataframe or
        remove all the columns except for ``qobs`` as a Series, default to
        False.

    Returns
    -------
    pandas.DataFrame
        Streamflow data observations in cubic meter per second (cms)
    """

    if isinstance(station_ids, str):
        station_ids = [station_ids]
    elif isinstance(station_ids, list):
        station_ids = [str(i) for i in station_ids]
    else:
        raise ValueError(
            "the ids argument should be either a string or a list or strings"
        )
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    siteinfo = nwis_siteinfo(station_ids)
    check_dates = siteinfo.loc[
        (siteinfo.stat_cd == "00003")
        & (start < siteinfo.begin_date)
        & (end > siteinfo.end_date),
        "site_no",
    ].tolist()
    nas = [s for s in station_ids if s in check_dates]
    if len(nas) > 0:
        msg = "Daily Mean data unavailable for the specified time period for the following stations:\n"
        msg += ", ".join(str(s) for s in nas)
        raise ValueError(msg)

    url = "https://waterservices.usgs.gov/nwis/dv"
    payload = {
        "format": "json",
        "sites": ",".join(str(s) for s in station_ids),
        "startDT": start.strftime("%Y-%m-%d"),
        "endDT": end.strftime("%Y-%m-%d"),
        "parameterCd": "00060",
        "statCd": "00003",
        "siteStatus": "all",
    }

    session = utils.retry_requests()
    r = utils.post_url(session, url, payload)

    ts = r.json()["value"]["timeSeries"]
    r_ts = {
        t["sourceInfo"]["siteCode"][0]["value"]: t["values"][0]["value"] for t in ts
    }

    def to_df(col, dic):
        q = pd.DataFrame.from_records(dic, exclude=["qualifiers"], index=["dateTime"])
        q.index = pd.to_datetime(q.index)
        q.columns = [col]
        q[col] = q[col].astype("float64") * 0.028316846592  # Convert cfs to cms
        return q

    qobs = pd.concat([to_df(f"USGS-{s}", t) for s, t in r_ts.items()], axis=1)
    return qobs


def nwis_siteinfo(ids=None, bbox=None, expanded=False):
    """Get NWIS stations by a list of IDs or within a bounding box.

    Only stations that record(ed) daily streamflow data are returned.
    The following columns are included in the dataframe:
    site_no         -- Site identification number
    station_nm      -- Site name
    site_tp_cd      -- Site type
    dec_lat_va      -- Decimal latitude
    dec_long_va     -- Decimal longitude
    coord_acy_cd    -- Latitude-longitude accuracy
    dec_coord_datum_cd -- Decimal Latitude-longitude datum
    alt_va          -- Altitude of Gage/land surface
    alt_acy_va      -- Altitude accuracy
    alt_datum_cd    -- Altitude datum
    huc_cd          -- Hydrologic unit code
    parm_cd         -- Parameter code
    stat_cd         -- Statistical code
    ts_id           -- Internal timeseries ID
    loc_web_ds      -- Additional measurement description
    medium_grp_cd   -- Medium group code
    parm_grp_cd     -- Parameter group code
    srs_id          -- SRS ID
    access_cd       -- Access code
    begin_date      -- Begin date
    end_date        -- End date
    count_nu        -- Record count
    hcdn_2009       -- Whether is in HCDN-2009 stations

    Parameters
    ----------
    ids : string or list of strings
        Station ID(s)
    bbox : list
        List of corners in this order [west, south, east, north]
    expanded : bool, optional
        Whether to get expanded sit information for example drainage area.

    Returns
    -------
    pandas.DataFrame
    """
    if bbox is not None and ids is None:
        if isinstance(bbox, list) or isinstance(bbox, tuple):
            if len(bbox) == 4:
                query = {"bBox": ",".join(f"{b:.06f}" for b in bbox)}
            else:
                raise TypeError(
                    "The bounding box should be a list or tuple of length 4: [west, south, east, north]"
                )
        else:
            raise TypeError(
                "The bounding box should be a list or tuple of length 4: [west, south, east, north]"
            )

    elif ids is not None and bbox is None:
        if isinstance(ids, str):
            query = {"sites": ids}
        elif isinstance(ids, list):
            query = {"sites": ",".join(str(i) for i in ids)}
        else:
            raise ValueError(
                "the ids argument should be either a string or a list or strings"
            )
    else:
        raise ValueError("Either ids or bbox argument should be provided.")

    url = "https://waterservices.usgs.gov/nwis/site"

    if expanded:
        outputType = {"siteOutput": "expanded"}
    else:
        outputType = {"outputDataTypeCd": "dv"}

    payload = {
        **query,
        **outputType,
        "format": "rdb",
        "parameterCd": "00060",
        "siteStatus": "all",
        "hasDataTypeCd": "dv",
    }

    session = utils.retry_requests()
    r = utils.post_url(session, url, payload)

    r_text = r.text.split("\n")
    r_list = [l.split("\t") for l in r_text if "#" not in l]
    r_dict = [dict(zip(r_list[0], st)) for st in r_list[2:]]

    df = pd.DataFrame.from_dict(r_dict).dropna()
    df = df.drop(df[df.alt_va == ""].index)
    try:
        df = df[df.parm_cd == "00060"]
        df["begin_date"] = pd.to_datetime(df["begin_date"])
        df["end_date"] = pd.to_datetime(df["end_date"])
    except AttributeError:
        pass

    df[["dec_lat_va", "dec_long_va", "alt_va"]] = df[
        ["dec_lat_va", "dec_long_va", "alt_va"]
    ].astype("float64")

    df = df[df.site_no.apply(len) == 8]
    df["hcdn_2009"] = df.site_no.isin(helpers.hcdn_stations())

    return df


def daymet_byloc(lon, lat, start=None, end=None, years=None, variables=None, pet=False):
    """Get daily climate data from Daymet for a single point.

    Parameters
    ----------
    lon : float
        Longitude of the point of interest
    lat : float
        Latitude of the point of interest
    start : string or datetime
        Start date
    end : string or datetime
        End date
    years : list
        List of years
    variables : string or list
        List of variables to be downloaded. The acceptable variables are:
        tmin, tmax, prcp, srad, vp, swe, dayl
        Descriptions can be found in https://daymet.ornl.gov/overview
    pet : bool
        Whether to compute evapotranspiration based on
        `UN-FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`_.
        The default is False

    Returns
    -------
    Pandas DataFrame
        Climate data for the requested location and variables
    """

    if not (14.5 < lat < 52.0) or not (-131.0 < lon < -53.0):
        msg = "The location is outside the Daymet dataset. The acceptable range is: "
        msg += "14.5 < lat < 52.0 and -131.0 < lon < -53.0"
        raise ValueError(msg)

    if years is None and start is not None and end is not None:
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        if start < pd.to_datetime("1980-01-01"):
            raise ValueError("Daymet database ranges from 1980 till present.")
    elif years is not None and start is None and end is None:
        years = years if isinstance(years, list) else [years]
    else:
        raise ValueError("Either years or start and end arguments should be provided.")

    vars_table = pd.read_html("https://daymet.ornl.gov/overview")[1]
    valid_variables = vars_table.Abbr.values

    if variables is not None:
        variables = variables if isinstance(variables, list) else [variables]

        invalid = [v for v in variables if v not in valid_variables]
        if len(invalid) > 0:
            msg = "These required variables are not in the dataset: "
            msg += ", ".join(x for x in invalid)
            msg += f'\nRequired variables are {", ".join(x for x in valid_variables)}'
            raise KeyError(msg)

        if pet:
            reqs = ["tmin", "tmax", "vp", "srad", "dayl"]
            variables = list(set(reqs) | set(variables))
    else:
        variables = valid_variables

    url = "https://daymet.ornl.gov/single-pixel/api/data"
    if years is None:
        dates = {"start": start.strftime("%Y-%m-%d"), "end": end.strftime("%Y-%m-%d")}
    else:
        dates = {"years": ",".join(str(x) for x in years)}

    payload = {
        "lat": round(lat, 6),
        "lon": round(lon, 6),
        "vars": ",".join(x for x in variables),
        "format": "json",
        **dates,
    }

    session = utils.retry_requests()
    r = utils.get_url(session, url, payload)

    df = pd.DataFrame(r.json()["data"])
    df.index = pd.to_datetime(df.year * 1000.0 + df.yday, format="%Y%j")
    df.drop(["year", "yday"], axis=1, inplace=True)

    if pet:
        df = utils.pet_fao_byloc(df, lon, lat)
    return df


def daymet_bygeom(
    geometry,
    start=None,
    end=None,
    years=None,
    variables=None,
    pet=False,
    resolution=None,
    fill_holes=False,
    n_threads=4,
    verbose=False,
):
    """Gridded data from the Daymet database.

    The data is clipped using netCDF Subset Service.

    Parameters
    ----------
    geometry : Polygon, box
        The geometry of the region of interest
    start : string or datetime
        Starting date
    end : string or datetime
        Ending date
    years : list
        List of years
    variables : string or list
        List of variables to be downloaded. The acceptable variables are:
        tmin, tmax, prcp, srad, vp, swe, dayl
        Descriptions can be found in https://daymet.ornl.gov/overview
    pet : bool
        Whether to compute evapotranspiration based on
        `UN-FAO 56 paper <http://www.fao.org/docrep/X0490E/X0490E00.htm>`_.
        The default is False
    resolution : float
        The desired output resolution for the output in km,
        defaults to no resampling. The resampling is done using bilinear method
    fill_holes : bool, optional
        Whether to fill the holes in the geometry's interior, defaults to False.
    n_threads : int, optional
        Number of threads for simultanious download, defaults to 4 and max is 8.
    verbose : bool, optional
        Whether to show more information during runtime, defaults to False

    Returns
    -------
    xarray.DataArray
        The climate data within the requested geometery.
    """

    from pandas.tseries.offsets import DateOffset

    base_url = "https://thredds.daac.ornl.gov/thredds/ncss/ornldaac/1328/"

    if years is None and start is not None and end is not None:
        start = pd.to_datetime(start) + DateOffset(hour=12)
        end = pd.to_datetime(end) + DateOffset(hour=12)
        if start < pd.to_datetime("1980-01-01"):
            raise ValueError("Daymet database ranges from 1980 till 2019.")
        dates = utils.daymet_dates(start, end)
    elif years is not None and start is None and end is None:
        years = years if isinstance(years, list) else [years]
        start_list, end_list = [], []
        for year in years:
            s = pd.to_datetime(f"{year}0101")
            start_list.append(s + DateOffset(hour=12))
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                end_list.append(pd.to_datetime(f"{year}1230") + DateOffset(hour=12))
            else:
                end_list.append(pd.to_datetime(f"{year}1231") + DateOffset(hour=12))
        dates = [(s, e) for s, e in zip(start_list, end_list)]
    else:
        raise ValueError("Either years or start and end arguments should be provided.")

    vars_table = pd.read_html("https://daymet.ornl.gov/overview")[1]
    units = dict(zip(vars_table["Abbr"], vars_table["Units"]))
    valid_variables = vars_table.Abbr.values

    if variables is not None:
        variables = variables if isinstance(variables, list) else [variables]

        invalid = [v for v in variables if v not in valid_variables]
        if len(invalid) > 0:
            msg = "These required variables are not in the dataset: "
            msg += ", ".join(x for x in invalid)
            msg += f'\nRequired variables are {", ".join(x for x in valid_variables)}'
            raise KeyError(msg)

        if pet:
            reqs = ["tmin", "tmax", "vp", "srad", "dayl"]
            variables = list(set(reqs) | set(variables))
    else:
        if pet:
            variables = ["tmin", "tmax", "vp", "srad", "dayl"]
        else:
            variables = valid_variables

    if not isinstance(geometry, Polygon):
        raise TypeError("The geometry argument should be of Shapely's Polygon type.")
    elif fill_holes:
        geometry = Polygon(geometry.exterior)

    n_threads = min(n_threads, 8)

    west, south, east, north = np.round(geometry.bounds, 6)
    urls = []
    for s, e in dates:
        for v in variables:
            urls.append(
                base_url
                + "&".join(
                    [
                        f"{s.year}/daymet_v3_{v}_{s.year}_na.nc4?var=lat",
                        "var=lon",
                        f"var={v}",
                        f"north={north}",
                        f"west={west}",
                        f"east={east}",
                        f"south={south}",
                        "disableProjSubset=on",
                        "horizStride=1",
                        f'time_start={s.strftime("%Y-%m-%dT%H:%M:%SZ")}',
                        f'time_end={e.strftime("%Y-%m-%dT%H:%M:%SZ")}',
                        "timeStride=1",
                        "accept=netcdf",
                    ]
                )
            )
    session = utils.retry_requests()

    def getter(url):
        return xr.open_dataset(utils.get_url(session, url).content)

    data = xr.merge(
        pqdm(
            urls, getter, n_jobs=n_threads, desc=f"Gridded Daymet", disable=not verbose
        )
    )

    for k, v in units.items():
        if k in variables:
            data[k].attrs["units"] = v

    data = data.drop_vars(["lambert_conformal_conic"])
    data.attrs[
        "crs"
    ] = "+proj=lcc +lon_0=-100 +lat_0=42.5 +lat_1=25 +lat_2=60 +ellps=WGS84"

    x_res, y_res = float(data.x.diff("x").min()), float(data.y.diff("y").min())
    x_origin = data.x.values[0] - x_res / 2.0  # PixelAsArea Convention
    y_origin = data.y.values[0] - y_res / 2.0  # PixelAsArea Convention

    transform = (x_res, 0, x_origin, 0, y_res, y_origin)

    x_end = x_origin + data.dims.get("x") * x_res
    y_end = y_origin + data.dims.get("y") * y_res
    x_options = np.array([x_origin, x_end])
    y_options = np.array([y_origin, y_end])

    data.attrs["transform"] = transform
    data.attrs["res"] = (x_res, y_res)
    data.attrs["bounds"] = (
        x_options.min(),
        y_options.min(),
        x_options.max(),
        y_options.max(),
    )

    if pet:
        data = utils.pet_fao_gridded(data)

    mask, transform = utils.geom_mask(
        geometry, data.dims["x"], data.dims["y"], ds_crs=data.crs
    )
    data = data.where(~xr.DataArray(mask, dims=("y", "x")), drop=True)
    return data


class NLDI:
    """Access to the Hydro Network-Linked Data Index (NLDI) service."""

    @classmethod
    def starting_comid(cls, station_id):
        """Find starting ComID based on the USGS station."""
        return cls.navigate("nwissite", station_id, navigation=None).comid.tolist()[0]

    @classmethod
    def comids(cls, station_id):
        """Find ComIDs of all the flowlines."""
        return cls.navigate("nwissite", station_id).comid.tolist()

    @classmethod
    def tributaries(cls, station_id):
        """Get upstream tributaries of the watershed."""
        return cls.navigate("nwissite", station_id)

    @classmethod
    def main(cls, station_id):
        """Get upstream main channel of the watershed."""
        return cls.navigate("nwissite", station_id, "upstreamMain")

    @classmethod
    def stations(cls, station_id, navigation="upstreamTributaries", distance=None):
        """Get USGS stations up/downstream of a station.

        Parameters
        ----------
        station_id : string
            The USGS station ID.
        navigation : string, optional
            The direction for navigating the NHDPlus database. The valid options are:
            None, ``upstreamMain``, ``upstreamTributaries``,``downstreamMain``,
            ``downstreamDiversions``. Defaults to upstreamTributaries.
        distance : float, optional
            The distance to limit the navigation in km. Defaults to None (all stations).

        Returns
        -------
        GeoDataFrame
        """
        return cls.navigate("nwissite", station_id, navigation, "nwissite", distance)

    @classmethod
    def pour_points(cls, station_id):
        """Get upstream tributaries of the watershed."""
        return cls.navigate("nwissite", station_id, dataSource="huc12pp")

    @classmethod
    def flowlines(cls, station_id):
        """Get flowlines for the entire watershed from NHDPlus V2"""
        return nhdplus_byid("nhdflowline_network", cls.comids(station_id))

    @classmethod
    def catchments(cls, station_id):
        """Get chatchments for the entire watershed from NHDPlus V2"""
        return nhdplus_byid("catchmentsp", cls.comids(station_id))

    @staticmethod
    def basin(station_id):
        """Get USGS stations basins using NLDI service."""
        crs = "epsg:4326"
        url = (
            "https://labs.waterdata.usgs.gov/api/nldi/linked-data"
            + f"/nwissite/USGS-{station_id}/basin"
        )
        r = utils.get_url(utils.retry_requests(), url)
        gdf = gpd.GeoDataFrame.from_features(r.json(), crs=crs)
        gdf.crs = crs

        return gdf

    @staticmethod
    def navigate(
        feature,
        featureids,
        navigation="upstreamTributaries",
        dataSource="flowline",
        distance=None,
    ):
        """Navigate NHDPlus V2 based on ComID(s).

        Parameters
        ----------
        feature : string
            The requested feature. The valid features are ``nwissite`` and ``comid``.
        featureids : string or list
            The ID(s) of the requested feature.
        navigation : string, optional
            The direction for navigating the NHDPlus database. The valid options are:
            None, ``upstreamMain``, ``upstreamTributaries``,``downstreamMain``,
            ``downstreamDiversions``. Defaults to upstreamTributaries.
        distance : float, optional
            The distance to limit the navigation in km. Defaults to None (limitless).
        dataSource : string, optional
            The data source to be navigated. Acceptable options are ``flowline`` for flowlines,
            ``nwissite`` for USGS stations and ``huc12pp`` for HUC12 pour points.
            Defaults to None.

        Returns
        -------
        GeoDataFrame
        """
        valid_features = ["comid", "nwissite"]
        if feature not in valid_features:
            msg = "The acceptable feature options are:"
            msg += f" {', '.join(x for x in valid_features)}"
            raise ValueError(msg)

        valid_dataSource = ["flowline", "nwissite", "huc12pp"]
        if dataSource not in valid_dataSource:
            msg = "The acceptable dataSource options are:"
            msg += f"{', '.join(x for x in valid_dataSource)}"
            raise ValueError(msg)

        if not isinstance(featureids, list):
            featureids = [featureids]

        if feature == "nwissite":
            featureids = ["USGS-" + str(f) for f in featureids]

        if len(featureids) == 0:
            raise ValueError("The featureID list is empty!")

        ds = "" if dataSource == "flowline" else f"/{dataSource}"
        dis = "" if distance is None else f"?distance={distance}"

        nav_options = {
            "upstreamMain": "UM",
            "upstreamTributaries": "UT",
            "downstreamMain": "DM",
            "downstreamDiversions": "DD",
        }
        if navigation is not None and navigation not in list(nav_options.keys()):
            msg = "The acceptable navigation options are:"
            msg += f" {', '.join(x for x in list(nav_options.keys()))}"
            raise ValueError(msg)
        elif navigation is None:
            nav = ""
        else:
            nav = f"navigate/{nav_options[navigation]}{ds}{dis}"

        base_url = f"https://labs.waterdata.usgs.gov/api/nldi/linked-data/{feature}"
        crs = "epsg:4326"
        session = utils.retry_requests()

        def get_url(fid):
            url = f"{base_url}/{fid}/{nav}"

            r = utils.get_url(session, url)
            return gpd.GeoDataFrame.from_features(r.json(), crs=crs)

        gdf = gpd.GeoDataFrame(pd.concat(get_url(fid) for fid in featureids))
        comid = "nhdplus_comid" if dataSource == "flowline" else "comid"
        gdf = gdf.rename(columns={comid: "comid"})
        gdf = gdf[["comid", "geometry"]]
        gdf["comid"] = gdf.comid.astype("int64")
        gdf.crs = crs

        return gdf


def nhdplus_bybox(feature, bbox):
    """Get NHDPlus flowline database within a bounding box.

    Parameters
    ----------
    feature : string
        The NHDPlus feature to be downloaded. Valid features are:
        ``nhdarea``, ``nhdwaterbody``, ``catchmentsp``, and ``nhdflowline_network``
    bbox : list
        The bounding box for the region of interest in WGS 83, defaults to None.
        The list should provide the corners in this order:
        [west, south, east, north]

    Returns
    -------
    GeoDataFrame
    """

    valid_features = ["nhdarea", "nhdwaterbody", "catchmentsp", "nhdflowline_network"]
    if feature not in valid_features:
        msg = f"The provided feature, {feature}, is not valid."
        msg += f" Valid features are {', '.join(x for x in valid_features)}"
        raise ValueError(msg)

    wfs = services.USGSGeoserver("wfs", feature)
    r = wfs.getfeature_bybox(bbox)

    crs = "epsg:4326"
    gdf = gpd.GeoDataFrame.from_features(r.json(), crs=crs)
    gdf.crs = crs
    if gdf.shape[0] == 0:
        raise KeyError(
            f"No feature was found in bbox({', '.join(str(round(x, 3)) for x in bbox)})"
        )

    return gdf


def nhdplus_byid(feature, featureids):
    """Get flowlines or catchments from NHDPlus V2 based on ComIDs.

    Parameters
    ----------
    feature : string
        The requested feature. The valid features are:
        ``catchmentsp`` and ``nhdflowline_network``
    featureids : string or list
        The ID(s) of the requested feature.

    Returns
    -------
    GeoDataFrame
    """
    valid_features = ["catchmentsp", "nhdflowline_network"]
    if feature not in valid_features:
        msg = f"The provided feature, {feature}, is not valid."
        msg += f"Valid features are {', '.join(x for x in valid_features)}"
        raise ValueError(msg)

    wfs = services.USGSGeoserver("wfs", feature)
    propertyname = "featureid" if feature == "catchmentsp" else "comid"
    r = wfs.getfeature_byid(propertyname, featureids)

    crs = "epsg:4326"
    gdf = gpd.GeoDataFrame.from_features(r.json(), crs=crs)
    gdf.crs = crs
    if gdf.shape[0] == 0:
        raise KeyError("No feature was found with the provided IDs")
    return gdf


def ssebopeta_byloc(lon, lat, start=None, end=None, years=None, verbose=False):
    """Gridded data from the SSEBop database.

    The data is clipped using netCDF Subset Service.

    Parameters
    ----------
    geom : list
        The bounding box for downloading the data. The order should be
        as follows:
        geom = [west, south, east, north]
    start : string or datetime
        Starting date
    end : string or datetime
        Ending date
    years : list
        List of years
    verbose : bool, optional
        Whether to show more information during runtime, defaults to False

    Returns
    -------
    xarray.DataArray
        The actual ET for the requested region.
    """

    import zipfile
    import io

    f_list = utils.get_ssebopeta_urls(start=start, end=end, years=years)
    session = utils.retry_requests()

    elevations = {}
    with utils.onlyIPv4():

        def _ssebop(urls):
            dt, url = urls
            r = utils.get_url(session, url)
            z = zipfile.ZipFile(io.BytesIO(r.content))

            with rio.MemoryFile() as memfile:
                memfile.write(z.read(z.filelist[0].filename))
                with memfile.open() as src:
                    return {
                        "dt": dt,
                        "eta": [e[0] for e in src.sample([(lon, lat)])][0],
                    }

        elevations = pqdm(
            f_list, _ssebop, n_jobs=4, desc="Single pixel SSEBop", disable=not verbose
        )
    data = pd.DataFrame.from_records(elevations)
    data.columns = ["datetime", "eta (mm/day)"]
    data.set_index("datetime", inplace=True)
    return data * 1e-3


def ssebopeta_bygeom(
    geometry,
    start=None,
    end=None,
    years=None,
    resolution=None,
    fill_holes=False,
    verbose=False,
):
    """Gridded data from the SSEBop database.

    Notes
    ----
    Since there's still no web service available for subsetting, the data first
    needs to be downloaded for the requested period then the data is masked by the
    region interest locally. Therefore, it's not as fast as other functions and
    the bottleneck could be the download speed.

    Parameters
    ----------
    geometry : Geometry
        The geometry for downloading clipping the data. For a box geometry,
        the order should be as follows:
        geom = box(minx, miny, maxx, maxy)
    start : string or datetime
        Starting date
    end : string or datetime
        Ending date
    years : list
        List of years
    fill_holes : bool, optional
        Whether to fill the holes in the geometry's interior, defaults to False.
    verbose : bool, optional
        Whether to show more information during runtime, defaults to False

    Returns
    -------
    xarray.DataArray
        The actual ET for the requested region at 1 km resolution.
    """

    import zipfile
    import io

    if not isinstance(geometry, Polygon):
        raise TypeError("Geometry should be of type Shapely Polygon.")
    elif fill_holes:
        geometry = Polygon(geometry.exterior)

    resolution = 1.0e3 / 6371000.0 * 3600.0 / np.pi * 180.0
    west, south, east, north = geometry.bounds

    width = int((east - west) * 3600 / resolution)
    height = int(abs(north - south) / abs(east - west) * width)

    mask, transform = utils.geom_mask(geometry, width, height)
    f_list = utils.get_ssebopeta_urls(start=start, end=end, years=years)

    session = utils.retry_requests()

    with utils.onlyIPv4():

        def _ssebop(url_stamped):
            dt, url = url_stamped
            r = utils.get_url(session, url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            return (dt, z.read(z.filelist[0].filename))

        resp = pqdm(
            f_list, _ssebop, n_jobs=4, desc=f"Gridded SSEBop", disable=not verbose
        )

        data = utils.create_dataset(
            resp[0][1], mask, transform, width, height, "eta", None
        )
        data = data.expand_dims(dict(time=[resp[0][0]]))

        if len(resp) > 1:
            for dt, r in resp:
                ds = utils.create_dataset(
                    r, mask, transform, width, height, "eta", None
                )
                ds = ds.expand_dims(dict(time=[dt]))
                data = xr.merge([data, ds])

    eta = data.eta.copy()
    eta = eta.where(eta < eta.nodatavals[0], drop=True)
    eta *= 1e-3
    eta.attrs.update({"units": "mm/day", "nodatavals": (np.nan,)})
    return eta


def nlcd(
    geometry,
    years=None,
    width=None,
    resolution=None,
    file_path=None,
    fill_holes=False,
    in_crs="epsg:4326",
    out_crs="epsg:4326",
):
    """Get data from NLCD database (2016).

    Download land use, land cover data from NLCD2016 database within
    a given geometry in epsg:4326.

    Notes
    ----
        NLCD data has a resolution of 1 arc-sec (~30 m).

    Parameters
    ----------
    geometry : Shapely Polygon
        The geometry for extracting the data.
    years : dict, optional
        The years for NLCD data as a dictionary, defaults to
        {'impervious': 2016, 'cover': 2016, 'canopy': 2016}.
    width : int
        The width of the output image in pixels. The height is computed
        automatically from the geometry's bounding box aspect ratio. Either width
        or resolution should be provided.
    resolution : float
        The data resolution in arc-seconds. The width and height are computed in pixel
        based on the geometry bounds and the given resolution. Either width or
        resolution should be provided.
    file_path : dict, optional
        The path to save the downloaded images, defaults to None which will only return
        the data as ``xarray.Dataset`` and doesn't save the files. The argument should be
        a dict with keys as the variable name in the output dataframe and values as
        the path to save to the file.
    fill_holes : bool, optional
        Whether to fill the holes in the geometry's interior, defaults to False.
    in_crs : string, optional
        The spatial reference system of the input geometry, defaults to
        epsg:4326.
    out_crs : string, optional
        The spatial reference system to be used for requesting the data, defaults to
        epsg:4326.

    Returns
    -------
     xarray.DataArray (optional), tuple (optional)
         The data as a single DataArray and or the statistics in form of
         three dicts (imprevious, canopy, cover) in a tuple
    """
    nlcd_meta = helpers.nlcd_helper()

    names = ["impervious", "cover", "canopy"]
    avail_years = {n: nlcd_meta[f"{n}_years"] for n in names}

    if years is None:
        years = {"impervious": 2016, "cover": 2016, "canopy": 2016}
    if isinstance(years, dict):
        for service in years.keys():
            if years[service] not in avail_years[service]:
                msg = (
                    f"{service.capitalize()} data for {years[service]} is not in the databse."
                    + "Avaible years are:"
                    + f"{' '.join(str(x) for x in avail_years[service])}"
                )
                raise ValueError(msg)
    else:
        raise TypeError("Years should be of type dict.")

    url = "https://www.mrlc.gov/geoserver/mrlc_download/wms"

    layers = {
        "canopy": f'NLCD_{years["canopy"]}_Tree_Canopy_L48',
        "cover": f'NLCD_{years["cover"]}_Land_Cover_Science_product_L48',
        "impervious": f'NLCD_{years["impervious"]}_Impervious_L48',
    }

    ds = services.wms_bygeom(
        url,
        "NLCD",
        geometry,
        width=width,
        resolution=resolution,
        layers=layers,
        outFormat="image/geotiff",
        fill_holes=fill_holes,
        in_crs=in_crs,
        out_crs=out_crs,
    )
    ds.cover.attrs["units"] = "classes"
    ds.canopy.attrs["units"] = "%"
    ds.impervious.attrs["units"] = "%"
    return ds


def nationalmap_dem(
    geometry,
    width=None,
    resolution=None,
    fill_holes=False,
    in_crs="epsg:4326",
    out_crs="epsg:4326",
    fpath=None,
):
    """Get elevation DEM from `3DEP <https://www.usgs.gov/core-science-systems/ngp/3dep>`_ service.

    The 3DEP service has multi-resolution sources so depeneding on the user
    provided resolution (or width) the data is resampled on server-side based
    on all the available data sources.

    Parameters
    ----------
    geometry : Geometry
        A shapely Polygon in WGS 84 (epsg:4326).
    width : int
        The width of the output image in pixels. The height is computed
        automatically from the geometry's bounding box aspect ratio. Either width
        or resolution should be provided.
    resolution : float
        The data resolution in arc-seconds. The width and height are computed in pixel
        based on the geometry bounds and the given resolution. Either width or
        resolution should be provided.
    fill_holes : bool, optional
        Whether to fill the holes in the geometry's interior, defaults to False.
    in_crs : string, optional
        The spatial reference system of the input geometry, defaults to
        epsg:4326.
    out_crs : string, optional
        The spatial reference system to be used for requesting the data, defaults to
        epsg:4326.
    fpath : string or Path
        Path to save the output as a ``tiff`` file, defaults to None.

    Returns
    -------
    xarray.DataArray
        DEM in meters.
    """
    url = "https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WMSServer"

    layers = {"elevation": "3DEPElevation:None"}
    if fpath is not None:
        fpath = {"elevation": fpath}

    dem = services.wms_bygeom(
        url,
        "DEM",
        geometry,
        width=width,
        resolution=resolution,
        layers=layers,
        outFormat="image/tiff",
        fill_holes=fill_holes,
        fpath=fpath,
        in_crs=in_crs,
        out_crs=out_crs,
    )
    dem.attrs["units"] = "meters"
    return dem
