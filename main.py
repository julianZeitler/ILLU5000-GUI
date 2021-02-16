#! /usr/bin/python3
from sys import argv

from cl_data import Top
from cl_plot import Plot
from func_load import loadmat   # custom load function
from func_save import save


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
data = loadmat('data.mat')
try:
    conf = loadmat(conf_file)
except: pass

# initialize data object from dict
top = Top(**data)

print(top.plot_data.data['raw_force'].name)
print(top.plot_data.meta.worker)
print(top.plot_data.plot['raw'].figure[0].title)
print(top.plot_data.plot['raw'].figure[1].title)
print(top.plot_data.plot['raw'].figure[0].subplot[0].plot_type)
print(top.plot_data.plot['raw'].figure[0].subplot[0].x_label)
print(top.plot_data.plot['frequency'].figure[0].subplot[0].x_label)

saved_data = save(top, 'PlotData')
top2 = Top(**saved_data)

print(top2.plot_data.plot['raw'].figure[0].title)
print(top2.plot_data.plot['frequency'].figure[0].subplot[0].x_label)
