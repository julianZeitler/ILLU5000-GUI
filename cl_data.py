from dataclasses import dataclass


@dataclass
class Config:
    subplot: tuple = (1, 1)
    title: str = 'Default title'
    legend_location: str = 'upper left'
    x_label: str = 'default x_label'
    y_label: str = 'default y_label'


@dataclass
class PlotData:
    values: list
    name: str
    unit: str


@dataclass
class Meta:
    timestamp_last_sample: float
    location: str
    machine: str
    worker: str


class Top:
    def __init__(self, __header__: bytes, __version__: str, __globals__: list, trace):
        self.__header__ = __header__
        self.__version__ = __version__
        self.__globals__ = __globals__

        # map the trace dictionary on the Trace class
        trace.pop('static')
        self.trace = self.Trace(**trace)

    class Trace:
        def __init__(self, data, meta, plot):
            data.pop('static')
            meta.pop('static')
            plot.pop('static')
            self.meta = Meta(**meta)

            # add the plot information + data to PlotData objects for every k, v in data
            # values of data are PlotData objects, e.g. the name of raw_x1 can be accessed like this:
            # top.trace.data['raw_x1'].name
            self.data = {k: PlotData(**v) for k, v in data.items()}

            # overwrite the standard config with custom config
            # and create Config objects
            self.plot = {k: [Config(**inner_v) for inner_v in v]
                         for k, v in plot.items()}

