import pandas as pd
import json
import os
from shapely.geometry import Point
from shapely.geometry import LineString

import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def list_airports(df, country='United Kingdom', city=None, code_type='iata'):
    df_sel = df[df['country'] == country]
    if city:
        df_sel = df_sel[df['city'] == city]
    airport_code_list = df_sel[code_type].to_list()
    return airport_code_list

# POINTS

ports = pd.read_csv("../resources/ports/ports.csv")
savepath = '../plots/ports'
savename= 'ports.png'

port_geometry = [Point(xy) for xy in zip(ports['lon'], ports['lat'])]
port_geodata = gpd.GeoDataFrame(ports, crs="EPSG:4326", geometry=port_geometry)


fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Robinson()},
                       figsize=(14, 7), facecolor='lightcyan')
port_geodata.plot(ax=ax, transform=ccrs.PlateCarree(), color='steelblue', markersize=1, alpha=0.5)
ax.set_facecolor('lightcyan')
ax.set_axis_off()
plt.text(0.5, 0.2, 'Global Ports', fontsize=18, color='steelblue',
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes
         )
plt.tight_layout()
plt.savefig(os.path.join(savepath, savename))
plt.show()