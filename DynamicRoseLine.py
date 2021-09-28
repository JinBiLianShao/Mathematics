###
#  动画演示玫瑰线的绘画过程
###


from matplotlib import pyplot as plt

import numpy as np

import math

i = np.linspace(0,2*math.pi,500)

theta=5*np.sin(3*i)

plt.title('p=5*sin(3*i)',color='r')

i_list=[]

theta_list=[]

for (i_tmp,theta_tmp) in zip(i,theta):

    i_list.append(i_tmp)

    theta_list.append(theta_tmp)

#去除负值，使得动画更顺畅

    if(theta_tmp>=0):

        plt.plot(i_list,theta_list)

        plt.pause(0.01)

        plt.axes(polar=True)

        plt.ylim(0,5)

#保存动画

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.animation as animation

# 生成图例

fig = plt.figure(figsize=(5,5))

ax = plt.subplot(projection='polar')

# 绘制动态函数的变量

x = np.linspace(0, 2*np.pi, 500)

# 实例化线条

line, = ax.plot([], [], color='r')

r,theta=[],[]

def init():

    # 设置y轴的范围

    ax.set_ylim(0, 5)

    return line

# 更新函数，n是动态变量

def update(n):

    # 更新数据

    theta.append(n)

    r.append(5*np.sin(3*n))

    line.set_xdata(theta)

    line.set_ydata(r)

    return line

# frames在调用update函数时，会将frames后面的数据作为实参传递给“n”

# interval更新频率，单位ms

ani = animation.FuncAnimation(fig, update,frames=x,init_func=init,interval=10)

ani.save('sin.gif',writer='pillow')