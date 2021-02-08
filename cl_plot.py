import matplotlib.pyplot as plt


class Plot:
    def __init__(self, x_dim, y_dim, constrained=True, suptitle=None):
        self.x_dim = x_dim
        self.y_dim = y_dim

        self.fig, self.ax = plt.subplots(self.y_dim, self.x_dim, constrained_layout=constrained)

        if suptitle:
            self.fig.suptitle(suptitle)
    
    def subplot(self, n, y_data, x_data, name=('name'), unit=('unit'), style=('-'), title=None):
        try:
            iter(y_data)
            cnt = 0
            for data in y_data:
                self.ax[n].plot(x_data, data, style[cnt], label=name[cnt])
                cnt += 1
        except:
             self.ax[n].plot(x_data, y_data, style[cnt], label=name[0])

        if title:
            self.ax[n].set_title(title)
        if xlabel:
            self.ax[n].set_xlabel(xlabel)
        if ylabel:
            self.ax[n].set_ylabel(xlabel)


'''
# axesSubplot objects
ax = []
# line objects for every plot (nD List for n plots on subplot)
line = []

gs_1 = GridSpec(1, 1)
fig1 = plt.figure(1)

ax.append(fig1.add_subplot(gs_1[0, 0]))
line.append(ax[0].plot(t_incremental.values, raw_x1.values, label=raw_x1.name))


gs_2 = GridSpec(1, 2)
fig2 = plt.figure(2)

ax.append(fig2.add_subplot(gs_2[0, 0], sharex=ax[0]))
ax.append(fig2.add_subplot(gs_2[0, 1], sharex=ax[0]))
line.append(ax[1].plot(t_incremental.values, raw_x2.values, label=raw_x2.name))
line.append(ax[2].plot(t_incremental.values, raw_x3.values, label=raw_x3.name))

ax[0].set_ylabel(raw_x1.name)
ax[1].set_ylabel(raw_x2.name)
ax[2].set_ylabel(raw_x3.name)

for i in ax:
    i.set_xlabel(t_incremental.name)
    i.legend()

# create callback for every plot
for i in range(len(ax)):
    AutoYrange(ax[i], line[i])
'''
