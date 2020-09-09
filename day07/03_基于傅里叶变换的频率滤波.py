# -*- coding:utf-8 -*-
"""
1. 含噪信号是高能信号与低能信号叠加的信号，可以通过傅里叶变换的频率滤波来实现降噪
2. 通过fft使含噪信号转换为频谱，去掉低能频谱，在使用ifft留下高能信号
"""
import numpy as np
import numpy.fft as nf
from pydub import AudioSegment
import scipy.io.wavfile as siw
import matplotlib.pyplot as mp

# 读取音频信息
audio = AudioSegment.from_file('data/1.m4a', format='m4a')
print(audio.frame_rate)

# audio.get_array_of_samples() 获取音频的数组数据
y = np.array(audio.get_array_of_samples())/1000
print('y的维度是：', y.shape)

x = np.linspace(0, 1000, num=len(y))
mp.subplot(221)
mp.plot(x, y, label='1.m4a', color='pink')

mp.subplot(222)

# 将原函数值经过傅里叶变换得到复数数组
res = nf.fft(y)

# 根据采样数量和采样周期求得曲线的频率序列
freq = nf.fftfreq(len(y), x[1]-x[0])
print('频率序列为：', freq)
power = np.abs(res)
mp.plot(freq[freq > 0], power[freq > 0], label='1.m4a', color='pink')
mp.legend()
res[power < 1800] = 0

mp.subplot(224)
power = np.abs(res)
mp.plot(freq[freq > 0], power[freq > 0], label='1.m4a', color='pink')

mp.subplot(223)
y_ = nf.ifft(res).real
mp.plot(x, y_, color='green', label='clean sound')


siw.write('new.wav', audio.frame_rate * 2, (y_*1000).astype(np.int16))
newa = audio._spawn((y_*1000).astype(np.int16))
# newa.export('newa.wav', format='wav')
mp.show()
