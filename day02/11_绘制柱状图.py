# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

x = np.linspace(-np.pi, np.pi, num=20)
y = np.sin(x)
gs = mpl.GridSpec(2, 2)
mpl.subplot(gs[0, 0:2])
# 绘制图形
mpl.bar(
    x, y,
    width=0.08,
    color='red',
    label='柱状图'
)
ax = mpl.gca()
ax.spines["top"].set_color(None)
ax.spines["right"].set_color(None)
ax.spines["left"].set_position(('data', 0))
ax.spines["bottom"].set_position(('data', 0))

mpl.subplot(gs[1, 0:2])

# 散点图
mpl.scatter(
    x, y,
    marker='o',
    facecolor='red',
    s=5

)
mpl.savefig("柱状图和散点图.svg", format="svg")
mpl.show()
