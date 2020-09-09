# -*- coding:utf-8 -*-
"""
1.积分
    使用scipy.integrate.quad方法求积分
    res = si.quad(f, -5, 5)
    参数1：方法名
    参数2：上底
    参数3：下底
"""
# 求[-5, 5]区间上y = 2 * x ** 2 + 3 * x + 4曲线上的定积分
import numpy as np
import matplotlib.pyplot as mp


def f(x):
    return 2 * x ** 2 + 3 * x + 4


x = np.linspace(-6, 6, num=2000)
mp.figure("int")
mp.title("int", fontsize=14)
mp.plot(x, f(x), label="a", color="red", linewidth=5)
mp.fill_between(x, f(x), 0, f(x) > 0)

import scipy.integrate as si
print(si.quad(f, -5, 5))
mp.legend(loc="best")
mp.show()
