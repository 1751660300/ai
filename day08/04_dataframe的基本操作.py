# -*- coding:utf-8 -*-
import pandas as pd
"""

"""

data = pd.DataFrame({'one': pd.Series([15, 45, 531]), 'two': pd.Series([45, 45, 42])})
print(data)

# 列访问
print(data["one"])
print(data[["one", "two"]])

# 列添加
data['three'] = pd.Series([123, 15, 45])
print(data)

# 删除列
del data['three']
print(data)

data.pop('one')
print(data)

# 行访问
# 切片的方式
print(data[0:1])
# 根据loc 和 iloc方法来访问
# loc只支持行级索引来访问
# iloc也支持下标索引
print(data.loc[0])
print(data.loc[[0, 1]])
print(data.iloc[[0, 1]])

# 行添加
data.loc[3] = 10
print(data)

# 行删除, 返回一个新的dataframe
data = data.drop(3)
print(data)
