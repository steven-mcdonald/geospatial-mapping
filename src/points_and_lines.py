import pandas as pd
import os
from shapely.geometry import Point
from shapely.geometry import LineString

import geopandas as gpd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# # POINTS
#
# ports = pd.read_csv("../resources/ports/ports.csv")
# savepath = '../plots/ports'
# savename= 'ports.png'
#
# port_geometry = [Point(xy) for xy in zip(ports['lon'], ports['lat'])]
# port_geodata = gpd.GeoDataFrame(ports, crs="EPSG:4326", geometry=port_geometry)
#
#
# fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Robinson()},
#                        figsize=(14, 7), facecolor='lightcyan')
# port_geodata.plot(ax=ax, transform=ccrs.PlateCarree(), color='steelblue', markersize=1, alpha=0.5)
# ax.set_facecolor('lightcyan')
# ax.set_axis_off()
# plt.text(0.5, 0.2, 'Global Ports', fontsize=18, color='steelblue',
#          horizontalalignment='center',
#          verticalalignment='center',
#          transform=ax.transAxes
#          )
# plt.tight_layout()
# plt.savefig(os.path.join(savepath, savename))
# plt.show()

# LINES

# to do: pick out routes I have flown and plot them in a different colour

savepath = '../plots/air'
savename= 'air.png'

airports = pd.read_csv("../resources/air/airports.csv", delimiter=',', names=['id', 'name', 'city', 'country', 'iata',
                                                                   'icao', 'lat', 'long', 'altitude', 'timezone',
                                                                   'dst', 'tz', 'type', 'source'])

routes = pd.read_csv("../resources/air/routes.csv", delimiter=',', names=['airline', 'id', 'source_airport', 'source_airport_id',
                                                               'destination_airport', 'destination_airport_id', 'codeshare',
                                                               'stops', 'equitment'])

source_airports = airports[['name', 'iata', 'icao', 'lat', 'long']]
destination_airports = source_airports.copy()
source_airports.columns = [str(col) + '_source' for col in source_airports.columns]
destination_airports.columns = [str(col) + '_destination' for col in destination_airports.columns]

routes = routes[['source_airport', 'destination_airport']]
routes = pd.merge(routes, source_airports, left_on='source_airport', right_on='iata_source')
routes = pd.merge(routes, destination_airports, left_on='destination_airport', right_on='iata_destination')

print(routes.columns)

routes_geometry = [LineString([[routes.iloc[i]['long_source'], routes.iloc[i]['lat_source']], [routes.iloc[i]['long_destination'], routes.iloc[i]['lat_destination']]]) for i in range(routes.shape[0])]
routes_geodata = gpd.GeoDataFrame(routes, geometry=routes_geometry, crs='EPSG:4326')

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Robinson()},
                       figsize=(14, 7), facecolor='black')
ax.set_facecolor('black')
routes_geodata.plot(ax=ax, transform=ccrs.Geodetic(), color='white', linewidth=0.1, alpha=0.1)
ax.set_axis_off()
plt.text(0.5, 0.1, 'Global Flight Routes', fontsize=18, color='white', alpha=0.7,
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes,
         )
plt.tight_layout()
plt.savefig(os.path.join(savepath, savename))
plt.show()

print()
