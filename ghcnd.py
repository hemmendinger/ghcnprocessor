import pandas as pd

resources = {
    'countries':'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-countries.txt',
    'states':'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-states.txt',
    'inventory':'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt',
    'stations':'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stationst.txt'
}

def process_countries_txt(filepath):
    """
    Process ghcnd-countries.txt

    Resource locations:
      ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-countries.txt
      https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-countries.txt

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
    Resource locations:
      ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-states.txt
      https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-states.txt

    :param filepath:
    :return:
    """
    return process_countries_txt(filepath)


def process_inventory_txt(filepath):
    """
    Process ghcnd-inventory.txt: "File listing the periods of record for each station and element"

    Resource locations:
      ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt
      https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt
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
    Processes file containing all ghcnd station meta data.

    Resource locations:
      ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
      https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stationst.txt

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

def process_stations_id(id):
    """
    First 2 characters are a FIPS country code
    Third character is a "network code" identifying the station numbering system used
    Last 8 characters are the actual station ID
    :param id: str
    :return:
    """
    pass

def process_dly(filepath):
    """Each dly file contains all data for one station.
    Each row is one month of data for one element.

    :param filepath:
    :return:
    """
    pass


def read_dly(filepath):
    """

    :param filepath:
    :return:
    """
    names = [
        'id',
        'year',
        'month',
        'element',
        # Plus more names generated:
        # value1, mflag1, qflag1, sflag1, ... , value31, mflag31, qflag31, sflag31
    ]

    name_stems = [
        'value',
        'mflag',
        'qflag',
        'sflag',
    ]

    for n in range(1,32):
        for stem in name_stems:
            names.append(stem+str(n))

    widths = [
        (0, 11),  # id
        (11, 15),  # year
        (15, 17),  # month
        (17, 21),  # element
        # Plus widths generated for the 1-31 possible days per month
    ]

    start_widths = [
        (21, 26),
        (26, 27),
        (27, 28),
        (28, 29),
    ]

    for n in range(0, 31):
        char_gap = 8
        for w in start_widths:
            lower = w[0] + (char_gap * n)
            upper = w[1] + (char_gap * n)
            widths.append((lower, upper))

    df = pd.read_fwf(colspecs=widths, names=names, filepath_or_buffer=filepath)

    return df
