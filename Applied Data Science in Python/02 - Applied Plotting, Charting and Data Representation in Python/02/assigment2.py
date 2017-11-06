import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd


def leaflet_plot_stations(binsize, hashid):

    station_locations_by_hash = read_csv_stations(binsize, hashid)
    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8, 8))
    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()


def read_csv_stations(binsize, hashid):
    # df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))
    df = pd.read_csv('BinSize_d{}.csv'.format(binsize))
    # return df
    station_locations_by_hash = df[df['hash'] == hashid]
    return station_locations_by_hash


def get_cleaned_data():
    # df = pd.read_csv('data/C2A2_data/0a94e6b522c619cfe6c3c48e6fea6ff3c00c7109dc47ae70af4cd8c6.csv')
    df = pd.read_csv(
        '0a94e6b522c619cfe6c3c48e6fea6ff3c00c7109dc47ae70af4cd8c6.csv')
    return df


df = get_cleaned_data()
len(df)
