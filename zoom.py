

class AutoYrange:
    def __init__(self, ax, lines):
        # ax -> AxesSubplot object
        # lines -> list from line objects, each line represents one plot
        self.ax = ax
        self.lines = lines
        self.x_data = [list(line.get_xdata()) for line in lines]
        self.y_data = [list(line.get_ydata()) for line in lines]
        self.cid = ax.callbacks.connect('xlim_changed', self)

    # Gets executed when AutoYrange() is called
    def __call__(self, event):
        scale = len(self.y_data[0]) / self.x_data[0][-1]
        limits = [int(limit * scale) for limit in event.get_xlim()]
        min_array = []
        max_array = []

        if limits[0] < 0:
            limits[0] = 1
        if limits[1] > len(self.x_data[0]):
            limits[1] = len(self.x_data[0])
        if limits[0] == limits[1]:
            limits[1] += 1

        for line in range(len(self.y_data)):
            min_array.append(min(self.y_data[line][limits[0]:limits[1]]))
            max_array.append(max(self.y_data[line][limits[0]:limits[1]]))

        new_limits = [min(min_array),
                      max(max_array)]

        offset = (new_limits[1] - new_limits[0]) * 0.05
        new_limits[0] = new_limits[0] - offset
        new_limits[1] = new_limits[1] + offset

        event.set_ylim(new_limits[0], new_limits[1])
