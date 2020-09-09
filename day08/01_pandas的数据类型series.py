# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
"""
一、 Series
    可以理解为一个数组，只是index名可以改动。类似与有序字典，有index和value
    
    1. 创建一个空的Series
    series = pd.Series()
    
    2.从ndarray创建一个Series,并且指定行级标签
    data = np.arange(1, 10)
    series2 = pd.Series(data, index=[chr(i) for i in range(ord('a'), ord('a')+9)])
    
    3.从字典创建一个Series
    dic = {'a': 1, 'b': 2, 'c': 3}
    series3 = pd.Series(dic)
    
    4.从变量创建一个series
    series4 = pd.Series(1, range(5))
    
二、访问series中的数据
    
    5.通过索引检索元素
    print(series3[1])
    print(series3[1:])
    
    6.通过行级标签访问数据
    print(series3['a'])
    print(series3[['a', 'c']])
"""
# 1创建一个空的Series
# series = pd.Series()

# 2 从ndarray创建一个Series,并且指定行级标签
data = np.arange(1, 10)
series2 = pd.Series(data, index=[chr(i) for i in range(ord('a'), ord('a')+9)])
print(series2)

# 3 从字典创建一个Series
dic = {'a': 1, 'b': 2, 'c': 3}
series3 = pd.Series(dic)
print(series3)

# 4 从变量创建一个series
series4 = pd.Series(1, range(5))
print(series4)

# 5
print(series3[1])
print(series3[1:])

# 6
print(series3['a'])
print(series3[['a', 'c']])
