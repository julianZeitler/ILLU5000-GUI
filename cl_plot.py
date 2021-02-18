from numpy import ndarray, asarray

from matplotlib.pyplot import subplots

from func_mat import load
from cl_data import Top


class Plot:
    def __init__(self, file, key):
        self.read_data = load(file)
        top = Top(**self.read_data)

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object

        self.axes = []
        for fig in self.plot[key].figure:
            self.axes += list(self.create_figures(fig, self.data))

    @staticmethod
    def create_figures(figure, data):
        fig, axs = subplots(figure.subplot_rows,
                            figure.subplot_cols,
                            constrained_layout=figure.constrained_layout)

        if not isinstance(axs, ndarray):
            axs = asarray([axs])

        if axs.ndim == 2:
            cnt = 0
            for i in range(len(axs)):
                for j in range(len(axs[i])):
                    figure.subplot[cnt].plot(axs[i, j], data)
                    cnt += 1
        else:
            for i in range(len(axs)):
                figure.subplot[i].plot(axs[i], data)

        return axs
