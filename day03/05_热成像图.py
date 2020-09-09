# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

n = 1000
x = np.linspace(-5, 5, n)
rx, ry = np.meshgrid(x, x)  # 将坐标网格化，必须用这个函数
z = (1 - rx / 2 + rx ** 5 + ry ** 3) * np.exp(-rx ** 2 - ry ** 2)

mpl.imshow(z, cmap='jet', origin='upper')
mpl.colorbar()  # 显示颜色条
mpl.show()

