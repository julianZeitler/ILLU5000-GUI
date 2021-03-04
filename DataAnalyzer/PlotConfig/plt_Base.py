"""The Base module is the parent class of all PlotTypes that are specified in PlotTypes module."""


class Base:
    """This class defines the init method, the most basic configuration can be stored here.
    For basic 2-dimensional plots, the Plot method is specified in `TwoD.plot_TwoD.TwoD.Plot()`.
    For further specification, `Plot()` calls (if it exists) the `plot_specific` method,
    which can be defined in every Plot type.
    """
    def __init__(self,
                 plots,
                 title=' ',
                 x_label='time',
                 y_label='Y-Axis',
                 legend='upper left',
                 grid=True,
                 plot_type='LinLin',
                 regression=''):
        """ The basic subplot config gets stored here.

        :param plots: Name of the plots that are in the subplot
        :type plots: list
        :param title: subplot title
        :type title: str
        :param x_label: x_label
        :type x_label: str
        :param y_label: y_label
        :type y_label: str
        :param legend: legend location (upper left, lower right, ...)
        :type legend: str
        :param grid: toggle grid
        :type grid: bool
        :param plot_type: name of class `Plot()` should be inherited from
            (it is sufficient to write the name without *plt_*)
        :type plot_type: str
        :param regression: optionally add regression type
        :type regression: str
        """

        self.plots = plots
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.legend = legend
        self.grid = grid
        self.plot_type = plot_type
        self.regression = regression
