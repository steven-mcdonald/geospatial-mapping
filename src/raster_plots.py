import rasterio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, BoundaryNorm
from matplotlib import cm

forests_file = rasterio.open('../resources/gm_ve_v1.tif')
forests = forests_file.read()

# print(np.amin(forests))
# print(np.amax(forests))
# print(len(np.unique(forests)))

# # raw plot shows oceans in green due to none forest areas being given the highest colour value of 254
# fig = plt.figure(facecolor='#FCF6F5FF')
# ax = plt.axes()
# fig.set_size_inches(7, 3.5)
# ax.patch.set_facecolor('#FCF6F5FF')
# ax.imshow(forests[0],cmap='Greens',interpolation='nearest')
# ax.axis('off')
# plt.show()

# # check pallete
# purples = cm.get_cmap('Greens', 254)
# newcolors = purples(np.linspace(0, 1, 254))
# background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
# newcolors[:1, :] = background_colour
# newcmp_forests = ListedColormap(newcolors)
#
# bounds = np.arange(254)
# norm_forests = BoundaryNorm(bounds, newcmp_forests.N)
#
# gradient = np.linspace(0, 1, 254)
# gradient = np.vstack((gradient, gradient))
# fig, ax = plt.subplots()
# ax.imshow(gradient, aspect='auto', cmap=newcmp_forests)
# ax.get_yaxis().set_visible(False)
# ax.axvline(100, ls="--", c='black', )
# plt.text(105, 0.7, "Data Ends", rotation=90)
#
# plt.show()

# if we reset the 254 values to zero then matplotlib will map the data properly with no forest = white
forests[0][forests[0] == 254] = 0.0

ourcmap = cm.get_cmap('Greens', 101)
newcolors = ourcmap(np.linspace(0, 1, 101))
background_colour = np.array([0.9882352941176471, 0.9647058823529412, 0.9607843137254902, 1.0])
newcolors[:1, :] = background_colour
newcmp_forests = ListedColormap(newcolors)
fig = plt.figure(facecolor='#FCF6F5FF', figsize=(14, 7))
ax = plt.axes()
# fig.set_size_inches(7, 3.5)
ax.patch.set_facecolor('#FCF6F5FF')
ax.imshow(forests[0], cmap=newcmp_forests, interpolation='nearest')
ax.axis('off')
plt.savefig('../plots/forests_new_cmap_2.png')
plt.show()

print()
