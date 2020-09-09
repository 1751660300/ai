# -*- coding:utf-8 -*-
import pandas as pd
"""
pandas有两种排序方法，分别是按标签和按实际值来排
1. 按行标签来排序
    使用sort_index()方法，通过传递axis参数和排序顺序，可以对dataframe进行排序，默认是升序
    axis=1 表示按列标签排序
    axis=0 按行标签排序

2.按某列值来排序
    使用sort_values()方法，传递一个列名
"""
data = pd.DataFrame({"name": ['zs', 'ls', 'ww', 'zl'], 'sex': ['nan', 'nv', 'nan', 'nv'],
                     'age': [10, 8, 45, 20]})

print(data)

# 1. 按行标签来排序
print(data.sort_index(axis=1, ascending=False))

# 2. 按某列值来排序
print(data.sort_values('age'))
# 先按age排，然后按sex排
print(data.sort_values(['age', 'sex']))

print(data.groupby('sex'), type(data.groupby('sex')))
print(data.groupby('sex').mean())

group = data.groupby('sex')
for i, j in group:
    print(i, j)
