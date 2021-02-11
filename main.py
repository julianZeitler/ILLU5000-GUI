#! /usr/bin/python3
import numpy as np
from sys import argv

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from cl_zoom import AutoYrange
from cl_data import Top
from func_load import loadmat # custom load function
from cl_plot import Plot


# get arguments
# args[0] is the file itself
args = argv
if len(args) > 2:
    raise AttributeError(f'Expected one argument, got {len(args)-1}')

# load matlab data file
data = loadmat(args[1])

# initialize data object from dict
top = Top(**data)


print(top.trace.data['raw_force'].name)
