import numpy as np

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from cl_zoom import AutoYrange
from cl_data import Data
from cl_load import LoadMat    # custom load function
from cl_plot import Plot


# load matlab data file
read_data = LoadMat('data.mat')
data = read_data.loadmat()

# initialize data object from dict
t_incremental = Data(**data['t_incremental'])
raw_x1 = Data(**data['raw_x1'])
raw_x2 = Data(**data['raw_x2'])
raw_x3 = Data(**data['raw_x3'])

fig1 = Plot(1, 1, suptitle='Figure 1')
fig1.subplot(0, t_incremental, raw_x1, name=(raw_x1.name), title=raw_x1.name)

plt.show()
