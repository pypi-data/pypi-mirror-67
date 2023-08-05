#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some helper function for Hydrodata"""

import xml.etree.cElementTree as ET

import numpy as np
import pandas as pd
from hydrodata import utils


def nlcd_helper():
    """Helper for NLCD cover data

    Notes
    -----
    The following references have been used:
        * https://github.com/jzmiller1/nlcd
        * https://www.mrlc.gov/data-services-page
        * https://www.mrlc.gov/data/legends/national-land-cover-database-2016-nlcd2016-legend
    """
    url = "https://www.mrlc.gov/downloads/sciweb1/shared/mrlc/metadata/NLCD_2016_Land_Cover_Science_product_L48.xml"
    r = utils.get_url(utils.retry_requests(), url)

    root = ET.fromstring(r.content)

    colors = root[4][1][1].text.split("\n")[2:]
    colors = [i.split() for i in colors]
    colors = dict((int(c), (float(r), float(g), float(b))) for c, r, g, b in colors)

    classes = dict(
        (root[4][0][3][i][0][0].text, root[4][0][3][i][0][1].text.split("-")[0].strip())
        for i in range(3, len(root[4][0][3]))
    )

    nlcd_meta = dict(
        impervious_years=[2016, 2011, 2006, 2001],
        canopy_years=[2016, 2011],
        cover_years=[2016, 2013, 2011, 2008, 2006, 2004, 2001],
        classes=classes,
        categories={
            "Unclassified": ("0"),
            "Water": ("11", "12"),
            "Developed": ("21", "22", "23", "24"),
            "Barren": ("31",),
            "Forest": ("41", "42", "43", "45", "46"),
            "Shrubland": ("51", "52"),
            "Herbaceous": ("71", "72", "73", "74"),
            "Planted/Cultivated": ("81", "82"),
            "Wetlands": ("90", "95"),
        },
        roughness={
            "11": 0.001,
            "12": 0.022,
            "21": 0.0404,
            "22": 0.0678,
            "23": 0.0678,
            "24": 0.0404,
            "31": 0.0113,
            "41": 0.36,
            "42": 0.32,
            "43": 0.4,
            "45": 0.4,
            "46": 0.24,
            "51": 0.24,
            "52": 0.4,
            "71": 0.368,
            "72": np.nan,
            "81": 0.325,
            "82": 0.16,
            "90": 0.086,
            "95": 0.1825,
        },
        colors=colors,
    )

    return nlcd_meta


def nhdplus_fcodes():
    """Get NHDPlus FCode lookup table"""
    url = (
        "https://nhd.usgs.gov/userGuide/Robohelpfiles/NHD_User_Guide"
        + "/Feature_Catalog/Hydrography_Dataset/Complete_FCode_List.htm"
    )
    return (
        pd.concat(pd.read_html(url, header=0))
        .drop_duplicates("FCode")
        .set_index("FCode")
    )


def nwis_errors():
    """Get error code lookup table for USGS sites that have daily values"""
    return pd.read_html("https://waterservices.usgs.gov/rest/DV-Service.html")[0]


def hcdn_stations():
    """Get USGS Hydro-Climatic Data Network 2009 (HCDN-2009)"""
    hcdn = pd.read_excel(
        "https://water.usgs.gov/osw/hcdn-2009/HCDN-2009_Station_Info.xlsx"
    )
    return (
        hcdn["STATION ID"]
        .astype("str")
        .str.pad(width=8, side="left", fillchar="0")
        .tolist()
    )
