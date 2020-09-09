## 三、matplotlib概述

matplotlib是python的一个绘图库。使用它可以很方便的绘制出版质量级别的图形。

### 1. matplotlib基本功能

1. 基本绘图 （在二维平面坐标系中绘制连续的线）
   1. 设置线型、线宽和颜色  
   2. 设置坐标轴范围
   3. 设置坐标刻度
   4. 设置坐标轴
   5. 图例
   6. 特殊点
   7. 备注
2. 图形对象(图形窗口)
   1. 子图
   2. 刻度定位器
   3. 刻度网格线
   4. 半对数坐标
   5. 散点图
   6. 填充
   7. 条形图
   8. 饼图
   9. 等高线图
   10. 热成像图
   11. 三维曲面
   12. 简单动画



## 四、matplotlib基本功能详解

### 1. 基本绘图

#### 1）绘图核心API

案例： 绘制简单直线

```python
import numpy as np
import matplotlib.pyplot as mp

# 绘制简单直线
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 9, 12, 15])`

mp.plot(x, y)
mp.show() # 显示图片，阻塞方法
```

![](C:/Users/xuming/Desktop/code1911/images/%E7%9B%B4%E7%BA%BF.png)

#### 2）设置线型、线宽

效果：

![](C:/Users/xuming/Desktop/code1911/images/sin_cos%E6%9B%B2%E7%BA%BF.png)



linestyle: 设置线型，常见取值有实线（'-'）、虚线（'--'）、点虚线（'-.'）、点线（':'）

linewidth：线宽

color：颜色（red, blue, green）（#aabbcc）(0.8, 0.4, 0.6, 0.9)

alpha: 设置透明度（0~1之间）



案例：绘制正弦、余弦曲线，并设置线型、线宽、颜色、透明度

```python
# 绘制正弦曲线
import numpy as np
import matplotlib.pyplot as mp
import math

x = np.arange(0, 2 * np.pi, 0.1)  # 以0.1为单位，生成0~6的数据
print(x)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
mp.plot(x, y1, label="sin", linewidth=2)  # 实线，线宽2像素
mp.plot(x, y2, label="cos", linestyle="--", linewidth=4)  # 虚线，线宽4像素

mp.xlabel("x")  # x轴文字
mp.ylabel("y")  # y轴文字

# 设置坐标轴范围
mp.xlim(0, 2 * math.pi)
mp.ylim(-1, 2)

mp.title("sin & cos")  # 图标题
mp.legend()  # 图例
mp.show()
```

#### 3）设置坐标刻度

效果：

![](C:/Users/xuming/Desktop/20.02%E7%A0%94%E5%8F%91/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/images/%E4%B8%80%E5%85%83%E4%BA%8C%E6%AC%A1%E6%9B%B2%E7%BA%BF.png)

语法：

```python
#x_val_list: 	x轴刻度值序列
#x_text_list:	x轴刻度标签文本序列 [可选]
mp.xticks(x_val_list , x_text_list )
#y_val_list: 	y轴刻度值序列
#y_text_list:	y轴刻度标签文本序列 [可选]
mp.yticks(y_val_list , y_text_list )
```

案例：绘制二次函数曲线

```python
# 绘制二次函数曲线
import numpy as np
import matplotlib.pyplot as mp
import math

x = np.arange(-5, 5, 0.1)  # 以0.1为单位，生成-5~5的数据
print(x)
y = x ** 2

# 绘制图形
mp.plot(x, y, label="$y = x ^ 2$",
         linewidth=2,  # 线宽2像素
         color="red",  # 颜色
         alpha=0.5)  # 透明度

mp.xlabel("x")  # x轴文字
mp.ylabel("y")  # y轴文字

# 设置坐标轴范围
mp.xlim(-10, 10)
mp.ylim(-1, 30)

# 设置刻度
x_tck = np.arange(-10, 10, 2)
x_txt = x_tck.astype("U")
mp.xticks(x_tck, x_txt)

y_tck = np.arange(-1, 30, 5)
y_txt = y_tck.astype("U")
mp.yticks(y_tck, y_txt)

