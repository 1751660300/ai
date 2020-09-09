# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

# from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d import Axes3D

n = 100
# x = np.random.normal(0, 1, n)
# y = np.random.normal(0, 1, n)
# z = np.random.normal(0, 1, n)
x = np.random.randn(100) * 10
y = np.random.randn(100) * 10
z = np.random.randn(100) * 10
# 绘制三维点阵
gs = mpl.GridSpec(3, 2)
ax3d = mpl.subplot(gs[0, :], projection='3d')
mpl.title('3d')

# ax3d = mpl.gca(projection='3d')
# ax3d = Axes3D(d3)
ax3d.scatter(
    x, y, z, marker='o',
    c=z,
    s=60,
    cmap='jet'
)

# 绘制三维曲面图
ax3d1 = mpl.subplot(gs[1, :], projection='3d')
n1 = 1000
x = np.linspace(-5, 5, n1)
rx, ry = np.meshgrid(x, x)  # 将坐标网格化，必须用这个函数
z = (1 - rx / 2 + rx ** 5 + ry ** 3) * np.exp(-rx ** 2 - ry ** 2)
# ax3d1 = mpl.gca(projection='3d')
# ax3d1 = Axes3D(sur)
ax3d1.plot_surface(
    rx,
    ry,
    z,
    cstride=30,
    rstride=30,
    cmap='jet'
)

mpl.subplot(gs[2, :], projection='polar')
x1 = np.linspace(0, 8*np.pi, 1000)
y1 = np.linspace(0, 100, 1000)
mpl.plot(x1, y1)

mpl.show()
