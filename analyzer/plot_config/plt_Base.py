class Base:
    """
    The Base module is the parent class of all plot_types that are specified in plot_types module.
    This class defines the init method, the most basic configuration can be stored here.
    For basic 2-dimensional plots, the plot method is specified in two_d.plot_TwoD.TwoD.plot().
    For further specification, plot() calls (if it exists) the plot_specific method, which can be defined in every plot
    type.
    """
    def __init__(self,
                 plots,
                 title=' ',
                 x_label='time',
                 y_label='Y-Axis',
                 legend='upper left',
                 share_x='',
                 share_y='',
                 grid=True,
                 plot_type='LinLin',
                 regression=''):

        self.plots = plots
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.legend = legend
        self.share_x = share_x
        self.share_y = share_y
        self.grid = grid
        self.plot_type = plot_type
        self.regression = regression
