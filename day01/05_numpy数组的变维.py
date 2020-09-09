# -*- coding:utf-8 -*-
import numpy as np
# 创建一个数组
data = np.ones(6, dtype="u8")
print(data)

# 第一种变维方式（视图变维）
data1 = data.reshape(3, 2)  # 行 列
print("reshape变维：\n", data1)
data1[0, 0] = 2
print("源数据：\n", data)
print("变维后的数据：\n", data1)

data1 = data.ravel()
print("ravel变维：\n", data1)
data1[2] = 3
print("源数据：\n", data)
print("变维后的数据：\n", data1)

# 第二种变维方式（复制变维）
data3 = data.flatten()  # 具有独立的数据
data3 = data1.reshape(2, 3)
print("flatten变维：\n", data3)

# 第三种变维方式
data.shape = (2, 3)
print("shape属性变维：\n", data)
data.resize(3, 2)
print("resize方法变维：\n", data)
