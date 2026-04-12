import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 20)

ax1 = plt.axes()
ax1.plot(np.sin(x))
bottom, left, width, height
0.4 - 40% of figure width
ax2 = plt.axes([0.4, 0.3, 0.2, 0.1])
ax2.plot(np.cos(x))

fig = plt.figure()
ax1 = fig.add_axes()
ax2 = fig.add_axes()

plt.axes([0, 0, 1, 1])
subplot(2, 3, i)
sin(x + np.pi / 4 * i)

fig, ax = plt.subplots(2, 3, sharex="col")

x1 = np.linspace(0, 10, 50)
x2 = np.linspace(0, 20, 100)

for i in range(2):
    for j in range(3):
        if i % 2 == 0:
            ax[i, j].plot(np.sin(x1 + np.pi / 4 * (i*2 + j)))
        else:
            ax[i, j].plot(np.sin(x2 + np.pi / 4 * (i*2 + j)))
plt.axes()

plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1])
plt.subplot(grid[:, 2])
plt.subplot(grid[1, :2])

grid = plt.GridSpec(4, 4, ws=0.2, hspace=0.1)  # note: 'ws' is likely a typo; should be 'wspace'

rng = np.random.default_rng(1)
x, y = rng.multivariate_normal([0, 0], [[1, 2], [3, 4]], 1000).T

main_axes = plt.subplot(grid[:-1, 1:])  # X
y_axes = plt.subplot(grid[:-1, 0])     # Y
x_axes = plt.subplot(grid[-1, 1:])     # Z

main_axes.plot(x, y, 'ok', alpha=0.2)
y_axes.hist(y, 40, orientation="horizontal", color='grey')
y_axes.invert_xaxis()

births = pd.read_csv("./digital_python-25-26/data/births-1969.csv")

births["day"] = births["day"].astype(int)

births.index = pd.to_datetime(
    births["year"] * 10000 + births["month"] * 100 + births["day"],
    format="%Y%m%d"
)

births_dom = births.pivot_table("births", index=[births.month, births.day])

fig, ax = plt.subplots()

print(births)

births_dom = births.pivot_table("births", index=[births.index.month, births.index.day])
from datetime import datetime

births_dom.index[datetime(1969, month, day) for (month, day) in births_dom.index]

fig, ax = plt.subplots()
births_dom.plot(ax=ax)

ax.text('1969-10-10', 5500, "New Year")

ax.annotate(
    "Annotation text",
    xy=("1969-1-1", 5500),
    xtext=("1969-12-1", 4500),   # likely a typo; should be 'xytext'
    # arrowprops=dict(facecolor="black"),
    arrowprops=dict(arrowstyle="-", facecolor="black", connectionstyle="angle3,angleA=0, a=")
)

ax1 = plt.axes()
ax1.set_xlim(0,2)
ax2 = plt.axes([0.4, 0.3, 0.1, 0.2])

ax1.text(0.6, 0.8, "#1_1", transform=ax1.transData)
ax2.text(0.6, 0.8, "#2_1", transform=ax2.transData)

ax1.text(0.5, 0.1, "#1_2", transform=ax1.transAxes)
ax2.text(0.5, 0.1, "#2_2", transform=ax2.transAxes)

ax1.text(0.05, 0.05, "#13", transform=fig.transFigure)
ax2.text(0.2, 0.2, "#23", transform=fig.transFigure)

plt.show()

