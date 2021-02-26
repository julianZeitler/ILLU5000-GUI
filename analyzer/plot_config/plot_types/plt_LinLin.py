from analyzer.plot_config.two_d.plt_TwoD import TwoD
from analyzer.functions.func_import import dyn_import_cls


class LinLin(TwoD):
    def plot_specific(self, ax):
        cls = dyn_import_cls('analyzer.plot.cl_regression', self.regression)
        reg = cls(ax)
        reg.fit()
