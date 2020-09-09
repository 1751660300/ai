# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as mpl


x = np.linspace(0, 4 * np.pi, num=1000)
y1 = np.sin(x)
y2 = np.cos(x / 2) + 1
mpl.figure('fill', facecolor='lightgray')
mpl.plot(x, y1, label='sinx')
mpl.plot(x, y2, label=r'$cos\frac{x}{2}$')
mpl.xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi], ['0', '$\pi$', '$2\pi$', '$3\pi$', '$4\pi$'])
mpl.legend(loc='best')
mpl.fill_between(
    x, y1, y2,
    y1 > y2,
    color='red',
    alpha=0.5
)

mpl.show()
