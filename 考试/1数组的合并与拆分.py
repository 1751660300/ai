# -*- coding:utf-8 -*-
"""
5、一维数组和另外一个一维数组的整合变成二维数组
"""
import numpy as np
a = np.arange(10)
b = np.arange(10, 20)

# 水平合并
c = np.hstack((a, b))
print(c)

# 垂直合并
d = np.vstack((a, b))
print(d)

e = np.dstack((a, b))
print(e)