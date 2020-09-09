# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
b = np.linspace(-20, 20, 1000)
a = 5 * (b ** 2) + 1
x1 = np.array(b)
y1 = np.array(a / 20)
x2 = np.array(b)
y2 = np.array(4 * b + 1)

# 设置窗口
mpl.figure("A")
mpl.title("绘制函数图像")
mpl.xlabel("x")
mpl.ylabel("y")
# 设置图例

mpl.plot(x1, y1, label=r'$\frac{5*x^2+1}{50}$')
mpl.plot(x2, y2, label=r'$4*x+1$')
mpl.legend(loc='best')

# 设置坐标轴
axis = mpl.gca()
axis.spines["right"].set_color(None)
axis.spines["top"].set_color(None)
axis.spines["left"].set_position(('data', 0))
axis.spines["bottom"].set_position(('data', 0))
axis.xaxis.set_major_locator(mpl.MultipleLocator(10))
axis.xaxis.set_minor_locator(mpl.MultipleLocator(1))
# 设置特殊点
# 找到交点
import math

sy1 = y1[abs(y1 - y2) < 0.1]
sx1 = x1[abs(y1 - y2) < 0.1]
# sy1 = set(y1)
# sy2 = set(y2)
# res = sy1.intersection(sy2)
# print(list(sy1).count(True))
mpl.scatter(
    sx1,
    sy1,
    marker='^',
    facecolor='red',
    zorder=10
)
# 备注
mpl.annotate(
    "({},\n{})".format(sx1[0], sy1[0]),
    xytext=(50, -50),
    xy=(sx1[0], sy1[0]),
    textcoords="offset points",
    fontsize=15,
    arrowprops={
        'arrowstyle': "<|-|>",
        "connectionstyle": "arc3"
    }
)
mpl.annotate(
    "({},\n{})".format(sx1[1], sy1[1]),
    xytext=(-60, -70),
    xy=(sx1[1], sy1[1]),
    textcoords="offset points",
    fontsize=15,
    arrowprops={
        'arrowstyle': "<|-|>",
        "connectionstyle": "arc3"
    }
)
# 绘制图标的网格线
mpl.grid(linestyle=':')
# 保存为矢量图
mpl.tight_layout()
mpl.figure("B")
mpl.plot(x1, y1)
mpl.grid(".")
mpl.text(5, 2, "钱良虎", ha='center', size=15)
mpl.savefig(fname="name.svg", format="svg")
mpl.show()
# 问题
# 1.python的幂运算符号为：**
# 2.集合的运算
#     set.intersection() 交集
#     set.difference()  差集
#     set.union()   并集
# 3.如何计算绝对值
# abs()  内建函数
