# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=1000)
y = np.sin(x)
# 绘制图形
mpl.plot(x, y, label="sin(x)")
# 设置图标题
mpl.title(r'sin(x)')
# 图例
mpl.legend(loc="upper right")  # 图例 upper right, center
# 获取坐标轴
axis = mpl.gca()
top = axis.spines["top"]
top.set_color(None)
axis.spines["right"].set_color(None)
axis.spines["left"].set_position(('data', 0))
axis.spines["bottom"].set_position(('data', 0))

# 设置特殊点
mpl.scatter(
    [0],
    [0],
    marker='.',
    s=10,
    edgecolors='red',
    facecolor='red',
    zorder=3
)
# 设置备注
mpl.annotate(
    r'$\frac{\pi}{2}$',  # 备注中显示的文本内容
    xycoords='data',  # 备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(np.pi/2, 1),  # 备注目标点的坐标
    textcoords='offset points',  # 备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(10, 10),  # 备注文本的坐标
    fontsize=14,  # 备注文本的字体大小
    arrowprops={'arrowstyle': '->', 'connectionstyle': 'angle'}  # 使用字典定义文本指向目标点的箭头样式
)
mpl.tight_layout()
mpl.show()
