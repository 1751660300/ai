# -*- coding:utf-8 -*-
import numpy as np
data = np.arange(10)
# 一维数组切片
print("一维切片:\n", data[1::2])

data = data.reshape(2, 5)
# 二维数组切片
print("二维切片:\n", data[:3, :3])
