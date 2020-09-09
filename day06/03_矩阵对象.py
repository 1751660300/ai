# -*- coding:utf-8 -*-
"""
一、矩阵对象的创建
    1.numpy.matrix(array, copy=True)
    如果copy为True，则创建的矩阵独立创建一份数据
    2.numpy.mat(array)
    与源数据共享，无法复制一份数据独享
二、矩阵的运算
    1.乘法(可以实现斐波那契数列)
        e = numpy.mat([..])
        res = e * e
    2.逆矩阵
        e_ = e.I
        返回的师e的逆矩阵
三、解方程的方式
    1.numpy.linalg.lstsq()
    2.numpy.linalg.solve()
    3.使用逆矩阵来求解
"""
import numpy as np
a = np.mat('3.2 3.4; 3.4 3.6')
b = np.mat('118.6; 120.8')
x = np.linalg.lstsq(a, b, rcond=-1)[0]
print(x)
x = np.linalg.solve(a, b)
print(x)
x = a.I * b
print(x)

# 实现斐波那契数列
e = np.mat('1, 1; 1, 0')
print(e ** 3)

