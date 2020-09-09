# -*- coding:utf-8 -*-
import numpy as np

a = np.mat('1,1;1,0')
for i in range(10):
    print(a ** i)
    print('*' * 20)
