# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.image as mi

# 提取图片数据
original = mi.imread('lily.jpg', 'jpg')[:, :, 0]

# 转换为矩阵
original = np.mat(original)
# 提取奇异值
U, S, V = np.linalg.svd(original, full_matrices=False)
print(S.shape)
print(V.shape)
S[50:] = 0
S = np.diag(S)
data = U * S * V
print(data)
mp.imshow(data.real)
mp.show()
