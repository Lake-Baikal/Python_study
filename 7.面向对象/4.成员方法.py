#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Filename    :   4.成员方法.py
@Time    :   2025/01/18 22:21:43
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
"""
# !类除了有一些属性外,还有一些行为,比如人类有年龄,姓名等属性,我们人类还有一些行为比如:可以跑步,说话...通过学习可以左计算,这时就需要成员方法才能完成
# !定义类的基本方法
"""
class 类名
    属性
    行为
# !类中定义的行为(函数),我们称之为:成员方法/方法
"""
# !成员方法的定义和使用
# ?在类中定义成员方法和前面学习过的定义函数,基本上是一致的(原理和运行机制是一样的),但是形式上有点不同
"""
定义成员方法和基本语法
def 方法名(self,形参列表):
    方法体
> 1.在方法定义的参数列表中,有一个self
> 2.self是定义成员方法时,需要写上的
> 3.self表示当前对象本身
> 4.当我们通过对象调用方法时,self会隐式的传入
> 5.在方法内部,需要使用self,才能访问到成员变量
"""
# *案例
'''
? 定义一个Person类(name,age),完成如下要求:
> 1.添加hi成员方法,输出"hi Python"
> 2.添加cal01成员方法,可以计算1+2+...1000的结果
> 3.添加cal01成员方法,该方法可以接收一个数了,计算从1+...+n
> 4.添加get_num成员方法,可以计算两个数的和,并返回
'''


class Person:
    # 属性
    name = None
    age = None

    # 1.添加hi成员方法,输出"hi Python"
    def hi(self):
        print("hi Python")

    # 2.添加cal01成员方法,可以计算1+2+...1000的结果
    def cal01(self):
        result = 0
        for i in range(1, 1001):
            result += i
        print("result=", result)

    # 3.添加cal01成员方法,该方法可以接收一个数n,计算从1+...+n
    def cal02(self, n):
        result = 0
        for i in range(1, n + 1):
            result += i
        print("result=", result)

    # 4.添加get_num成员方法,可以计算两个数的和,并返回
    def getsum(self, n1, n2):
        return n1 + n2


# !完成测试
p = Person()
# 通过对象名.方法名()调用方法
p.hi()
p.cal01()
p.cal02(10)
print(p.getsum(10, 20))


# -> 成员方法的使用细节
# !Python也支持对象动态的添加方法
# 函数
def hi():
    print("hi python")


class Person:
    name = None
    age = None

    def ok(self):
        pass


# 创建了对象p和p2
p = Person()
p2 = Person()
# ! 1.动态给p对象添加方法,注意只是针对p对象添加方法
# ! 2.m1是你新增的方法的名称,由程序员指定名字
# ! 3.即m1方法和函数h1关联起来,当调用m1函数就会执行h1函数
p.m1 = hi
# 调用m1
p.m1()
print(type(p.m1), type(hi))
print(type(p.ok))
# 因为没有动态的给p2添加方法,会报错
# p2.m1()
