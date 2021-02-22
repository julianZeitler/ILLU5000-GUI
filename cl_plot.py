from numpy import ndarray, asarray, empty

from matplotlib.pyplot import subplots
from matplotlib.gridspec import GridSpec
from matplotlib.pyplot import figure

from func_mat import load
from cl_data import Top


class Plot:
    def __init__(self, file, key):
        self.read_data = load(file)
        top = Top(**self.read_data)

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object

        self.axes = empty(len(self.plot[key].figure), dtype=object)
        cnt = 0
        for fig in self.plot[key].figure:
            self.axes[cnt] = self.create_figures(fig, self.data)
            cnt += 1

    @staticmethod
    def create_figures(fig_config, data):
        fig = figure(constrained_layout=fig_config.constrained_layout)
        gs = GridSpec(fig_config.subplot_rows, fig_config.subplot_cols, figure=fig)

        axs = empty((fig_config.subplot_rows, fig_config.subplot_cols), dtype=object)

        for plot in fig_config.subplot:
            axs[plot.position[0], plot.position[1]] = fig.add_subplot(gs[plot.position[0], plot.position[1]])

        if not isinstance(axs, ndarray):
            axs = asarray([axs])

        if axs.ndim == 2:
            cnt = 0
            for i in range(len(axs)):
                for j in range(len(axs[i])):
                    fig_config.subplot[cnt].plot(axs[i, j], data)
                    cnt += 1
        else:
            for i in range(len(axs)):
                fig_config.subplot[i].plot(axs[i], data)

        return axs
