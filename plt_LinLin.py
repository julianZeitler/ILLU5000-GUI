from plt_TwoD import TwoD
from func_import import dyn_import_cls


class LinLin(TwoD):
    def plot_specific(self, ax):
        cls = dyn_import_cls('cl_regression', self.regression)
        reg = cls(ax)
        reg.fit()
