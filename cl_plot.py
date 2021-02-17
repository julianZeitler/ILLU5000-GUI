import matplotlib.pyplot as plt

from func_mat import load, save
from cl_data import Top
from func_import import dyn_import_obj


class Plot:
    def __init__(self, file):
        self.read_data = load(file)
        top = Top(**self.read_data)
        dic = save(top, 'PlotData', file='save.mat')
        print(dic)

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object
        self.plot_type = top.plot_data.plot['raw'].figure[0].subplot[0].plot_type

        for key, val in self.plot.items():
            self.create_figures(key, val)

    def create_figures(self, name, fig):
        pass

    def create_subplots(self, fig):
        obj = dyn_import_obj('plt_' + self.plot_type, self.plot_type)

