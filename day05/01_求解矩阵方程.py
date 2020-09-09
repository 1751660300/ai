# -*- coding:utf-8 -*-
import numpy as np
A = np.arange(1, 11)
A = A.reshape((5, 2))  # 二元一次方程组，x的系数
C = np.array([12, 10, 5, 13, 8])  # 结果
B = np.linalg.lstsq(A, C, rcond=None)[0]  # 使用最小二乘法求解,使用拟合求解

print(np.linalg.solve(A[:2], C[:2]))  # 使用这个函数A[:2]必须是方阵
print(B)
# 验证
print(np.mat(A).I * np.mat(C).T)  # 逆矩阵 * 结果矩阵

print(np.linalg.lstsq(A, C, rcond=-1))

print(np.dot(A, B))
