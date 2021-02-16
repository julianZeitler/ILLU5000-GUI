from dataclasses import dataclass

from plt_LinLin import LinLin
from func_import import dyn_import_cls


class Top:
    def __init__(self, __header__: bytes, __version__: str, __globals__: list, plot_data):
        self.__header__ = __header__
        self.__version__ = __version__
        self.__globals__ = __globals__

        # map the trace dictionary on the Trace class
        self.plot_data = self.PlotData(**plot_data)

    class PlotData:
        def __init__(self, data, plot, meta):
            # add the plot information + data to Data objects for every k, v in data
            self.data = {k: self.Data(**v) for k, v in data.items()}

            self.plot = {k: self.Figure(v) for k, v in plot.items()}

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
                self.figure = []
                for fig in figure.values():
                    for f in fig:
                        self.figure.append(self.FigConfig(**f))

            class FigConfig:
                def __init__(self,
                             subplot,
                             title: str = ' ',
                             subplot_rows: int = 1,
                             subplot_cols: int = 1
                             ):

                    self.title = title
                    self.subplot_rows = subplot_rows
                    self.subplot_cols = subplot_cols

                    if type(subplot) == dict:
                        try:
                            cls = dyn_import_cls('plt_' + subplot['plot_type'], subplot['plot_type'])
                        except KeyError:
                            cls = dyn_import_cls('plt_LinLin', 'LinLin')
                        self.subplot = [cls(**subplot)]

                    else:
                        self.subplot = []
                        for plot in subplot:
                            try:
                                cls = dyn_import_cls('plt_' + plot['plot_type'], plot['plot_type'])
                            except KeyError:
                                cls = dyn_import_cls('plt_LinLin', 'LinLin')
                            self.subplot.append(cls(**plot))
