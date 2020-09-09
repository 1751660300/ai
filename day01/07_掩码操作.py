# -*- coding:utf-8 -*-
import numpy as np

data = np.arange(100)
# 输出三的倍数
mask = data % 3 == 0
# print(data)
print(data[data % 3 == 0])
print(data[mask])
