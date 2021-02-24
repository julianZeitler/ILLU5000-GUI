from matplotlib.pyplot import subplot
from numpy import asarray

from plt_base import Base


class Polar(Base):
    def plot(self, ax, data):
        ax = subplot(111, projection='polar')

        if not isinstance(self.plots[0], list):
            self.plots = [self.plots]

        for plot in self.plots:
            ax.plot(asarray(data[plot[0].strip()].values),
                    asarray(data[plot[1].strip()].values),
                    label=data[plot[1].strip()].name)

        ax.grid(self.grid)
