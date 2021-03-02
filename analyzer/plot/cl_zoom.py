from matplotlib.pyplot import gca


class Zoom:
    """
    Zoom implements a functionality for automatically altering the y-Limits of the linked subplots.
    """
    def __init__(self, ax):
        # create callback for ax on event xlim_changed
        self.cid = ax.callbacks.connect('xlim_changed', self)

    # Gets executed when AutoYrange() is called
    def __call__(self, event):
        # get the current axis
        ca = gca()
        # get all shared axes from the current axis
        axes = ca.get_shared_x_axes()

        # call self._limits for every axis in the linked axes
        for axis in axes:
            for ax in axis:
                self._limits(event, ax)

    @staticmethod
    def _limits(event, ax):
        """
        :param event: the event from the event handler
        :param ax: axis object
        """
        # get the lines of ax object to retrieve the data from it
        lines = ax.lines[:]
        x_data = [list(line.get_xdata()) for line in lines]
        y_data = [list(line.get_ydata()) for line in lines]

        # calculate scale and get current limits
        scale = len(y_data[0]) / x_data[0][-1]
        limits = [int(limit * scale) for limit in event.get_xlim()]
        min_array = []
        max_array = []

        # handle border cases
        if limits[0] < 0:
            limits[0] = 1
        if limits[1] > len(x_data[0]):
            limits[1] = len(x_data[0])
        if limits[0] == limits[1]:
            limits[1] += 1

        # get the mins/maxs from all plots in a subplot
        for line in range(len(y_data)):
            min_array.append(min(y_data[line][limits[0]:limits[1]]))
            max_array.append(max(y_data[line][limits[0]:limits[1]]))

        # from all mins/maxs get the min/max and set as limit
        new_limits = [min(min_array),
                      max(max_array)]

        # add an offset of 5%
        offset = (new_limits[1] - new_limits[0]) * 0.05
        new_limits[0] = new_limits[0] - offset
        new_limits[1] = new_limits[1] + offset

        # set the new limits
        ax.set_ylim(new_limits[0], new_limits[1])
