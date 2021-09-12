#第一章：集合与常用逻辑

##集合是只具有某种特定性质的事物的总体。组成这个集合的事物称之为该集合的元素。
#一个集合，若它的元素是有限的话，我们称之为有限集。反之不是有限的我们称之为无限集。

import numpy as np
import math
#声明两个空集合，命名为A,B。
A = {}  #A集合
B = {} #B集合

#集合之间的关系：

#相等:集合A和集合B中的所有元素都相同
A = {1,2,3}
B = {1,3,2}
if A==B:
    print("A集合与B集合相等！")
else:
    print("A集合不等于B集合！")

#子集：集合A中任意一个元素都是集合B中的元素
A = {1,2,3}
B = {1,2,3,4,5}

result = A <= B
if result:
    print("A是B的子集！")
else:
    print("A不是B的子集！")

#真子集：集合A中任意一个元素都是集合B中的元素，且集合B中至少有一个元素不是集合A中的元素
A = {1,2,3}
B = {1,2,3}
result = A < B
if result:
    print("A是B的真子集！")
else:
    print("A不是B的真子集！")

#空集：是任何集合的子集，是任何非空集合的真子集
A = {}
B = {}

#并集：由集合A和集合B共同组成的集合叫并集（A并B）
A = {1,2,3,4}
B = {5,6,7,8,9}
result = A | B
print(result)

#交集：集合A和B共同拥有的元素构成的集合
A = {1,2,3,4}
B = {3,4,5,6}
result = A & B
print(result)

#补集与全集
U = {1,2,3,4,5,6,7,8,9} #全集
A = {1,2,3,4,5}
result = U - A #补集
print(result)

'''
函数介绍：numpy库中的arange方法生成的是左开右闭的区间。
'''
#开区间
x = np.arange(1+1,10)
print("这是（1，10）的开区间:" + str(x))

#闭区间
x = np.arange(1,10+1)
print("这是[1，10]的闭区间:" + str(x))

'''
无穷数的介绍：在python中其实也是可以表示正负无穷数的。
在此，我们使用float('inf')来表示正无穷数，float('inf')来表示负无穷数。
如何检测无穷数呢？我们用到math库的isinf()方法来判断
'''
# 无穷大
x = float('inf') #用于表示无穷大
y = 100000000000000000
print(math.isinf(x))
print(math.isinf(y))

#逻辑门（与，或，非）
class Logic:
    def __init__(self,x):
        self.x = x
    def AND(self):  #与门运算
        w = np.array([0.5,0.5])
        t = 0.7
        sum = np.sum(self.x*w)-t
        print(str(self.x[0]) + "与" + str(self.x[1]) + "为：")
        if sum <= 0:
            print(0)
        elif sum > 0:
            print(1)
    def OR(self):  #或门运算
        w = np.array([0.7, 0.7])
        t = 0.5
        sum = np.sum(self.x * w) - t
        print(str(self.x[0]) + "或" + str(self.x[1]) + "为：")
        if sum <= 0:
            print(0)
        elif sum > 0:
            print(1)
s = np.array([[1,0],[0,1],[0,0],[1,1]])
for x in s:
    # 实例化对象
    logic = Logic(x)
    #与门
    logic.AND()
    #或门
    logic.OR()