mp.title("square")  # 图标题
mp.legend(loc="upper right")  # 图例 upper right, center
mp.show()
```

***刻度文本的特殊语法*** -- *LaTex排版语法字符串*

```python
r'$x^n+y^n=z^n$',   r'$\int\frac{1}{x} dx = \ln |x| + C$',     r'$-\frac{\pi}{2}$'
```

$$
x^n+y^n=z^n,  \int\frac{1}{x} dx = \ln |x| + C,     -\frac{\pi}{2}
$$

#### 4）设置坐标轴  

效果：

![](C:/Users/xuming/Desktop/20.02%E7%A0%94%E5%8F%91/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/images/%E5%9D%90%E6%A0%87%E8%BD%B4%E6%A0%BC%E5%BC%8F.png)

坐标轴名：left / right / bottom / top

```python
# 获取当前坐标轴字典，{'left':左轴,'right':右轴,'bottom':下轴,'top':上轴 }
ax = mp.gca()
# 获取其中某个坐标轴
axis = ax.spines['坐标轴名']
# 设置坐标轴的位置。 该方法需要传入2个元素的元组作为参数
# type: <str> 移动坐标轴的参照类型  一般为'data' (以数据的值作为移动参照值)
# val:  参照值
axis.set_position(('data', val))
# 设置坐标轴的颜色
# color: <str> 颜色值字符串
axis.set_color(color)
```

案例：设置坐标轴格式

```python
# 设置坐标轴
import matplotlib.pyplot as mp

ax = mp.gca()
axis_b = ax.spines['bottom']  # 获取下轴
axis_b.set_position(('data', 0))  # 设置下轴位置, 以数据作为参照值

axis_l = ax.spines['left']  # 获取左轴
axis_l.set_position(('data', 0))  # 设置左轴位置, 以数据作为参照值

ax.spines['top'].set_color('none')  # 设置顶部轴无色
ax.spines['right'].set_color('none')  # 设置右部轴无色

mp.show()
```

#### 5）图例

显示两条曲线的图例，并测试loc属性。

```python
# 再绘制曲线时定义曲线的label
# label: <关键字参数 str> 支持LaTex排版语法字符串
mp.plot(xarray, yarray ... label='', ...)
# 设置图例的位置
# loc: <关键字参数> 制定图例的显示位置 (若不设置loc，则显示默认位置)
#	 ===============   =============
#    Location String   Location Code
#    ===============   =============
#    'best'            0
#    'upper right'     1
#    'upper left'      2
#    'lower left'      3
#    'lower right'     4
#    'right'           5
#    'center left'     6
#    'center right'    7
#    'lower center'    8
#    'upper center'    9
#    'center'          10
#    ===============   =============
mp.legend(loc='')
```

#### 6）特殊点

效果：

![](C:/Users/xuming/Desktop/20.02%E7%A0%94%E5%8F%91/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/images/%E7%89%B9%E6%AE%8A%E7%82%B9.png)

语法：

```python
# xarray: <序列> 所有需要标注点的水平坐标组成的序列
# yarray: <序列> 所有需要标注点的垂直坐标组成的序列
mp.scatter(xarray, yarray, 
           marker='', 		#点型 ~ matplotlib.markers
           s=80, 			#大小
           edgecolor='', 	#边缘色
           facecolor='',	#填充色
           zorder=3			#绘制图层编号 （编号越大，图层越靠上）
)

```

示例：在二次函数图像中添加特殊点

```python
# 绘制特殊点
mp.scatter(x_tck,  # x坐标数组
            x_tck ** 2,  # y坐标数组
            marker="s",  # 点形状 s:square
            s=40,  # 大小
            facecolor="blue",  # 填充色
            zorder=3)  # 图层编号
```

*marker点型可参照：help(matplotlib.markers)*

*也可参照附录： matplotlib point样式*



#### 7）备注

效果：

![](C:/Users/xuming/Desktop/code1911/images/%E6%B7%BB%E5%8A%A0%E5%A4%87%E6%B3%A8.png)

语法：

```python
# 在图表中为某个点添加备注。包含备注文本，备注箭头等图像的设置。
mp.annotate(
    r'$\frac{\pi}{2}$',			#备注中显示的文本内容
    xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(x, y),	 				#备注目标点的坐标
    textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(x, y),				#备注文本的坐标
    fontsize=14,				#备注文本的字体大小
    arrowprops=dict()			#使用字典定义文本指向目标点的箭头样式
)
```

arrowprops参数使用字典定义指向目标点的箭头样式

```python
#arrowprops字典参数的常用key
arrowprops=dict(
	arrowstyle='',		#定义箭头样式
    connectionstyle=''	#定义连接线的样式
)

