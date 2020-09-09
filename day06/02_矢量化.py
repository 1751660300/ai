# -*- coding:utf-8 -*-
"""
一、矢量化
    矢量化是指用数组代替标量来操作数组里的每一个元素
    numpy提供了vectorize函数，可以把处理标量的函数矢量化，返回的函数可以直接处理ndarray数组

二、numpy第二矢量化函数
    np.frompyfunc(func, 传递参数的个数, 返回结果的个数)
"""
import numpy as np


# 只能处理标量
def foo(x, y):
    return np.sqrt(x ** 2 + y ** 2)


newFoo = np.vectorize(foo)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(newFoo(a, b))

nfoo = np.frompyfunc(foo, 2, 1)
