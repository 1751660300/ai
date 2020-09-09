# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.animation as ma

fig = mpl.figure("qipao")
x = np.random.randn(20)
y = np.random.randn(20)
z = abs(np.random.randn(20))
size = z * 10
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(
    x, y, z,
    s=size,
    marker='o',
    c=z,
    cmap='jet'
    # color='#0000ff'
)

ax.set_title("test")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


def update(number):
    global x, y, z, size
    index = number % 20
    if z[index] > 2:
        x[index] = np.random.randn(1)
        y[index] = np.random.randn(1)
        z[index] = abs(np.random.randn(1))
        size[index] = z[index]
    size += 2
    z += 0.01
    sc.set_sizes(size)
    sc.set_offsets(np.vstack((x, y)).T)


a = ma.FuncAnimation(fig, update, interval=10)
mpl.show()
