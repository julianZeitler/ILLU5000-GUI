from numpy import asarray


class Base:
    def __init__(self,
                 plots,
                 title='',
                 x_label='time',
                 y_label='Y-Axis',
                 legend='upper left',
                 share_x='',
                 share_y='',
                 plot_type='LinLin'):

        self.plots = plots
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.legend = legend
        self.share_x = share_x
        self.share_y = share_y
        self.plot_type = plot_type

    def plot(self, ax, data):
        if not isinstance(self.plots[0], list):
            self.plots = [self.plots]

        for plot in self.plots:
            ax.plot(asarray(data[plot[0].strip()].values),
                    asarray(data[plot[1].strip()].values),
                    label=data[plot[1].strip()].name)

        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.set_title(self.title)
        ax.legend(loc=self.legend)
