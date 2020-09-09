# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
# print(df.describe())
# print(df.head(3))
# print(df[['animal', 'age']])

# 8. 选择['animal', 'age']的 [3, 4, 8]行
# print(df[['animal', 'age']].iloc[[3, 4, 8]])
# print(df.index[[3, 4, 8]])
# print(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])


# print(type())
"""
问题：df['visits'] > 2 返回的是Series数据类型，而掩码获取数据需要传递列表
"""

# 9. 选择visits大于 2的数据
# print(df.iloc[list(df['visits'] > 2), :])
# print(df.query('visits > 2'))

# 10. 选择有缺失值的行, i.e. is NaN.
# print(df.query('age == "NaN"'))
# print(df[df['age'].isnull()])

# 11. 选择 animal 是cat和age小于3.
# 单=是赋值，双==才是判别
# print(df.query('animal == "cat"').query('age < 3'))

# 12. 选择 age is between 2 and 4 (inclusive)的行
# print(df.query('2 <= age <= 4'))

# 13.将age里的'f'改成1.5.
# print(df)
# df.loc['f', 'age'] = 1.5
# df.at['f', 'age'] = 1.5
# print(df)

# 14.计算visits的和 (the total number of visits).
# print(df['visits'].sum())

# 15.计算每一个动物的平均年龄
# print(df.groupby('animal')['age'].mean())

# 16.添加新的一行 'k' ，数据自己填，然后再将此行删除返回原数据框
# df.loc['k'] = ['dog', 5, 2, 'no']
# print(df)
# df = df.drop('k')
# print(df)

# 17.对每个动物的数量进行计数
# print(df['animal'].value_counts())

# 18.对df按照age降序、visit升序进行排序
# print(df.sort_values(['age', 'visits'], ascending=[False, True]))
# print(df.sort_values(['visits', 'age'], ascending=[False, True]))

# 19.'priority' 列包含值 'yes' 和'no'. 使用布尔值对这列进行替换: 'yes' 替换成 True
# ， 'no' 替换成 False.
# df['priority'] = df['priority'].replace(['yes', 'no'], [True, False])
# df['priority'] = df['priority'].map({'yes': True, 'no': False})
# print(df)

# 20. 在'animal' 列, 将'snake' 替换成 'python'.
# df['animal'] = df['animal'].replace('snake', 'python')
# print(df)

# 21.
# r = df.pivot_table(values='age', index='animal', columns='visits', aggfunc='mean')
# print(r)

# df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
# df = df.drop_duplicates(subset='A', keep='last')
#
# print(df)

# 22.给定一个由数值型数据组成的数据框：
# df = pd.DataFrame(np.random.random(size=(5, 3)))
# # a 5x3 frame of float values
# 如何从行中的每个元素中减去行的平均值？

# df1 = pd.DataFrame(np.random.random(size=(5, 3)))
#
# print(df1)
# print(df1.mean(axis=1))
# print(df1.sub(df1.m

# 24.给定一个10列由数值组成的数据框：
# df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
# 哪一列的总和最小? (找出那一列的标签。)

# df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
# print(df.index(df.min(df.sum(axis=1))))
# print(df.sum().idxmin())
# 获取所有的列标，行标
# print(df.columns)
# print(df.indexed)

# 25.如何计算一个数据框有多少个唯一的行（即忽略所有重复的行）？
df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print(len(df.drop_duplicates(keep='first')))
