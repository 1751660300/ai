# -*- coding:utf-8 -*-
import matplotlib.animation as ma
import matplotlib.pyplot as mpl
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)
width = np.random.randn(100)
# z = np.vstack(x, y).T
# print(z)
sc = mpl.scatter(
    x, y,
    s=width,
    c=width,
    cmap='jet',
    marker='o'
)


# 定义函数行为
def update(number):
    global width, x, y
    index = number % 100
    x[index] = np.random.randn(1)
    y[index] = np.random.randn(1)
    width[index] = 0
    width += 30
    sc.set_sizes(width)
    z = np.vstack((x, y)).T
    sc.set_offsets(z)


ania = ma.FuncAnimation(mpl.gcf(), update, interval=10)
mpl.show()


# 问题：
# sc.set_offsets() 接收的参数是nx2的数组 [[1,2], [1,2], ...]
# numpy 的数组合并接收的参数只有一个，所有多个数组则要转为元组
# 调用ma.FuncAnimation函数，必须要接收返回值，否则该函数不会执行
