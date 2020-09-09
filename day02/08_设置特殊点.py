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
mpl.show()
