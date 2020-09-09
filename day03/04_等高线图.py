# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

n = 1000
x = np.linspace(-5, 5, n)
# a = [x for i in range(1000)]
# # rx = np.mat(a)
# ry = rx.T
rx, ry = np.meshgrid(x, x)
# print(rx)
# print(ry)
# z = rx ** 2 + ry ** 2
z = (1 - rx / 2 + rx ** 5 + ry ** 3) * np.exp(-rx ** 2 - ry ** 2)
mpl.figure('等高线图')
mpl.title('contour')
cntr = mpl.contour(
    rx, ry, z, 8,
    # colors='bla
    cmap='jet',
    linewidths=0.5
)

mpl.clabel(cntr, fmt='%.1f', inline_spacing=1, fontsize=5)
mpl.contourf(
    rx, ry, z, 80,
    # colors='bla
    cmap='jet',
    # linewidths=0.5
)
mpl.show()
