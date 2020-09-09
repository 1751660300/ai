# -*- coding:utf-8 -*-
import pandas as pd

data = pd.DataFrame({"name": ['zs', 'ls', 'ww', 'zl'], 'sex': ['nan', 'nv', 'nan', 'nv'],
                     'age': [10, 8, 45, 20]})
print(data)
print(data.axes)
print(data.empty)
print(data.size)
print(data.values, type(data.values))
print(data.head(2))
print(data.tail(2))
print(data.ndim)
print(data.describe())
print(data.describe(include=['object']))
print(data.describe(include=['number']))
print(data.describe(include=['object', 'number']))



