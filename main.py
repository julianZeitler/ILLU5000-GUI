# Standard library imports
import numpy as np

# Third party imports
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Local application imports
from cl_zoom import AutoYrange
from cl_data import Data
from cl_load import LoadMat    # custom load function


# load matlab data file
read_data = LoadMat('data.mat')
data = read_data.loadmat()

# initialize data object from dict
t_incremental = Data(**data['t_incremental'])
raw_x1 = Data(**data['raw_x1'])
raw_x2 = Data(**data['raw_x2'])

# axesSubplot objects
ax = []
# line objects for every plot (nD List for n plots on subplot)
line = []

gs = GridSpec(1, 1)

fig1 = plt.figure(1)

ax.append(fig1.add_subplot(gs[0, 0]))
line.append(ax[0].plot(t_incremental.values, raw_x1.values))


fig2 = plt.figure(2)
ax.append(fig2.add_subplot(gs[0, 0], sharex=ax[0]))
line.append(ax[1].plot(t_incremental.values, raw_x2.values))


# create callback for every plot
for i in range(len(ax)):
    AutoYrange(ax[i], line[i])


plt.show()
