# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=1000)
y = np.sin(x)
# 绘制图形
mpl.plot(x, y)
mpl.title(r'sin(x)')
mpl.show()

