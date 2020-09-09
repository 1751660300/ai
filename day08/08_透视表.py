# -*- coding:utf-8 -*-
import pandas as pd

"""

"""

data = pd.DataFrame({'uid': [1, 2, 3, 4, 6],
                     'name': ['zs', 'ls', 'ww', 'zl', 'tq'],
                     'age': [10, 24, 54, 51, 15],
                     'sex': ['f', 'm', 'm', 'f', 'm']})
data1 = pd.DataFrame({'uid': [1, 2, 3, 4, 5], 'class': ['a', 'a', 'c', 'b', 'c']})
table = pd.merge(data, data1, how='inner')

r = table.pivot_table(index='sex', values='age', aggfunc='max')
print(r)

r = table.pivot_table(index=['class', 'sex'], values=['age', 'uid'], aggfunc='max', margins=True)
print(r)

print(r.info())

# from lxml import html
# d = html.etree.HTML("<p>hahah</p>")
# print(d.xpath("//p/text()"))
