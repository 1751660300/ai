# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl
# mp.rcParams['font.sans-serif'] = ['SimHei']
# mp.rcParams['axes.unicode_minus'] = False

labels = 'Duck', 'Dog', 'Cow', 'Pig'
size = [15, 30, 45, 10]
explode = (0.1, 0.1, 0, 0)
fig1, ax1 = mpl.subplots()
ax1.pie(size, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
ax1.legend(loc='best')
mpl.show()