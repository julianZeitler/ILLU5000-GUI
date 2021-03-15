from matplotlib.pyplot import subplots
from numpy import ndarray
from dataclasses import dataclass

from DataAnalyzer.Functions.func_mat import load, save
from DataAnalyzer.Data.cl_data import FileData
from DataAnalyzer.Plot.cl_zoom import Zoom


class Plot:
    """
    Plot is responsible for building the Plot from the Data inside of a FileData object.
    The created axes objects can be accessed via Plot.figure[..].subplot[...]
    """
    def __init__(self, data, key):
        """Therefore it receives the arguments Data and key upon instantiation.
        `Data` can either be the name of a .mat file or an already created instance of `FileData.`
        `key` is the name of the Plot that should be plotted.

        :param data: name of .mat file or instance of `FileData`
        :type data: str or object
        :param key: name of the Plot type
        :type key: str
        """
        if type(data) == str:
            self.read_data = load(data)
            file_data = FileData(**self.read_data)
        elif type(data) == object:
            file_data = data
        else:
            raise TypeError('Data was not of type string nor object')

        self.data = file_data.plot_data.data      # dictionary
        self.plot = file_data.plot_data.plot    # dictionary
        self.meta = file_data.plot_data.meta      # object

        for figure in self.plot[key].figure:
            for subplot in figure.subplot:
                if subplot.x_label == ' ':
                    try:
                        subplot.x_label = self.data[subplot.plots[0][0]].unit
                    except KeyError:
                        subplot.x_label = self.data[subplot.plots[0]].unit

                if subplot.y_label == ' ':
                    try:
                        subplot.y_label = self.data[subplot.plots[0][1]].unit
                    except KeyError:
                        subplot.y_label = self.data[subplot.plots[0]].unit

        # create list of figures, which can be accessed via
        # self.figure[i].subplot[i]
        self.figure = [self.Subplot(self._create_figures(fig, self.data)) for fig in self.plot[key].figure]

        # self.ax_list contains the ax objects for every subplot that is linked
        try:
            self.ax_list = [self.figure[int(link[0])].subplot[int(link[1])] for link in self.plot[key].linkaxes]

            self._linkaxes()
            self._auto_zoom()
        except AttributeError:
            pass

    def _linkaxes(self):
        """links all axes in `self.ax_list`"""
        self.ax_list[0].get_shared_x_axes().join(*self.ax_list)

    def _auto_zoom(self):
        """creates a `Zoom` object for every ax object in `self.ax_list`"""
        for ax in self.ax_list:
            Zoom(ax)

    @staticmethod
    def _create_figures(fig_config, data):
        """_create_figures is a private method, which -as the name suggests- creates the figure instances.

        :param fig_config: figure configuration stored in file_data.plot_data.Plot[...].figure[...]
        :param data: the actual plotting Data
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
        """dataclass in which the subplots are stored as a list"""
        subplot: list
