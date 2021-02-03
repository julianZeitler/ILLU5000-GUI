# Standard library imports
import numpy as np

# Third party imports
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.io import savemat, loadmat

# Local application imports
from zoom import AutoYrange


x = np.arange(0, 5 * np.pi, 0.01)
# axesSubplot objects
ax = []
# line objects for every plot (n-D List for n plots on subplot)
line = []

gs = GridSpec(3, 1)
fig1 = plt.figure(1)

ax.append(fig1.add_subplot(gs[0, 0]))
ax.append(fig1.add_subplot(gs[1, 0], sharex=ax[0]))
ax.append(fig1.add_subplot(gs[2, 0], sharex=ax[0]))

line.append(ax[0].plot(x, np.sin(x), x, np.sin(2*x)))
line.append(ax[1].plot(x, np.sin(3*x), x, np.sin(4*x)))
line.append(ax[2].plot(x, 10*np.sin(x), x, 10*np.sin(2*x)))

fig2 = plt.figure(2)

ax.append(fig2.add_subplot(gs[0, 0], sharex=ax[0]))
ax.append(fig2.add_subplot(gs[1, 0], sharex=ax[0]))
ax.append(fig2.add_subplot(gs[2, 0], sharex=ax[0]))

line.append(ax[3].plot(x, 5*np.sin(3*x), x, 3*np.sin(2*x)))
line.append(ax[4].plot(x, np.sin(x), x, np.sin(4*x)))
line.append(ax[5].plot(x, np.sin(x), x, np.sin(5*x)))

# create callback for every plot
for i in range(len(ax)):
    AutoYrange(ax[i], line[i])

plt.show()
