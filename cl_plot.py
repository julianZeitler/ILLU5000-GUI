from matplotlib.pyplot import subplots

from func_mat import load, save
from cl_data import Top
from cl_zoom import AutoYrange


class Plot:
    def __init__(self, data, key):
        if type(data) == str:
            self.read_data = load(data)
            top = Top(**self.read_data)
        elif type(data) == object:
            top = data
        else:
            raise TypeError('data was not of type string nor object')

        self.data = top.plot_data.data      # dictionary
        self.plot = top.plot_data.plot    # dictionary
        self.meta = top.plot_data.meta      # object

        # self.axes is a 2D list with the first dimension as the figures and the second as axes objects
        self.axes = [self._create_figures(fig, self.data) for fig in self.plot[key].figure]

        # self.ax_list contains the ax objects for every subplot that is linked
        self.ax_list = [self.axes[link[0]][link[1]] for link in self.plot[key].linkaxes]

        self._linkaxes()
        self._auto_zoom()

    def _linkaxes(self):
        # links all axes in ax_list
        self.ax_list[0].get_shared_x_axes().join(*self.ax_list)

    def _auto_zoom(self):
        for ax in self.ax_list:
            AutoYrange(ax)

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
