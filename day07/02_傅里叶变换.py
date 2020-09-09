# -*- coding:utf-8 -*-
"""
一、什么是傅里叶定理
    任何一条周期曲线，无论多么跳跃或不规则，都可以表示成一组光滑的正弦曲线叠加而成

二、傅里叶变换
    就是根据傅里叶变换，将一条周期曲线拆解成一组光滑正弦曲线

三、numpy中傅里叶变换的api
    导入numpy中傅里叶包
    import numpy.fft as nf

    1.freqs = nf.fftfreq(采样数量, 采样周期)
    通过采样数与采样周期求得傅里叶变换分解所得的曲线的频率序列

    2.nf.fft(原函数值序列)
    通过原函数值的序列经过傅里叶变换得到一个复数数组，复数的模代表的是振幅，复数的辐角代表初相位

    3.nf.ifft()
    通过一个复数数组经过逆向傅里叶变换得到一个合成的函数值数组
"""
import numpy.fft as nf
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 4 * np.pi, num=1000)
# y = np.zeros(1000)
y = 4 * np.pi * np.sin(x)
for i in range(2, 10001):
    y += 4 / (2 * i - 1) * np.pi * np.sin((2 * i - 1) * x)
mp.subplot(121)
# mp.plot(x, y, label='fang bo')

req = nf.fft(y)
y_ = nf.ifft(req)
mp.plot(x, y, label='fang bo', color='red')

mp.subplot(122)
freq = nf.fftfreq(y_.size, x[1] - x[0])
power = np.abs(req)
mp.plot(freq, power, label='freq', color='red')
mp.legend()
mp.show()
