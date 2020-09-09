# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(-10, 10, 10)
b = np.random.randint(-20, 20, 10)
# 相关矩阵
print(np.corrcoef(a, b))
# 相关矩阵的分子矩阵
print(np.cov(a, b))


