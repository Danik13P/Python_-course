import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Figure
# Axes - axis (x,y)

grid = plt.GridSpec(1, 2)
ax1 = plt.subplot(grid[0, 0])
ax2 = plt.subplot(grid[0, 1])


ax1 = plt.subplot(grid[0, 0])
ax1.set_xscale("log")
ax1.set_xlim(1, 1000)
ax1.grid(True, which="major")

ax2 = plt.subplot(grid[0, 1])
ax2.set_yscale("log")
ax2.set(ylim=(1, 1000))
ax2.grid(True, which="major")

print(ax1[axis.get_major_locator()])
print(ax1.axes.get_major_formatter())
print(ax1.axes.get_minor_locator())
print(ax1.axes.get_minor_formatter())

print(ax1.yaxis.get_major_locator())
print(ax1.yaxis.get_major_formatter())
print(ax1.yaxis.get_minor_locator())
print(ax1.yaxis.get_minor_formatter())

ax1.axis.set_major_formatter(plt.NullFormatter())
ax2.axis.set_major_locator(plt.NullLocator())

from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces().images

fig, ax = plt.subplots(7, 7)
fig.subplots_adjust(hspace=0, wspace=0)

for i in range(7):
    for j in range(7):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[7 * i + j], cmap="binary_r")

x = np.linspace(0, 4 * np.pi, 1000)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label="Sinus")
ax.plot(x, np.cos(x), label="Cosinus")

for a in ax.flat:
    a.xaxis.set_major_locator(plt.MaxNLocator(10))
    a.yaxis.set_major_locator(plt.MaxNLocator(2))
    ax[i, j].imshow(faces[7 * i + j], cmap="binary_r")

def ff(value, tick_number):
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return 0
    elif N == 1:
        return r"$%frac{pi}{2}s"
    elif N == 2:
        return r"$%pi$"
    elif N % 2 == 0:
        t = int(N / 2)
        return f"{t}" + r"$%pi$"
    else:
        return f"{t}" + r"$%frac{pi}{2}$"
        # 0, pi/2, pi, 3/2 pi, 2 pi, 5/2 pi, 3 pi, 7/2 pi, 4 pi
    return value

x = np.linspace(0, 4 * np.pi, 1000)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label="Sinus")
ax.plot(x, np.cos(x), label="Cosinus")

for i in ax.flat:

ax[0].xaxis.set_major_locator(plt.NullLocator())
ax[1].xaxis.set_major_locator(plt.MultipleLocator(0.8))
ax[2].xaxis.set_major_locator(plt.FixedLocator([1, 3, 8, 9]))
ax[3].xaxis.set_major_locator(plt.LinearLocator(numticks=4))
ax[4].xaxis.set_major_locator(plt.IndexLocator(base=2, offset=1.3))
ax[5].xaxis.set_major_locator(plt.AutoLocator())
ax[6].xaxis.set_major_locator(plt.MaxNLocator(8))
ax[7].xaxis.set_major_locator(plt.LogLocator(base=3))

import matplotlib.ticker as mtick

ax[1].xaxis.set_major_formatter(plt.NullFormatter())
ax[2].xaxis.set_major_formatter(plt.FixedFormatter(['a', 'b', 'c', 'd']))
ax[3].xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f $m^2$'))
ax[4].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=4))

plt.style.use('./digital_python-25-26/lec_13.style')

x = np.random.randn(1000)
plt.figure(faccolor='#921212')
plt.axes(faccolor='#adadad')

x = np.random.randn(1000)
plt.figure(faccolor='#921212')
plt.axes(faccolor='#adadad')

plt.rc("figure", faccolor='#921212')
plt.rc("axes", faccolor='#adadad')

plt.hist(x)

from mpl_toolkits import mplot3d

def f(x, y):
    return np.sin(x * pi / 2 + np.sqrt(x**2 + y**2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-10, 10, 50)

print(y.shape)

X, Y = np.meshgrid(x, y)

print(X.shape)
print(Y.shape)

print(X)
print(Y)

Z = f(X, Y)
print(Z.shape)
print(Z)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.contour3D(X, Y, Z, 40)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(0, 90)

plt.hist(x)
plt.show()