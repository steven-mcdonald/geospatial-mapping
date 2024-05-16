import osmnx as ox
from shapely.geometry import MultiPolygon, Polygon
import rasterio.mask
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, BoundaryNorm
from matplotlib import cm
import pyproj
from pyproj import CRS
import rioxarray as rxr
from rasterio.crs import CRS

org_surface_timp_file = rasterio.open('../resources/MOD_LSTD_M_2021-01-01_rgb_3600x1800.TIFF')
org_surface_temp = org_surface_timp_file.read()

surface_temp_file = rxr.open_rasterio('../resources/MOD_LSTD_M_2021-01-01_rgb_3600x1800.TIFF', masked=True).squeeze()

city = 'London'
# country = 'UK'
# country = 'United Kingdom'
# country = 'Singapore'
# country = 'Norway'
# country = 'France'
country = 'Metropolitan France'

admin = ox.geocode_to_gdf(country)
# admin.plot()
# minx, miny, maxx, maxy = admin.to_crs(crs=4326).bounds.T[0]
xmin, ymin, xmax, ymax = admin.to_crs(crs=4326).bounds.T[0]
# bbox = ','.join([str(miny), str(minx), str(maxy), str(maxx)])
bbox = MultiPolygon([Polygon([[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]])])

# note you need
with rasterio.open("../resources/MOD_LSTD_M_2021-01-01_rgb_3600x1800.TIFF") as src:
    data, _ = rasterio.mask.mask(src, shapes=bbox.geoms, crop=True)

fig = plt.figure(facecolor='#FCF6F5FF', figsize=(14, 7))
# Plot the raster data using matplotlib
# ax = fig.add_axes([0, 0, 1, 1])
ax = plt.axes()
raster_image = ax.imshow(data[0, :, :], cmap="Reds", interpolation='nearest')

# fig.colorbar(raster_image, ax=ax,label="Elevation (in m) ",orientation='vertical',extend='both',shrink=0.5)
plt.show()

print()

