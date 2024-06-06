# Generate Various Geospatial plots
---

## Generating a Monthly Global Land Temperature Map Gif
 
This project gathers global land temperature data and generates a gif to shows its month-to-month variation over 4 years from May 2020 to April 2024.

![land temp gif](https://github.com/steven-mcdonald/geospatial-mapping/blob/master/gifs/surf_temp/surface_temp.gif "land temp gif")

### Data Source
Monthly Global Land Temperature data can be imported from the Nasa Earth Observations data portal at
[NEO Nasa Earth Observations](https://neo.gsfc.nasa.gov). Data was imported as a list of GeoTiff raster files of shape 3600x1800 with 0.1 degrees temperature resolution.

### Data Manipulation
The original data was reprojected to the Robinson projection. The colour map was changed to Matplotlib 'Reds' with the sea colour reset to gray.
