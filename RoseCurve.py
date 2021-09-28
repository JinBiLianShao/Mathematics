
##
#  玫瑰线
##
from matplotlib import pyplot as plt

import numpy as np

import math

i = np.linspace(-2*math.pi,2*math.pi,500)

theta=5*np.sin(3*i)

plt.subplot(221,projection='polar')

plt.plot(i,theta)

plt.title('p=5*sin(3*i)',color='r')

theta=5*np.sin(2*i)

plt.subplot(222,projection='polar')

plt.plot(i,theta)

plt.title('p=5*sin(2*i)',color='r')

theta=5*np.sin(3/2*i)

plt.subplot(223,projection='polar')

plt.plot(i,theta)

plt.title('p=5*sin(3/2i)',color='r')

theta=5*np.sin(1*i)

plt.subplot(224,projection='polar',title='p=5*sin(3*i)')

plt.plot(i,theta)

plt.title('p=5*sin(1*i)',color='r')

plt.show()

