import pandas as pd


def process_countries_txt(filepath):
    """
    Process ghcnd-countries.txt

    Resource: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-countries.txt

    :param filepath:
    :return: pandas.DataFrame
    """
    names = [
        'code',
        'name',
    ]

    widths = [
        (0,2),  # country code
        (3,50),  # country name
    ]

    df = pd.read_fwf(colspecs=widths, names=names, filepath_or_buffer=filepath)

    return df


def process_states_txt(filepath):
    """
    Format is the same as ghcnd-countries.txt
    Resource: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-states.txt

    :param filepath:
    :return:
    """
    return process_countries_txt(filepath)


def process_inventory_txt(filepath):
    """
    Process ghcnd-inventory.txt: "File listing the periods of record for each station and element"
    :param filepath:
    :return: pandas.DataFrame
    """
    names = [
        'id',
        'latitude',
        'longitude',
        'element',
        'firstyear',
        'lastyear',
    ]

    widths = [
        (0, 11),  # id
        (12, 20),  # latitude
        (21, 30),  # longitude
        (31, 35),  # element
        (36, 40),  # firstyear
        (41, 45),  # lastyear
    ]

    df = pd.read_fwf(colspecs=widths, names=names, filepath_or_buffer=filepath)

    return df


def process_stations_txt(filepath):
    """
    Processes file containing all ghcnd station meta data available at:
        ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

    Additional reference: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
    :param filepath:
    :return: pandas.DataFrame
    """
    names = [
        'id',
        'latitude',
        'longitude',
        'elevation',
        'state',
        'name',
        'gsn_flag',
        'hcn_or_crn_flag',
        'wmo_id'
    ]

    widths = [
        (0, 12),  # ID
        (12, 21),  # LATITUDE
        (21, 31),  # LONGITUDE
        (31, 38),  # ELEVATION
        (38, 41),  # STATE
        (41, 72),  # NAME
        (72, 76),  # GSN FLAG
        (76, 80),  # HCN/CRN FLAG
        (80, 86),  # WMO ID
    ]

    df = pd.read_fwf(colspecs=widths, names=names, filepath_or_buffer=filepath)

    # TODO: Set dtypes

    return df

