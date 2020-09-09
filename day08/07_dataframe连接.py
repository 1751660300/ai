# -*- coding:utf-8 -*-
import pandas as pd
"""
使用merge()方法可以实现两个数据的连接，类似数据库表的连接
data.merge(data1, how="")
how的参数见图片
"""

data = pd.DataFrame({'uid': [1, 2, 3, 4, 6], 'name': ['zs', 'ls', 'ww', 'zl', 'tq']})
data1 = pd.DataFrame({'uid': [1, 2, 3, 4, 5], 'class': ['a', 'a', 'c', 'b', 'c']})
# 内连接
res = data.merge(data1, how="inner")
print(res)

# 外全连接
res = data.merge(data1, how="outer")
print(res)

res = data.merge(data1, how="left")
print(res)

res = data.merge(data1, how="right")
print(res)
