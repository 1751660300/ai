# -*- coding:utf-8 -*-
import numpy as np

data = [("张三1", [78, 56, 92], 18), ("李四", [68, 72, 88], 15)]
# 第一种设置dtype的方式
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
print(a[0]['f0'], ":", a[0]['f1'])
print("=====================================")
# 第二种设置dtype的方式
b = np.array(data, dtype=[('name', 'str_', 2),
                          ('scores', '(3,)int32'),
                          ('age', '(1,)int32')])
print(b[0]['name'], ":", b[0]['scores'])
print("=====================================")

# 第三种设置dtype的方式
c = np.array(data, dtype={'names': ['name', 'scores', 'ages'],
                          'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'], ":", c[0]['scores'], ":", c.itemsize)
print("=====================================")

# 第四种设置dtype的方式
# 元组中的数字表示从第几个字节开始
d = np.array(data, dtype={'names': ('U3', 0),
                          'scores': ('3i4', 12),
                          'age': ('i4', 24)})
print(d[0]['names'], d[0]['scores'], d.itemsize)

print("=====================================")

# 测试日期类型数组
f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01', '2011-02-01'])
f = f.astype('M8[D]')
print(f)
f = f.astype('i4')
print(f[3] - f[0])