```

箭头样式（arrowstyle）字符串如下

```
============   =============================================
Name           Attrs
============   =============================================
  '-'          None
  '->'         head_length=0.4,head_width=0.2
  '-['         widthB=1.0,lengthB=0.2,angleB=None
  '|-|'        widthA=1.0,widthB=1.0
  '-|>'        head_length=0.4,head_width=0.2
  '<-'         head_length=0.4,head_width=0.2
  '<->'        head_length=0.4,head_width=0.2
  '<|-'        head_length=0.4,head_width=0.2
  '<|-|>'      head_length=0.4,head_width=0.2
  'fancy'      head_length=0.4,head_width=0.4,tail_width=0.4
  'simple'     head_length=0.5,head_width=0.5,tail_width=0.2
  'wedge'      tail_width=0.3,shrink_factor=0.5
============   =============================================

```

连接线样式（connectionstyle）字符串如下

```
============   =============================================
Name           Attrs
============   =============================================
  'angle' 		angleA=90,angleB=0,rad=0.0
  'angle3' 		angleA=90,angleB=0`   
  'arc'			angleA=0,angleB=0,armA=None,armB=None,rad=0.0
  'arc3' 		rad=0.0
  'bar' 		armA=0.0,armB=0.0,fraction=0.3,angle=None
============   =============================================


```

示例：在二次函数图像中添加备注

```python
# 设置备注
mp.annotate(
    r'$y = x ^ 2$',			#备注中显示的文本内容
    xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(4, 16),	 				#备注目标点的坐标 (4,16)
    textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(20, 30),				#备注文本的坐标
    fontsize=14,				#备注文本的字体大小
    arrowprops=dict(
        arrowstyle="->", connectionstyle="angle3"
    )			#使用字典定义文本指向目标点的箭头样式
)
```

### 2. 图形对象（图形窗口）

语法：绘制两个窗口，一起显示。

```python
# 手动构建 matplotlib 窗口
mp.figure(
    'sub-fig',			#窗口标题栏文本 
	facecolor=''		#图表背景色
)
mp.show()
```

mp.figure方法可以构建一个新窗口。plot方法将会针对刚构建的新窗口进行绘制。如果创建多个窗口，则需要多次调用figure方法即可。figure方法中的第一个参数（标题栏文本）相当于窗口的唯一标识符， 同一个标题的窗口只能创建一次。若使用figure方法构建了已存在标题的窗口的话，matplotlib将会把该窗口置为当前操作窗口，而后进行绘制。

**设置当前窗口的参数**

语法：测试窗口相关参数

```python
# 设置图表标题 显示在图表上方
mp.title(title, fontsize=12)
# 设置水平轴的文本
mp.xlabel(x_label_str, fontsize=12)
# 设置垂直轴的文本
mp.ylabel(y_label_str, fontsize=12)
# 设置图表网格线  linestyle设置网格线的样式
	#	-  or solid 粗线
	#   -- or dashed 虚线
	#   -. or dashdot 点虚线
	#   :  or dotted 点线
mp.grid(linestyle='')
# 设置紧凑布局，把图表相关参数都显示在窗口中
mp.tight_layout() 
```

示例：绘制两个图像窗口

```python
# 绘制两个图像窗口
import matplotlib.pyplot as mp

mp.figure("FigureA", facecolor="lightgray")
mp.grid(linestyle="-.")  # 设置网格线

mp.figure("FigureB", facecolor="gray")
mp.xlabel("Date", fontsize=14)
mp.ylabel("Price", fontsize=14)
mp.grid(linestyle="--")  # 设置网格线
mp.tight_layout()  # 设置紧凑布局

mp.show()
```

执行结果：

![](C:/Users/xuming/Desktop/code1911/images/%E4%B8%A4%E4%B8%AA%E7%AA%97%E5%8F%A3.png)

#### 1）子图

**矩阵式布局**

效果：

![](C:/Users/xuming/Desktop/20.02%E7%A0%94%E5%8F%91/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/images/9%E4%B8%AA%E5%AD%90%E5%9B%BE.png)



绘制矩阵式子图布局相关API：

```python
mp.figure('Subplot Layout', facecolor='lightgray')
# 拆分矩阵
	# rows:	行数
    # cols:	列数
    # num:	编号
mp.subplot(rows, cols, num)
	#	1 2 3
	#	4 5 6
	#	7 8 9 
mp.subplot(3, 3, 5)		#操作3*3的矩阵中编号为5的子图
mp.subplot(335)			#简写

```

