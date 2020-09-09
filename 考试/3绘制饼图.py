# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

a = np.array(['java', 'c++', 'c', 'python', 'php'])
b = np.array([10, 20, 30, 40, 50])
step = np.array([0, 0, 0.1, 0.1, 0])

mpl.figure('pie')
mpl.pie(
    b, step, labels=a,
    colors=['red', 'green', 'pink', 'black', '#aabbcc'],
    autopct='%.1f%%',
    startangle=0,
    shadow=True
)
mpl.show()