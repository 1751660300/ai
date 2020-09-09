# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

a = np.random.randint(-10, 10, 10)
b = np.random.randint(-20, 20, 10)
print(a)
print(b)
x = np.arange(10)
# 平均值
avg_a = a.mean()
avg_b = b.mean()

# 离差
dev_a = a - avg_a
dev_b = b - avg_b

# 协方差
cov_ab = np.mean(dev_a * dev_b)
cov_ba = np.mean(dev_b * dev_a)
print(cov_ba)
mpl.figure("cov", facecolor="gray")
mpl.title("cov", fontsize=10)
A = np.column_stack((a, x))
B = np.column_stack((b, x))
mpl.plot(x, a, color='red', linestyle='-.', label='a')
mpl.plot(x, b, color='blue', label='b')
mpl.legend(loc='best')
# 样本标准差
std_a1 = np.std(a)
std_a = ((a - avg_a) * (a - avg_a)).sum()/(a.size )
std_b1 = np.std(b)
std_b = ((b - avg_b) * (b - avg_b)).sum()/(a.size )
print(np.sqrt(std_a), np.sqrt(std_b))
# 相关系数
c = cov_ba / (np.sqrt(std_a) * np.sqrt(std_b))
d = cov_ba / (std_a1 * std_b1)
print(c, d)
mpl.show()
