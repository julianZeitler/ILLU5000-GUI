import matplotlib.pyplot as plt

from func_load import loadmat
from cl_data import Top


class Plot:
    def __init__(self, file):
        self.read_data = loadmat(file)
        top = Top(**self.read_data)
        print(top.plot_data.plot['raw'].figure[0].subplot[0].x_label)

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object
        self.plot_type = top.plot_data.plot['raw'].figure[0].subplot[0].plot_type

        for key, val in self.plot.items():
            self.create_figures(key, val)

    def create_figures(self, name, fig):
        pass

    def create_subplots(self, fig):
        obj = self.dyn_import('plt_' + self.plot_type, self.plot_type)

    @staticmethod
    def dyn_import(module_name, class_name, *args, **kwargs):
        module = __import__(module_name)
        my_class = getattr(module, class_name)
        obj = my_class(*args, **kwargs)
        return obj
