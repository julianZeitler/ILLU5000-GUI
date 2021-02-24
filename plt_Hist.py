from numpy import asarray

from plt_Base import Base


class Hist(Base):
    def __init__(self,
                 bins,
                 *args,
                 **kwargs):

        self.bins = bins
        super().__init__(*args, **kwargs)

    def plot(self, ax, data):

        if not isinstance(self.plots[0], list):
            self.plots = [self.plots]

        if len(self.plots) == 1:
            n, bins, patches = ax.hist(asarray(data[self.plots[0].strip()].values),
                                       self.bins)
        else:
            for plot in self.plots:
                n, bins, patches = ax.hist(asarray(data[plot[0].strip()].values),
                                           self.bins)
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.set_title(self.title)
        ax.grid(self.grid)
