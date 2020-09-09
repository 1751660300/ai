# -*- coding:utf-8 -*-
# 使用矩阵实现斐波那契
import numpy as np
a = np.mat('1,1;1,0')

for i in range(10):
    print((a ** i)[0, 0])