案例：绘制9宫格矩阵式子图，每个子图中写一个数字。

```python
mp.figure('Subplot Layout', facecolor='lightgray')

for i in range(9):
	mp.subplot(3, 3, i+1)
	mp.text(
		0.5, 0.5, i+1, 
		ha='center',
		va='center',
		size=36,
		alpha=0.5,
		withdash=False
	)
	mp.xticks([])
	mp.yticks([])

mp.tight_layout()
mp.show()

```

**网格式布局(很少使用)**

网格式布局支持单元格的合并。

绘制网格式子图布局相关API：

```python
import matplotlib.gridspec as mg
mp.figure('Grid Layout', facecolor='lightgray')
# 调用GridSpec方法拆分网格式布局
# rows:	行数
# cols:	列数
# gs = mg.GridSpec(rows, cols)	拆分成3行3列
gs = mg.GridSpec(3, 3)	
# 合并0行与0、1列为一个子图表
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()

```

案例：绘制一个自定义网格布局。

```python
import matplotlib.gridspec as mg
mp.figure('GridLayout', facecolor='lightgray')
gridsubs = mp.GridSpec(3, 3)
# 合并0行、0/1列为一个子图
mp.subplot(gridsubs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36)
mp.tight_layout()
mp.xticks([])
mp.yticks([])

```

**自由式布局(很少使用)**

自由式布局相关API：

```python
mp.figure('Flow Layout', facecolor='lightgray')
# 设置图标的位置，给出左下角点坐标与宽高即可
# left_bottom_x: 坐下角点x坐标
# left_bottom_x: 坐下角点y坐标
# width:		 宽度
# height:		 高度
# mp.axes([left_bottom_x, left_bottom_y, width, height])
mp.axes([0.03, 0.03, 0.94, 0.94])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()

```

案例：测试自由式布局，定位子图。

```python
mp.figure('FlowLayout', facecolor='lightgray')

mp.axes([0.1, 0.2, 0.5, 0.3])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36)
mp.show()

```

#### 2）刻度定位器

执行结果：

![主刻度次刻度](C:/Users/xuming/Desktop/20.02%E7%A0%94%E5%8F%91/%E7%AC%AC%E4%BA%94%E9%98%B6%E6%AE%B5%E8%AF%BE%E5%A0%82%E8%B5%84%E6%96%99/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/images/%E4%B8%BB%E5%88%BB%E5%BA%A6%E6%AC%A1%E5%88%BB%E5%BA%A6.png)



刻度定位器相关API：

```python
# 获取当前坐标轴
ax = mp.gca()
# 设置水平坐标轴的主刻度（显示字的刻度）定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
# 设置水平坐标轴的次刻度（不显示字的刻度）定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

```

案例：绘制一个数轴，每隔1一个主刻度，每隔0.1一个次刻度。

```python
import matplotlib.pyplot as mp

mp.figure('Locators', facecolor='lightgray')
# 获取当前坐标轴
ax = mp.gca()

# 隐藏除底轴以外的所有坐标轴
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 将底坐标轴调整到子图中心位置
ax.spines['bottom'].set_position(('data', 0))
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

mp.xlim(1, 5)
# 标记所用刻度定位器类名
mp.text(5, 0.3, 'NullLocator()', ha='center', size=12)

mp.show()
```

常用刻度器如下：

```python
# 空定位器：不绘制刻度
mp.NullLocator()
# 最大值定位器：
# 最多绘制nbins+1个刻度
mp.MaxNLocator(nbins=3)
# 定点定位器：根据locs参数中的位置绘制刻度
mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])
# 自动定位器：由系统自动选择刻度的绘制位置
mp.AutoLocator()
# 索引定位器：由offset确定起始刻度，由base确定相邻刻度的间隔
mp.IndexLocator(offset=0.5, base=1.5)
# 多点定位器：从0开始，按照参数指定的间隔(缺省1)绘制刻度
mp.MultipleLocator()
# 线性定位器：等分numticks-1份，绘制numticks个刻度
mp.LinearLocator(numticks=21)
# 对数定位器：以base为底，绘制刻度
mp.LogLocator(base=2)
```

案例：使用for循环测试刻度器样式：

