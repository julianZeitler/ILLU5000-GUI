from DataAnalyzer.PlotConfig.TwoD.plt_TwoD import TwoD
from DataAnalyzer.Functions.func_import import dyn_import_cls


class LinLin(TwoD):
    def plot_specific(self, ax):
        cls = dyn_import_cls('DataAnalyzer.Plot.cl_regression', self.regression)
        reg = cls(ax)
        reg.fit()
