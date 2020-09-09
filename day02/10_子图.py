# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=1000)
y = np.sin(x)
# 矩阵式分子图
# mpl.subplot(221)
# 绘制图形
# mpl.plot(x, y)
# mpl.subplot(222)
# mpl.plot(x, y)


# 这是网格布局
# gs = mpl.GridSpec(2, 2)
# mpl.subplot(gs[0, 0:2])
# mpl.plot(x, y)
# mpl.subplot(gs[1, 0:2])
# mpl.plot(x, y + 1)

# 自由布局
mpl.figure('Flow Layout', facecolor='lightgray')
mpl.axes([0, 0, 3.0, 3.0])
mpl.plot(x, y)
mpl.show()






