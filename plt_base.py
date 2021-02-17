class Base:
    def __init__(self,
                 plots,
                 title='',
                 x_label='X-Axis',
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
