import osmnx as ox
import rasterio
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, BoundaryNorm
from matplotlib import cm
from matplotlib import colors
from datetime import datetime
import imageio

import pyproj
from pyproj import CRS
import rioxarray as rxr
from rasterio.crs import CRS


if __name__ == "__main__":

    png_save_path = '../plots'
    gif_save_path = '../gifs'

    file_list = [
        'MOD_LSTD_M_2020-05-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-06-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-07-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-08-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-09-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-10-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-11-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2020-12-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-01-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-02-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-03-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-04-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-05-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-06-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-07-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-08-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-09-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-10-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-11-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2021-12-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-01-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-02-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-03-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-04-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-05-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-06-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-07-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-08-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-09-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-10-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-11-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2022-12-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-01-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-02-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-03-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-04-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-05-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-06-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-07-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-08-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-09-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-10-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-11-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2023-12-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2024-01-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2024-02-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2024-03-01_rgb_3600x1800.TIFF',
        'MOD_LSTD_M_2024-04-01_rgb_3600x1800.TIFF'
    ]

    for file in file_list:
        surface_temp_file = rxr.open_rasterio(f'../resources/{file}', masked=True).squeeze()
        # extract the date from the filename
        date_string = file.split('_rgb')[0].split('_M_')[1]
        # convert to datetime format
        date_datetime = datetime.strptime(date_string, '%Y-%m-%d')
        # re-convert to more readable string
        date_string_text = date_datetime.strftime('%Y %B')

        # # convert main image array to numpy
        # surface_temp = surface_temp_file.to_numpy()

        # remap to robinson projection
        print("Original projection: ", surface_temp_file.rio.crs)
        crs_rob = CRS.from_string('+proj=robin')
        surface_temp = surface_temp_file.rio.reproject(crs_rob)
        print("New projection: ", surface_temp.rio.crs)
        surface_temp = surface_temp.to_numpy()

        # sea values are initially set at 255 - reset to 0 for display
        surface_temp[surface_temp == 255] = 0

        # extract rgb colour values from matplotlib named colour for background
        background_colour_name = 'lightgray'
        background_colour_rgb = colors.to_rgba(background_colour_name)

        # check palette and update background
        reds = cm.get_cmap('Reds', 254)
        newcolors = reds(np.linspace(0, 1, 254))
        newcolors[:1, :] = background_colour_rgb
        # newcolors[-1:, :] = np.array([0.0, 0.9647058823529412, 0.0, 1.0])
        newcmp_surf_temp = ListedColormap(newcolors)

        fig = plt.figure(facecolor='#FCF6F5FF', figsize=(14, 7))
        ax = plt.axes()
        # fig.set_size_inches(7, 3.5)
        ax.patch.set_facecolor('#FCF6F5FF')
        ax.imshow(surface_temp, cmap=newcmp_surf_temp, interpolation='nearest')
        # adding text inside the plot
        plt.text(2400, 2300, date_string_text, fontsize=18, color='dimgray')
        ax.axis('off')
        savename = f'surface_temp_{date_string}.png'
        plt.savefig(os.path.join(png_save_path, savename))
        plt.show()

        print()

    input_filenames = [f for f in os.listdir(png_save_path) if os.path.isfile(os.path.join(png_save_path, f))]
    input_filenames = sorted(input_filenames)

    images = []
    for filename in input_filenames:
        print(filename)
        images.append(imageio.v2.imread(os.path.join(png_save_path, filename)))
    imageio.mimsave(os.path.join(gif_save_path, 'surface_temp.gif'), images, fps=4)

    print()
