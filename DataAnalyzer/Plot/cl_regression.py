"""This module can be used to add trendlines to the plots.

.. todo:: Add more regression types (trigo, log, ...).
"""

from numpy import asarray, sqrt, log, exp


class Regression:
    """The specific regression types inherit from this class."""
    def __init__(self, ax):
        """Read the Data from the axes and calculate the sums of x- and y-Data

        :param ax: axis object
        :type ax: object
        """
        self.ax = ax

        self.lines = ax.lines[:]
        self.x_data = [list(line.get_xdata()) for line in self.lines]
        self.x_data = self.x_data[0]
        self.y_data = [list(line.get_ydata()) for line in self.lines]
        self.y_data = self.y_data[0]

        self.sum_x = sum(self.x_data)
        self.sum_y = sum(self.y_data)


class Linear(Regression):
    """Create a linear regression"""
    def fit(self):
        """Calculate the parameters with the method of smallest error squares"""
        sum_x2 = 0
        for x in self.x_data:
            sum_x2 = sum_x2 + x * x

        sum_xy = 0
        for i in range(len(self.x_data)):
            sum_xy = sum_xy + self.x_data[i] * log(self.y_data[i])

        sum_y = 0
        for y in self.y_data:
            sum_y = sum_y + log(y)

        # y = ax + b
        b = (sum_xy - sum_y * sum_x2 / self.sum_x) / (self.sum_x - sum_x2 * len(self.x_data) / self.sum_x)
        a_ = (sum_y - len(self.x_data) * b) / self.sum_x
        a = exp(a_)

        graph = [(a * exp(x*b)) for x in self.x_data]
        self.ax.plot(asarray(self.x_data), asarray(graph), label='regression')


class Exponential(Regression):
    """Create an exponential regression

    .. todo::
        currently only two parameters are calculated of the form y = a(e^bx).
        Add a third parameter c: y = a(e^bx) + c
    """
    def fit(self):
        """Calculate the parameters with the method of smallest error squares"""
        sum_x2 = 0
        for x in self.x_data:
            sum_x2 = sum_x2 + x * x

        sum_xy = 0
        for i in range(len(self.x_data)):
            sum_xy = sum_xy + self.x_data[i] * self.y_data[i]

        # y = ax + b
        b = (sum_xy - self.sum_y * sum_x2 / self.sum_x) / (self.sum_x - sum_x2 * len(self.x_data) / self.sum_x)
        a = (self.sum_y - len(self.x_data) * b) / self.sum_x

        graph = [(a * x + b) for x in self.x_data]
        self.ax.plot(asarray(self.x_data), asarray(graph), label='regression')


class Root(Regression):
    """Create a square root regression"""
    def fit(self):
        """Calculate the parameters with the method of smallest error squares"""
        sum_sx = 0
        for x in self.x_data:
            sum_sx = sum_sx + sqrt(x)

        sum_xy = 0
        for i in range(len(self.x_data)):
            sum_xy = sum_xy + sqrt(self.x_data[i]) * self.y_data[i]

        # y = sqrt(ax) + b
        b = (sum_xy - self.sum_y*self.sum_x/sum_sx)/(sum_sx - self.sum_x*len(self.x_data)/sum_sx)
        a_ = (self.sum_y - len(self.x_data)*b) / sum_sx
        a = a_ * a_

        graph = [(sqrt(a * x) + b) for x in self.x_data]
        self.ax.plot(asarray(self.x_data), asarray(graph), label='regression')
