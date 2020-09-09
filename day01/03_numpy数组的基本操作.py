# -*- coding:utf-8 -*-
import numpy as np
# 创建数组
data = np.arange(0, 10)

# 数组的维度
print("data的维度是：{}列{}行".format(data.shape[0], data.shape[1] if (len(data.shape)) > 1 else 1))

# 元素的类型
print("元素的类型：%s" % data.dtype)

# 数组中元素的个数
print("数组中元素的个数：{}个".format(data.size))

# 数组下标从0开始
print("data第一个元素是：{}".format(data[0]))

# 问题：三元运算符
# x = 1 if y > 0 else x = 0