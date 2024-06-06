# data from https://openflights.org/data

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



savepath = '../plots/air'
savename= 'air_sel.png'

airports = pd.read_csv("../resources/air/airports.csv", delimiter=',', names=['id', 'name', 'city', 'country', 'iata',
                                                                   'icao', 'lat', 'long', 'altitude', 'timezone',
                                                                   'dst', 'tz', 'type', 'source'])

routes = pd.read_csv("../resources/air/routes.csv", delimiter=',', names=['airline', 'id', 'source_airport', 'source_airport_id',
                                                               'destination_airport', 'destination_airport_id', 'codeshare',
                                                               'stops', 'equitment'])

response = list_airports(airports, country='United Kingdom', city=None)

source_airports = airports[['name', 'iata', 'icao', 'lat', 'long']]
destination_airports = source_airports.copy()
source_airports.columns = [str(col) + '_source' for col in source_airports.columns]
destination_airports.columns = [str(col) + '_destination' for col in destination_airports.columns]

routes = routes[['source_airport', 'destination_airport']]
routes = pd.merge(routes, source_airports, left_on='source_airport', right_on='iata_source')
routes = pd.merge(routes, destination_airports, left_on='destination_airport', right_on='iata_destination')

# there are multiple 'identical' routes between 2 airports - select only first each time
routes_unique = routes.groupby(['source_airport', 'destination_airport']).first().reset_index()

# Opening JSON file with selected routes as dictionary
with open("../resources/air/selected_routes.json") as json_file:
    selected_routes_dict = json.load(json_file)

# select unique routes information from my selected routes data and create gdf
gdf_list = []
for source_airport in ['London', 'Paris', 'Singapore']:
    sel_routes = routes_unique[routes_unique.set_index(['source_airport', 'destination_airport']).index.isin(selected_routes_dict[source_airport].values())]
    sel_routes_geometry = [LineString([[sel_routes.iloc[i]['long_source'], sel_routes.iloc[i]['lat_source']], [sel_routes.iloc[i]['long_destination'], sel_routes.iloc[i]['lat_destination']]]) for i in range(sel_routes.shape[0])]
    sel_routes_geodata = gpd.GeoDataFrame(sel_routes, geometry=sel_routes_geometry, crs='EPSG:4326')
    gdf_list.append(sel_routes_geodata)

# create gdf for all unique routes
routes_geometry = [LineString([[routes.iloc[i]['long_source'], routes.iloc[i]['lat_source']], [routes.iloc[i]['long_destination'], routes.iloc[i]['lat_destination']]]) for i in range(routes.shape[0])]
routes_geodata = gpd.GeoDataFrame(routes, geometry=routes_geometry, crs='EPSG:4326')

# plot the map
route_colour_list = ['red', 'orange', 'gold']
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Robinson()},
                       figsize=(14, 7), facecolor='black')
ax.set_facecolor('black')
# plot the routes
routes_geodata.plot(ax=ax, transform=ccrs.Geodetic(), color='white', linewidth=0.1, alpha=0.1)
for i in range(len(gdf_list)):
    gdf_list[i].plot(ax=ax, transform=ccrs.Geodetic(), color=route_colour_list[i], linewidth=1.0, alpha=0.6)

# add some text
plt.text(0.5, 0.1, 'Global Flight Routes', fontsize=18, color='white', alpha=0.7,
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes,
         )
plt.text(0.40, 0.02, 'London', fontsize=14, color='red', alpha=0.6,
         horizontalalignment='right',
         verticalalignment='center',
         transform=ax.transAxes,
         )
plt.text(0.5, 0.02, 'Paris', fontsize=14, color='orange', alpha=0.6,
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes,
         )
plt.text(0.60, 0.02, 'Singapore', fontsize=14, color='gold', alpha=0.6,
         horizontalalignment='left',
         verticalalignment='center',
         transform=ax.transAxes,
         )
ax.set_axis_off()
plt.tight_layout()
plt.savefig(os.path.join(savepath, savename))
plt.show()

print()
