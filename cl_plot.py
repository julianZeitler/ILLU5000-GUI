import matplotlib.pyplot as plt
from numpy import ndarray, asarray

from func_mat import load, save
from cl_data import Top
from func_import import dyn_import_obj


class Plot:
    def __init__(self, file, key):
        self.read_data = load(file)
        top = Top(**self.read_data)

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object

        for fig in self.plot[key].figure:
            self.create_figures(fig, self.data)

    @staticmethod
    def create_figures(figure, data):
        fig, axs = plt.subplots(figure.subplot_rows,
                                figure.subplot_cols,
                                constrained_layout=figure.constrained_layout)
        if not isinstance(axs, ndarray):
            axs = asarray([axs])

        for i in range(len(figure.subplot)):
            #for plot in figure.subplot[i].plots:
            figure.subplot[i].plot(axs[i], data)
