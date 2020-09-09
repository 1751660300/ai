# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

# 五种语言的占比
mpl.figure('pie', facecolor='lightgray')
mpl.title('pie')
values = [50.0, 10.2, 15.8, 20.0, 4.0]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['python', 'c#', 'c/c++', 'java', 'kotlin']
colors = ['#ff4455', '#4455ff', '#2233ee', '#ee3322', '#556677']
mpl.pie(
    values,
    spaces,
    labels,
    colors,
    '%.1f%%',
    shadow=True,
    startangle=0,
    radius=0.8
)
mpl.legend(loc='upper right')
mpl.show()