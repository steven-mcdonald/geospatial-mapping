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


def create_map_plot(img_array, cmap, savepath, savename, text=None, text_loc=(0, 0),
                    show_plot=False):
    fig = plt.figure(facecolor='#FCF6F5FF', figsize=(14, 7))
    ax = plt.axes()
    ax.patch.set_facecolor('#FCF6F5FF')
    ax.imshow(img_array, cmap=cmap, interpolation='nearest')
    # adding text inside the plot
    plt.text(text_loc[0], text_loc[1], text, fontsize=18, color='dimgray')
    ax.axis('off')
    plt.savefig(os.path.join(savepath, savename))
    if show_plot:
        plt.show()


def create_gif_from_png_list(input_filenames, savepath, savename, fps=4):
    images = []
    for filename in input_filenames:
        print(filename)
        images.append(imageio.v2.imread(os.path.join(png_save_path, filename)))
    imageio.mimsave(os.path.join(savepath, savename), images, fps=fps)


if __name__ == "__main__":

    tiff_input_path = '../resources/surf_temp'
    png_save_path = '../plots/surf_temp'
    gif_save_path = '../gifs/surf_temp'

    tiff_filelist = [f for f in os.listdir(tiff_input_path) if os.path.isfile(os.path.join(tiff_input_path, f))]
    tiff_filelist = sorted(tiff_filelist)

    for file in tiff_filelist:
        # surface_temp_file = rxr.open_rasterio(f'../resources/{file}', masked=True).squeeze()
        surface_temp_file = rxr.open_rasterio(os.path.join(tiff_input_path, file), masked=True).squeeze()
        # extract the date from the filename
        date_string = file.split('_rgb')[0].split('_M_')[1]
        # convert to datetime format
        date_datetime = datetime.strptime(date_string, '%Y-%m-%d')
        # re-convert to more readable string
        date_string_text = date_datetime.strftime('%Y %B')

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

        create_map_plot(surface_temp, cmap=newcmp_surf_temp,
                        savepath=png_save_path, savename=f'surface_temp_{date_string}.png',
                        text=date_string_text, text_loc=(2400, 2300))

        print()

    input_filenames = [f for f in os.listdir(png_save_path) if os.path.isfile(os.path.join(png_save_path, f))]
    input_filenames = sorted(input_filenames)

    create_gif_from_png_list(input_filenames, savepath=gif_save_path, savename='surface_temp.gif',
                             fps=4)

    print()
