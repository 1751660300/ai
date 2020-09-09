# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl
import matplotlib as mp
mp.rcParams['font.sans-serif'] = ['SimHei']
mp.rcParams['axes.unicode_minus'] = False
x = np.linspace(1, 12, num=12)
y1 = [15, 45, 21, 23, 15, 31, 23, 54, 56, 53, 15, 61]
y2 = [15, 45, 21, 23, 15, 31, 23, 54, 56, 53, 15, 61]
y2.sort()
mpl.figure('bar', facecolor='lightgray')
mpl.plot(x, y1, label='apple')
mpl.plot(x + 0.4, y2, label='orange')
mpl.bar(
    x, y1, 0.4,
    color='blue',
    alpha=0.4
)
mpl.bar(
    x + 0.4, y2, 0.4,
    color='red',
    alpha=0.4
)
mpl.legend(loc='best')
mpl.xticks([i + 1 for i in range(12)],
           ['一月', '二月', '三月', '四月', '五月', '六月', '七月'
               , '八月', '九月', '十月', '十一月', '十二月'])
mpl.show()
