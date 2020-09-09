# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-50, 50, num=1000)
y = x ** 3 + 2 * x ** 2 - 12 * x + 6
mpl.plot(x, y)
mpl.hlines(0, -50, 50)
ax = mpl.gca()
ax.xaxis.set_major_locator(mpl.MultipleLocator(1))
ax.xaxis.set_minor_locator(mpl.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mpl.MultipleLocator(1))
mpl.xlim(-10, 10)
mpl.ylim(-20, 20)
mpl.show()
# 创建一个矩阵
data = np.mat("1 3 5; 2 0 3; 1 0 1")
print(data)
# 调用eigvals求解特征值
c = np.linalg.eigvals(data)
# 求解特征值和特征向量
c1, c2 = np.linalg.eig(data)
print(c1, c2)

# 验证
for i in range(len(c1)):
    print("1:", np.dot(data, c2[:, i]))
    print("2:", c1[i] * c2[:, i])

sum0 = 0
sum1 = 2
for i in range(len(c1)):
    sum0 = sum0 + c1[i]
    # sum1 = sum1 + data[i][i]
print(sum0)

