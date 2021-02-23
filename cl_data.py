from dataclasses import dataclass

# function to dynamically import classes
from func_import import dyn_import_cls


class Top:
    def __init__(self, __header__: bytes, __version__: str, __globals__: list, plot_data):
        """
        :param __header__: Matlab specific header
        :param __version__: Matlab version
        :param __globals__: Matlab globals
        :param plot_data: Data for creating the plots
        """
        self.__header__ = __header__
        self.__version__ = __version__
        self.__globals__ = __globals__

        # map the trace dictionary on the Trace class
        self.plot_data = self.PlotData(**plot_data)

    class PlotData:
        """
        PlotData class receives and stores data, plot and meta
        """
        def __init__(self, data, plot, meta):
            """
            :param data: data contains the actual plot data
            :param plot: plot contains the configuration of the plots
            :param meta: meta contains meta information about the recorded data
            """
            # data/plot are dictionaries containing another dictionary
            # class Data receives the complete value of data via dictionary unpacking
            self.data = {k: self.Data(**v) for k, v in data.items()}

            # Figure receives the values of plot
            self.plot = {k: self.Figure(v) for k, v in plot.items()}

            # again, Meta gets the values of meta via dictionary unpacking
            self.meta = self.Meta(**meta)

        @dataclass
        class Data:
            values: list
            name: str
            unit: str

        @dataclass
        class Meta:
            timestamp_last_sample: float
            location: str
            machine: str
            worker: str

        class Figure:
            def __init__(self, figure):
                # figure is a dictionary with the figure config as its value
                self.figure = []
                for key, val in figure.items():
                    if key == 'figure':
                        # the configuration is a list
                        for fig in val:
                            # the config of every figure is passed to FigConfig
                            self.figure.append(self.FigConfig(**fig))
                    elif key == 'linkaxes':
                        self.linkaxes = val

            class FigConfig:
                # Inside the figure configuration is also the subplot config
                def __init__(self,
                             subplot,
                             title: str = ' ',
                             subplot_rows: int = 1,
                             subplot_cols: int = 1,
                             constrained_layout: bool = True
                             ):

                    self.title = title
                    self.subplot_rows = subplot_rows
                    self.subplot_cols = subplot_cols
                    self.constrained_layout = constrained_layout

                    # If subplot only contains one element, the parenthesis get removed so they get added manually
                    if type(subplot) == dict:
                        subplot = [subplot]

                    # the subplots are stored in self.subplot
                    self.subplot = []
                    for plot in subplot:
                        try:
                            """
                            try to import the class of the plot_type,
                            if none is specified LinLin gets imported as default
                            """
                            cls = dyn_import_cls('plt_' + plot['plot_type'], plot['plot_type'])

                        except KeyError:
                            cls = dyn_import_cls('plt_LinLin', 'LinLin')

                        # append and create the subplot objects
                        self.subplot.append(cls(**plot))
