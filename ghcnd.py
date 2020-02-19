import pandas as pd

def process
def process_stations_txt(filepath):
    '''
    Processes file containing all ghcnd station meta data available at:
        ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

    Additional reference: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
    :param filepath:
    :return:
    '''

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

    return df

