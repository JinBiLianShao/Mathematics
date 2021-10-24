'''
    python基础
'''
import numpy as np  # 计算
import math
import matplotlib.pyplot as plt  # 画图
import sympy as sp  # 函数库
import interval as iv  # 区间库



'''x = sp.symbols("x")  # 定义未知数x，x为非空集合中的一个未知元素。
y = sp.solve(((x - 2) ** 2) * ((x - 3) ** 3) * ((x - 4) ** 4), x)  # 函数关系式，该方法是在函数等用0的时候参与运算求解，得到的结果为数组。
print(y) #求函数等于0的时候的解
s = sp.diff(((x - 2) ** 2) * ((x - 3) ** 3) * ((x - 4) ** 4), x)
print(s) #求导
x = np.arange(-5, 5, 0.1)  # 定义x的区间和表示单位
y = ((x - 2) ** 2) * ((x - 3) ** 3) * ((x - 4) ** 4)  # 函数体
plt.plot(x, y)
plt.ylim(-10, 10)  # 定义y的区间
plt.show()
f1 = (sp.sin(sp.sin(x)) - sp.sin(sp.sin(sp.sin(x)))) / (sp.sin(x)) ** 3
# f1 = sp.sin(x)/x
z = sp.limit(f1, x, 0)
print(z)
# 求导
f2 = (sp.sin(sp.sin(x)) - sp.sin(sp.sin(sp.sin(x))))
f2q = sp.diff(f2,x)
print(f2q)
f3 = (sp.sin(x)) ** 3
f3q = sp.diff(f3,x)
print(f3q)
f4 = f2q/f3q
h = sp.limit(f4, x, 0)
print(h)
#极限的几何意义
x = np.arange(-3, 3, 0.1)
y = x**2
plt.plot(x, y)
y1 = np.arange(0, 5, 0.01)
x1 = -1.1*y1/y1
plt.plot(x1, y1, linestyle="--")
y2 = np.arange(0, 5, 0.01)
x2 = -0.9*y2/y2
plt.plot(x2, y2, linestyle="--")
x3 = np.arange(-3, 3, 0.01)
y3 = 0.81*x3/x3
plt.plot(x3, y3, linestyle="--")
x4 = np.arange(-3, 3, 0.01)
y4 = 1.21*x4/x4
plt.plot(x4, y4, linestyle="--")
plt.ylim(0, 2)
plt.show()

x1 = np.arange(-5,5,0.1)
y1 = x1
plt.plot(x1,y1)
# x的取值范围-2到2
x2 = np.arange(-2,2,0.1)
y2 = (4-x2**2)**0.5
plt.plot(x2,y2)

x3 = np.arange(-5,5,0.1)
y3 = 1+x3/x3
plt.plot(x3,y3)
plt.ylim(-5,5)
plt.show()
’’’
num = input()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data[0])
'''
x = np.arange(-10, 10, 0.1)
y = 2 ** x
plt.plot(x, y)
plt.ylim(-5, 5)
plt.show()
