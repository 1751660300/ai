# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=1000)
y = np.sin(x)
# 设置x轴的刻度值
mpl.xticks(np.arange(-np.pi, np.pi+1, np.pi/4),
           [r'$-\pi$', r'$-\frac{3\pi}{4}$', r'$-\frac{\pi}{2}$'
            , r'$-\frac{\pi}{4}$', '0', r'$\frac{\pi}{4}$'
            , r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$'
           , r'$\pi$'])
# 设置y轴的刻度值
mpl.yticks(np.arange(-1, 2, 0.5))

# 绘制图形
mpl.plot(x, y)
mpl.show()
