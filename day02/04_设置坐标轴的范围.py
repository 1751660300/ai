# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=1000)
y = np.sin(x)
# 设置x轴范围
mpl.xlim(-np.pi, np.pi)
# 设置y轴范围
mpl.ylim(-0.5, 0.5)
# 绘制图形
mpl.plot(x, y)
mpl.show()
