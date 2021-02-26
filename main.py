#! /usr/bin/python3
from sys import argv
import matplotlib.pyplot as plt

from cl_plot import Plot
from data import data_mat

# argpass
# get arguments
# args[0] is the file itself
# args = argv

'''
# argument handling
if len(args) <= 1:
    raise AttributeError(f'Please specify *.mat plot file')
if len(args) == 2:
    file = args[1]
elif len(args) >= 3:
    file = args[1]
    conf_file = args[2:]
'''
data_mat()

plot = Plot('data.mat', 'raw')

plt.show()
