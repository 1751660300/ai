# -*- coding:utf-8 -*-
"""
1.二项分布随机数
    产生size个随机数，每个随机数来自n次尝试中成功的次数，其中每次成功的概率为p
    使用random.binomial(n, p, size)
2.超几何分布
    产生size个随机数，每个随机数t为在总样本中抽取nsample个样本后好样本的个数
    总样本由ngood好样本和nbad坏样本组成
    np.random.hypergeometric(ngood, nbad, nsample, size)
"""
import numpy as np
n = np.random.random((2, 2))
print(np.random.rand(2, 2))
print("-"*50)
print(np.random.choice([1, 2, 5, 6], 6))
print("-"*50)
print(np.random.binomial(10, 0.3, (2, 2)))
print("-"*50)
# print(np.random.hypergeometric(ngood, nbad, nsample, size))
print("-"*50)
print(n)
