from plt_TwoD import TwoD


class LinLog(TwoD):
    @staticmethod
    def plot_specific(ax):
        ax.set_yscale('log')
