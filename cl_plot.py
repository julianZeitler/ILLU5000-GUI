from matplotlib.pyplot import subplots


class Plot:
    def __init__(self, x_dim, y_dim, constrained=True, subtitle=None):
        self.x_dim = x_dim
        self.y_dim = y_dim

        self.fig, self.ax = subplots(self.y_dim, self.x_dim, constrained_layout=constrained, squeeze=False, sharex=True)

        if subtitle:
            self.fig.suptitle(subtitle)
    
    def subplot(self, x_data, y_data, n=(0, 0), name=('name'), unit=('unit'), style=('-'), title=None):
        try:
            iter(y_data)
            cnt = 0
            for data in y_data:
                self.ax[n[1], n[0]].plot(x_data, data)
                cnt += 1
        except:
            self.ax[n[1], n[0]].plot(x_data, y_data)


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
