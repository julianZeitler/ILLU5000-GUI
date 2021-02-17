#! /usr/bin/python3
from sys import argv

from cl_data import Top
from cl_plot import Plot
from func_mat import load, save  # custom load function


# get arguments
# args[0] is the file itself
args = argv

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

# load matlab data file
#data = loadmat(file)
data = load('data.mat')
try:
    conf = load(conf_file)
except: pass

plot = Plot('data.mat')
