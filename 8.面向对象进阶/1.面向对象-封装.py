#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   面向对象-封装.py
@Time    :   2025/02/01 14:34:04
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# !面向对象编程有三大基本特征:封装,继承,多态
# ?封装的家介绍
'''
1.封装(encapsulation)就是把抽象出的数据[属性]和对数据的操作[方法]封装到一起,数据被保护在内侧
2.程序只有通过被授权的操作,才能对数据进行访问
'''
# 封装的好处
# 1.隐藏实现细节
# 2.可以对数据进行验证,保证安全合理
# 3.可以保护数据隐私,要求授权才可以访问

# ?私有成员
'''
!公共的变量和方法
默认情况下,类中的变量和方法都是共有的,他们的名称前面没有下划线
公共的变量和方法,在类的外部和内部都可以正常访问
>如何将属性/方法进行私有化
类中的变量或方法以下划线__开头命名,则该变量或方法为私有的,私有的变量或方法,只能在本类内部使用,类的外部无法使用
>如何访问私有的属性/方法:提供公共的方法,用于对私有成员的操作
'''
'''
!案例
创建职员类(clerk),属性有name,job,salary
1.不能随便查看职员clerk的职位和工资等隐私,比如职员("alan","Python",20000)
2.提供公共的方法,可以对职位和工资进行操作
'''


class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共的方法, 对私有属性进行操作(根据实际的业务进行编写即可)
    def set_job(self, job):
        self.__job = job

    def get__job(self):
        return self.__job

    # 私有方法
    def __hi(self):
        print("hi")

    # 提供公共方法,操作私有方法
    def f1(self):
        self.__hi()


clerk = Clerk("alan", "Python工程师", 20000)
# 如果是公共属性,在类的外部可以直接访问
print(clerk.name)
# 如果是私有属性,在类的外部不可以直接访问
# print(clerk.__job)
# AttributeError: 'Clerk' object has no attribute '__job'

print(clerk.get__job())
clerk.set_job("java工程师")
print(clerk.get__job())

# 私有方法不能在类的外部直接调用
# clerk.__hi()
# AttributeError: 'Clerk' object has no attribute '__hi'
# 通过公共方法调用私有方法
clerk.f1()
