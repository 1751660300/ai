# -*- coding:utf-8 -*-
import pandas as pd
"""
1. pandas识别的日期字符串格式
    使用pandas的to_datetime转换成日期
    date = pd.Series(['2020', '2020-7', '2020/7/22', '2020/7/22/ 10:40:00', '22 july 2020'])
    date = pd.to_datetime(date)

2. 日期运算
    datla = date - pd.to_datetime('2019')
    
3.dateTimeIndex
    通过指定周期和频率，使用date_range()函数可以创建日期序列，默认情况下频率是天
    datelist = pd.date_range('2020', periods=5)
    
    结果
    DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
               '2020-01-05'],
              dtype='datetime64[ns]', freq='D')
"""
# 1 pandas识别的日期字符串格式
date = pd.Series(['2020', '2020-7', '2020/7/22', '2020/7/22/ 10:40:00', '22 july 2020'])
print(date, date.dtype)

date = pd.to_datetime(date)
print(date, date.dtype)

# 2 日期运算
detla = date - pd.to_datetime('2019')
print(detla)
# 把detla转换成数字
print(detla.dt.days)

# 3 freq='D' 频率为天 ，freq='M' 频率为月
datelist = pd.date_range('2020', periods=5, freq='M')
print(datelist)
# 工作日序列,会除去星期六，星期天
print(pd.bdate_range('2020', periods=10))
# 构建区间的时间序列
print(pd.bdate_range('2020-1-5', '2020-1-10'))
