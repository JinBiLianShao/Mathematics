# 第二章：函数
import numpy as np  # 计算
import math
import matplotlib.pyplot as plt  # 画图
import sympy as sp  # 函数库
import interval as iv  # 区间库

# 函数 ：由两个非空集合相互对应的一种表示（可一对一，多对一）
x = sp.symbols("x")  # 定义未知数x，x为非空集合中的一个未知元素。
y = sp.solve(x, x)  # 函数关系式，该方法是在函数等用0的时候参与运算求解，得到的结果为数组。
print(y)
x = np.arange(-5.0, 5.0, 0.1)  # 定义x的区间和表示单位
y = x  # 函数体
plt.plot(x, y)
plt.ylim(-10, 10)  # 定义y的区间
plt.show()

# 函数相等：如果两个函数定义域相同，对应关系完全一致，称这两个函数相等。
x1 = np.arange(-5.0, 5.0, 0.1)
x2 = np.arange(-5.0, 5.0, 0.1)
y1 = x1
y2 = pow(pow(x2, 2), 0.5)  # y2 = x2的平方开算术平方根，pow是算平方的内置方法
plt.plot(x1, y1)
plt.plot(x2, y2, linestyle="--")
plt.ylim(-10, 10)
plt.show()  # 如图所示，不是相等函数。

# 函数奇偶性：如上图可看出，y（-x）=-y(x)是奇函数，y（-x）=y（x）是偶函数

# 分段函数： 给定不同的区间有不同的对应关系的函数
x1 = np.arange(-5.0, 0.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.1)
y1 = x1
y2 = pow(x2, 2)
plt.plot(x1, y1)
plt.plot(x2, y2, linestyle="--")
plt.ylim(-10, 10)
plt.show()  # 如图是分段函数

# 一次函数：又叫线性函数。y=kx+b(k!=0)
x = np.arange(-5.0, 5.0, 0.1)
y = 2 * x + 2
plt.plot(x, y)
plt.ylim(-10, 10)
plt.show()  # 如图，是一条直线，k是直线的斜率，b是y轴上的截距。

# 二次函数：非线性函数，抛物线。
x = np.arange(-5.0, 5.0, 0.1)
y = 2 * x ** 2 + 3 * x + 2
plt.plot(x, y)
plt.ylim(-10, 10)
plt.show()

# 指数函数：非线性
x = np.arange(-1, 3, 0.1)
y = 2 ** x
plt.plot(x, y)
plt.ylim(-2, 25)
plt.show()

# 三角函数
# sin函数
x = np.arange(-5,5,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.ylim(-2,2)
plt.show()

#cos函数图像
x = np.arange(-5,5,0.1)
y = np.cos(x)
plt.plot(x,y)
plt.ylim(-2,2)
plt.show()