from matplotlib.pyplot import subplots
from numpy import ndarray
from dataclasses import dataclass

from analyzer.functions.func_mat import load, save
from analyzer.data.cl_data import FileData
from analyzer.plot.cl_zoom import Zoom


class Plot:
    """
    Plot is responsible for building the plot from the data inside of a FileData object.
    Therefore it receives the arguments data and key upon instantiation. Data can either be the name of a .mat file
    or an already created instance of FileData. Key is the name of the plot that should be plotted.
    The created axes objects can be accessed via plot.figure[..].subplot[...]
    """
    def __init__(self, data, key):
        if type(data) == str:
            self.read_data = load(data)
            file_data = FileData(**self.read_data)
        elif type(data) == object:
            file_data = data
        else:
            raise TypeError('data was not of type string or object')

        self.data = file_data.plot_data.data      # dictionary
        self.plot = file_data.plot_data.plot    # dictionary
        self.meta = file_data.plot_data.meta      # object

        # create list of figures, which can be accessed via
        # self.figure[i].subplot[i]
        self.figure = [self.Subplot(self._create_figures(fig, self.data)) for fig in self.plot[key].figure]

        # self.ax_list contains the ax objects for every subplot that is linked
        self.ax_list = [self.figure[link[0]].subplot[link[1]] for link in self.plot[key].linkaxes]

        self._linkaxes()
        self._auto_zoom()

    def _linkaxes(self):
        # links all axes in ax_list
        self.ax_list[0].get_shared_x_axes().join(*self.ax_list)

    def _auto_zoom(self):
        for ax in self.ax_list:
            Zoom(ax)

    @staticmethod
    def _create_figures(fig_config, data):
        """
        _create_figures is a private method, which -as the name suggests- creates the figure instances.
        :param fig_config: figure configuration stored in file_data.plot_data.plot[...].figure[...]
        :param data: the actual plotting data
        :return: a list of axes objects
        """
        fig, axs = subplots(ncols=fig_config.subplot_cols,
                            nrows=fig_config.subplot_rows,
                            constrained_layout=fig_config.constrained_layout)

        # convert multi-dim numpy array to single-dim python list
        if not isinstance(axs, ndarray):
            axs = [axs]
        elif axs.ndim == 1:
            axs = list(axs)
        elif axs.ndim == 2:
            axs = [ax for dim in axs for ax in dim]

        for ax in axs:
            fig_config.subplot[axs.index(ax)].plot(ax, data)

        return axs

    @dataclass
    class Subplot:
        subplot: list
