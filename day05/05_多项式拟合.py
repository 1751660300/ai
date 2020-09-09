# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

p = [-3, 1, 2, 1, 5]
x = np.arange(10)
y = 4 * x ** 2 - x + 1

# 去多项式拟合的系数
P = np.polyfit(x, y, 1)
print(P)

# 求得拟合值
y1 = np.polyval(P, x)
mpl.figure('nihe', facecolor='gray')
mpl.title("polyfit", fontsize=10)
mpl.scatter(x, y, color='red', marker='o')
mpl.plot(x, y1, color='blue', linestyle='-')
mpl.show()
