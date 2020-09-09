# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

# 绘制简单直线
# 创建两个ndarray数组x，y
x = np.linspace(0, 10, num=15)
y = np.linspace(10, 20, num=15, endpoint=False)

print(x)
print(y.base)


# 画一条直线
mpl.plot(x, y)
# 画一条水平线
mpl.hlines(10, 2, 10)
# 画一条垂直线
mpl.vlines(5, 2, 10)
# 显示

mpl.show()