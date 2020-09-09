# -*- coding:utf-8 -*-
"""
1.什么是奇异值分解？
    一个矩阵M，可以分解为3个矩阵U，S，V，使得U * S * V等于M。
    U，V都是 正交矩阵（正交矩阵乘于该矩阵的转置等于单位矩阵）
    那么S矩阵主对角线上的元素称为矩阵M的奇异值，其他元素都为0.
2.奇异值的应用
    可以根据奇异值，逆推原矩阵，跟特征值的作用相似，不同的是奇异值可以提取非方阵，特征值的提取
    必须是方阵
3.获取奇异值
    使用numpy.linalg.svd(M, full_matrices=False)方法，返回三个矩阵U，S，V，但是S是一个一维数组（就是奇异值）
    full_matrices=False:是否返回完全的方阵
"""
import numpy as np

M = np.mat("4 11 14; 8 7 -2")
print(M)

# 奇异值分解
U, S, V = np.linalg.svd(M, full_matrices=False)

# 如果不是设置 full_matrices=False 则函数返回的U，V就是方阵
# U, S, V = np.linalg.svd(M)
print(U * U.T)
print(V * V.T)
print(S)

S = np.diag(S)
print(S)
print(U * S * V)


