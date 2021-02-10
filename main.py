import numpy as np

import matplotlib.pyplot as plt

from cl_zoom import AutoYrange
from cl_data import Data
from func_load import LoadMat    # custom load function
from cl_plot import Plot


# load matlab data file
read_data = LoadMat('data.mat')
data = read_data.loadmat()

# initialize data object from dict
t_incremental = Data(**data['t_incremental'])
raw_x1 = Data(**data['raw_x1'])
raw_x2 = Data(**data['raw_x2'])
raw_x3 = Data(**data['raw_x3'])

fig1 = Plot(1, 1, subtitle='Figure 1')
fig1.subplot(t_incremental.values, raw_x1.values, n=(0, 0))

fig2 = Plot(1, 2, subtitle='Figure 2')
fig2.subplot(t_incremental.values, raw_x2.values, n=(0, 0))
fig2.subplot(t_incremental.values, raw_x3.values, n=(0, 1))

plt.show()
