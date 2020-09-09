# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl
a = np.random.randint(1, 10, 10)
b = np.random.randint(2, 20, 10)
x = np.arange(10)
# 平均值
avg_a = a.mean()
avg_b = b.mean()

# 离差
dev_a = a - avg_a
dev_b = b - avg_b

# 协方差
cov_ab = (dev_a * dev_b).sum()/10
cov_ba = (dev_b * dev_a).sum()/10

mpl.figure("cov", edgecolor="gray")
mpl.title("cov", fontsize=10)
A = np.column_stack((a, x))
B = np.column_stack((b, x))
mpl.plot(x, a, color='red', linestyle='-.', label='a')
mpl.plot(x, b, color='blue', label='b')
mpl.legend(loc='best')
print(A)
mpl.show()
