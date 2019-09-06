import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize = (16, 9), edgecolor = 'w')
ax = fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(projection = 'cyl', resolution = None, llcrnrlat = -90, urcrnrlat=90, llcrnrlon = -180, urcrnrlon=180)
m.etopo()

fig.savefig("worldtopo", bbox_inches='tight')
