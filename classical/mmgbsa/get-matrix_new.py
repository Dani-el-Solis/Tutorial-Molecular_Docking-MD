# coding: utf-8
import pickle
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.pyplot as plt
import pandas as pd
from math import floor
import sys


infile = sys.argv[1]
# Put xticks at the top of the figure
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.labeltop'] = True

# Remove ticks
plt.rcParams['xtick.top'] = False
plt.rcParams['ytick.left'] = False

# dpi
plt.rcParams["figure.dpi"] = 200

# Fonts
mpl.rcParams['font.family'] = ['serif']
mpl.rcParams['font.sans-serif'] = ['Helvetica']
#plt.rcParams["font.family"] = "sans-serif"
#plt.rcParams["font.sans-serif"] = "Helvetica"
fontsize = 12

try:
    get_ipython().run_line_magic("matplotlib","")
except:
    plt.ion()

names = ["vdw", "el", "pol", "np", "tot"]
xlabels = names
#xlabels = [r"$\Delta$G$_{%s}$"%i for i in names]
data = pd.read_csv(infile, names = names, delim_whitespace = True)
data.sort_values(by = "tot", inplace = True)
data = data.loc[data.index.values[:10]] # Only first 10 rows
min_data = np.min(data["tot"])
ylabels = data.index.values
ylabels_new = []
for i in range(len(ylabels)):
    temp =str(ylabels[i][0]) + str(ylabels[i][1]) 
    ylabels_new.append(temp)

fig, ax = plt.subplots()

# Generate listed (discrete) colormap
#cmap = ListedColormap([cm.Blues(i) for i in np.linspace(1,0,50)])
cmap = ListedColormap([cm.plasma(i) for i in np.linspace(0,1,50)])
#norm = BoundaryNorm(np.linspace(floor(min_data),0,50), cmap.N)
norm = BoundaryNorm(np.linspace(-10,0,11), cmap.N)
#myplot = ax.imshow(data_red, cmap = cm.Blues)
myplot = ax.imshow(data.values, cmap = cmap, norm = norm)
ax.set_xticks(np.arange(0,len(names)))
ax.set_yticks(np.arange(0,len(data.values)))
ax.set_xticklabels(xlabels, fontsize = 12)
ax.set_yticklabels(ylabels_new, fontsize = 12)

# Set grid
ax.set_xticks(np.arange(0.5,5.5), minor = True)
ax.set_yticks(np.arange(0.5,10.5), minor = True)
grid = ax.grid(which = "minor", axis = "both", linestyle = "-", color = "k", linewidth = 1)

#ax.set_xlabel("Selected MOs from the Sampled Geometry 29")
#ax.xaxis.set_label_position("top")
#ax.set_ylabel("Reference Active Space")

# Set colorbar
cb = fig.colorbar(myplot, orientation = "vertical")

# Set size
fig.set_size_inches(5, 6)
plt.show()
#plt.savefig('kk.png', transparent = True)
plt.savefig('decomp.png')
