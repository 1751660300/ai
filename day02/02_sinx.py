# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=1000)
y = np.sin(x)
# 绘制图形
mpl.figure()
mpl.title('sin(x) and cos(x)')
mpl.subplot(121)
mpl.plot(x, y, label='sin(x)', color='green')
mpl.subplot(122)
mpl.plot(x, np.cos(x), label='cos(x)', color='red')
mpl.grid()
mpl.show()
