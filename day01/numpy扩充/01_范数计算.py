# -*- coding:utf-8 -*-
import numpy as np

data = np.arange(6)
data=data.reshape(2, 3)
print(data)
print(np.linalg.norm(data, ord=1, keepdims=True))
