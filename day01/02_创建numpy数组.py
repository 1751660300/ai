# -*- coding:utf-8 -*-
import numpy as np
# 第一种创建方法
data1 = np.array([1, 2, 3, 4, 5, 6])
print(data1, type(data1))

# 第二种创建方法
data2 = np.arange(0, 10, 2)
print("data2:{}".format(data2))

# 第三种创建方法
data3 = np.zeros(6, dtype="i")
print("data3:{}".format(data3))

# 第四种创建方法
data4 = np.ones(6, dtype="U")
print("data4:{}".format(data4))