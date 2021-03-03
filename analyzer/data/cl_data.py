"""This module is responsible for creating a data tree from a dictionary"""

from dataclasses import dataclass

# function to dynamically import classes
from analyzer.functions.func_import import dyn_import_cls


class FileData:
    """
    FileData is the top-level class for storing the config and data specified in the mat file in a hierarchical
    structure.

    .. note::
       This tree is build upon nested classes and not inheritance!

    """
    def __init__(self, __header__: bytes, __version__: str, __globals__: list, plot_data):
        """ When creating mat files, the variables `__header__`, `__version__` and `__globals__` always get set. Because
        double underscores are Python specific syntax these variables get stored without them. `plot_data` is read
        from the mat file as a dictionary and contains the actual configuration and plotting data.

        :param __header__: Matlab specific header
        :type __header__: bytes
        :param __version__: Matlab version
        :type __version__: str
        :param __globals__: Matlab globals
        :type __globals__: list
        :param plot_data: Data for creating the plots
        :type plot_data: dict

        When declaring `self.plot_data`, `plot_data` is given to the constructor of `PlotData` class.
        """
        self.header = __header__
        self.version = __version__
        self.globals = __globals__

        # map the trace dictionary on the Trace class
        self.plot_data = self.PlotData(**plot_data)

    class PlotData:
        """ `PlotData` only defines the `__init__` method to store data, where the members `self.data`, `self.plot`
        and `self.meta` are declared.
        """
        def __init__(self, data, plot, meta):
            """ `self.data`'s keys are assigned dynamically, so the variable `self.data` is a dictionary itself, that
            can be accessed with the keywords defined previously.

            :param data: data contains the actual plot data
            :type data: dict

            The same is true for `self.plot`, where different plot types can be defined. The dict's values are defined
            as objects of the Figure class which then contains a list of all figure configuration.

            :param plot: plot contains the configuration of the plots
            :type plot: dict

            `self.meta` contains meta information like the time when the trace has been recorded. `self.meta` gets
            assigned to an object of the `Meta` dataclass.

            :param meta: meta contains meta information about the recorded data
            :type meta: dict
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
            """`Data` is the class, where the actual plotting data can be stored in."""
            values: list
            name: str
            unit: str

        @dataclass
        class Meta:
            """`Meta` is the class, where meta information can be stored in."""
            timestamp_last_sample: float
            location: str
            machine: str
            worker: str

        class Figure:
            """
            `Figure` defines the `__init__` method, as well as the `FigConfig` class.
            The figure configuration can be accessed with **plot_data.plot[...].figure[n]**
            """
            def __init__(self, figure):
                """The amount of figures can vary, therefore `self.figure` gets assigned as a list.

                :param figure: a dictionary with the figure config as its value
                """
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
                """`FigConfig` only defines an `__init__` method. It takes the actual figure configuration.
                Besides the figure config, it contains the subplots and their configuration.
                It is possible to create custom plot types, therefore the configuration of the subplots is outsourced
                to the `plot_config` package. `FigConfig` only imports those classes dynamically and creates objects
                with the according values.

                .. note::
                   Custom plotting types can be added

                """
                def __init__(self,
                             subplot,
                             subplot_rows: int = 1,
                             subplot_cols: int = 1,
                             constrained_layout: bool = True
                             ):
                    """
                    .. note::
                       individual subplots configs are saved dynamically to plot type classes!

                    `__init__` defines the figure configuration:

                    :param subplot: list of subplot configs
                    :type subplot: list
                    :param subplot_rows: number of subplots in y-dimension
                    :type subplot_rows: int
                    :param subplot_cols: number of subplots in x-dimension
                    :type subplot_cols: int
                    :param constrained_layout: automatic, ideal space organization
                    :type constrained_layout: bool
                    """

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
                            # try to import the class of the plot_type,
                            # if none is specified LinLin gets imported as default
                            cls = dyn_import_cls('analyzer.plot_config.plot_types.plt_' + plot['plot_type'],
                                                 plot['plot_type'])

                        except KeyError:
                            cls = dyn_import_cls('analyzer.plot_config.plot_types.plt_LinLin', 'LinLin')

                        # append and create the subplot objects
                        self.subplot.append(cls(**plot))
