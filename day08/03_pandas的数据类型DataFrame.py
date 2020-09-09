# -*- coding:utf-8 -*-
import pandas as pd
"""
一、DataFrame
    DataFrame是一个类似表格的数据类型，可以理解为是一个二维数组，索引有两个维度，可以更改。
    特点：
     潜在的列是不同的数据类型
     大小可变
     标记轴（行和列）
     可对行和列执行算术运算
    
    1.创建空的DataFrame
    
"""
# 1.创建空的DataFrame
data = pd.DataFrame()
print(data, type(data))

# 2. 从列表创建dataframe
df = pd.DataFrame([1, 2, 3, 4, 5])
print(df)

# 3. 根据二维列表创建
df2 = pd.DataFrame([['bob', 12], ['jone', 20]], columns=['name', 'age'])
print(df2)

# 4. 根据字典创建, key: 为字段名称,必须要设置行级索引
df3 = pd.DataFrame({'bob': [12, 50, 80], 'jone': [202, 50, 80]}, index=['zs', 'ls', 'ww'])
print(df3)
