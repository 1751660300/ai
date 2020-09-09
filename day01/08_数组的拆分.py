# -*- coding:utf-8 -*-
import numpy as np
data = np.arange(12)

data.shape = (6, 2)
print(data, end="\n")

a, b = np.vsplit(data, 2)
print(a, b, sep="\n")

data = np.dstack((a, b))
print(data)

# 一维数组的组合
data1 = np.arange(5)
data2 = np.arange(5)

a = np.row_stack((data1, data2))
b = np.column_stack((data1, data2))
print(a)
print(b)

