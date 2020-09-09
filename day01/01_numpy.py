# -*- coding:utf-8 -*-
import numpy as np

#  numpy.ndarray类的对象表示n维数组
array = np.array([1, 2, 3, 4, 5, 6])
print(array, type(array))
print(array.shape)  # shape代表维度
# array.shape = (2, 3)  # 修改array的维度,如果数据不够,则报错
# print(array,array.shape)

# 数组的运算 与每个元素相乘
print(array * 3)
print(array > 3)



# data = [("zs", [126, 100, 25], 25),
#         ("ls", [100, 25, 96], 23)]
data = [
    ('zs', [90, 80, 85], 15),
    ('ls', [92, 81, 83], 16),
    ('ww', [95, 85, 95], 15)
]
# 设置detype
a = np.array(data, dtype={"names": ['name', 'scores', 'age'],
                          "formats": ['U2', '3int32', 'int32']})
print(a)
