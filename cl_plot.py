from matplotlib.pyplot import subplots

from func_mat import load
from cl_data import Top
from cl_zoom import AutoYrange


class Plot:
    def __init__(self, file, key):
        self.read_data = load(file)
        top = Top(**self.read_data)

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object

        # self.axes is a 2D list with the first dimension as the figures and the second as axes objects
        self.axes = [self._create_figures(fig, self.data) for fig in self.plot[key].figure]

        self._linkaxes(self.plot[key].linkaxes, self.axes)

        for fig in self.axes:
            for ax in fig:
                AutoYrange(ax)

    @staticmethod
    def _linkaxes(link_list, all_ax_list):
        # create list with the axis objects which should be connected
        ax_list = [all_ax_list[link[0]][link[1]] for link in link_list]

        # links all axes in ax_list
        ax_list[0].get_shared_x_axes().join(*ax_list)

    @staticmethod
    def _create_figures(fig_config, data):
        fig, axs = subplots(ncols=fig_config.subplot_cols,
                            nrows=fig_config.subplot_rows,
                            constrained_layout=fig_config.constrained_layout)

        # convert multi-dim numpy array to single-dim python list
        if axs.ndim == 1:
            axs = list(axs)
        elif axs.ndim == 2:
            axs = [ax for dim in axs for ax in dim]

        for ax in axs:
            fig_config.subplot[axs.index(ax)].plot(ax, data)

        return axs
