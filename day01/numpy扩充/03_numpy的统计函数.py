# -*- coding:utf-8 -*-
import numpy as np
# data = np.linspace(1, 10, num=6).reshape(2, 3)
data = np.random.rand(2, 3)
print(data)
# 极值
print(np.ptp(data, axis=0))
