# -*- coding:utf-8 -*-
"""
一、符号数组
    sign函数可以把样本数组变成对应的符号数组，正数变为1，负数变为负数，0变为0
    array = np.sign(原数组)
二、数组处理函数
    针对原数组中的每一个元素，检测其是否符合条件序列中的条件，返回符合对应条件的结果序列
    中的元素

    np.piecewise(原数组, 条件序列, 结果序列)
    a = np.array([60, 30, 100])
    p = np.piecewise(a, [a < 60, a == 60, a > 60], [-1, 0, 1])

    p 为 [0, -1, 1]


"""
import numpy as np
a = np.array([60, 30, 100])
p = np.piecewise(a, [a < 60, a == 60, a > 60], [-1, 0, 1])
print(p)