```python
import matplotlib.pyplot as mp
import numpy as np

locators = ['mp.NullLocator()', # 空刻度定位器，不绘制刻度
            'mp.MultipleLocator(1)', # 多点定位器：从0开始，按照参数指定的间隔(缺省1)绘制
            'mp.MaxNLocator(nbins=4)',# 最多绘制指定个数+1个主刻度
            'mp.AutoLocator()'] # 自动定位器：由系统自动选择刻度的绘制位置

for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1)
    mp.xlim(0, 10)
    mp.ylim(-1, 1)
    mp.yticks([])
    # 获取当前坐标轴
    ax = mp.gca()
    # 隐藏除底轴以外的所有坐标轴
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # 将底坐标轴调整到子图中心位置
    ax.spines['bottom'].set_position(('data', 0))
    # 设置水平坐标轴的主刻度定位器
    ax.xaxis.set_major_locator(eval(locator))
    # 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
    mp.plot(np.arange(11), np.zeros(11), c='none')
    # 标记所用刻度定位器类名
    mp.text(5, 0.3, locator, ha='center', size=12)

mp.show()
```

执行结果：

![](C:/Users/xuming/Desktop/code1911/images/%E5%A4%9A%E4%B8%AA%E5%88%BB%E5%BA%A6%E5%AE%9A%E4%BD%8D%E5%99%A8.png)

#### 3）条形图（柱状图）

绘制柱状图的相关API：

```python
mp.figure('Bar', facecolor='lightgray')
mp.bar(
	x,				# 水平坐标数组
    y,				# 柱状图高度数组
    width,			# 柱子的宽度
    color='', 		# 填充颜色
    label='',		#
    alpha=0.2		#
)
```

案例：先以柱状图绘制苹果12个月的销量，然后再绘制橘子的销量。

```python
import matplotlib.pyplot as mp
import numpy as np

apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])

mp.figure('Bar', facecolor='lightgray')
mp.title('Bar', fontsize=20)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.ylim((0, 40))

x = np.arange(len(apples))  # 产生均匀数组，长度等同于apples

mp.bar(x - 0.2,  # 横轴数据
       apples,  # 纵轴数据
       0.4,  # 柱体宽度
       color='dodgerblue',
       label='Apple')
mp.bar(x + 0.2,  # 横轴数据
       oranges,  # 纵轴数据
       0.4,  # 柱体宽度
       color='orangered', label='Orange', alpha=0.75)

mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

mp.legend()
mp.show()
```

#### 

#### 3）散点图

可以通过每个点的坐标、颜色、大小和形状表示不同的特征值。

| 身高 | 体重 | 性别 | 年龄段 | 种族 |
| ---- | ---- | ---- | ------ | ---- |
| 180  | 80   | 男   | 中年   | 亚洲 |
| 160  | 50   | 女   | 青少   | 美洲 |

绘制散点图的相关API：

```python
mp.scatter(
    x, 					# x轴坐标数组
    y,					# y轴坐标数组
    marker='', 			# 点型
    s=10,				# 大小
    color='',			# 颜色
    edgecolor='', 		# 边缘颜色
    facecolor='',		# 填充色
    zorder=''			# 图层序号
)

```

numpy.random提供了normal函数用于产生符合 正态分布 的随机数 

```python
n = 100
# 172:	期望值
# 10:	标准差
# n:	数字生成数量
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)

```

案例：绘制平面散点图。

```python
# 散点图示例
import matplotlib.pyplot as mp
import numpy as np

n = 40
# 期望值：期望值是该变量输出值的平均数
# 标准差：是反映一组数据离散程度最常用的一种量化形式，是表示精确度的重要指标
x = np.random.normal(172, 20 ,n ) # 期望值, 标准差, 生成数量
y = np.random.normal(60, 10, n) # 期望值, 标准差, 生成数量

x2 = np.random.normal(180, 20 ,n ) # 期望值, 标准差, 生成数量
y2 = np.random.normal(70, 10, n) # 期望值, 标准差, 生成数量

mp.figure("scatter", facecolor="lightgray")
mp.title("Scatter Demo")
mp.scatter(x, y, c="red", marker="D")
mp.scatter(x2, y2, c="blue", marker="v")

mp.xlim(100, 240)
mp.ylim(0, 100)
mp.show()
```

执行结果：

![](C:/Users/xuming/Desktop/code1911/images/%E6%95%A3%E7%82%B9%E5%9B%BE%E7%A4%BA%E4%BE%8B.png)

*cmap颜色映射表参照附件：cmap颜色映射表*

#### 