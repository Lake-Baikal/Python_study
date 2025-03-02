#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   16.抽象类.py
@Time    :   2025/02/25 22:36:35
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def cry(self):
#         # 动物都有叫唤行为...但是这个行为不明确(即不能明确实现)
#         print("不知道是什么动物,不知道是什么叫声")

from abc import ABC, abstractmethod


# 当父类的某些方法,需要声明,但是又不确定如何实现,怎么办
# 不需要实例化父类对象,父类主要的是用于设计和制定规范,让其他类来继承并实现,怎么办
# !抽象类的介绍
"""
1.默认情况下,Python不提供抽象类,Python附带一个模块,改模块为定义抽象基类提供了基础,该模块的名称为abc
2.当我们需要抽象基类时,让类继承ABC(abc模块的ABC类),使用@abstractmethod声明抽象方法,(@abstractmethod用于声明抽象方法的装饰器,在abc模块中),那么这个类就是抽象类
3.抽象类的价值更多的作用是在于设计,是设计者设计好后,让子类继承并实现抽象类的抽象方法
"""
# !当父类的一些方法不确定时,可以使用@abstractmethod声明,(说明:@abstractmethod用于声明抽象方法的装饰器),同时继承ABC类,那么这个类就是抽象类
# 把Animal 作为抽象类,并让子类Tiger实现


# Animal就是抽象类
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这是cry就是一个抽象方法
    @abstractmethod
    def cry(self):
        # 动物都有叫唤行为...但是这个行为不明确(即不能明确实现)
        # print("不知道是什么动物,不知道是什么叫声")
        pass


# !注意抽象类(含有抽象方法),不能实例化
# TypeError: Can't instantiate abstract class
# animal = Animal("动物", 3)


# 编写子类Tiger继承Animal 并实现抽象方法
class Tiger(Animal):
    def cry(self):
        print(f"老虎{self.name}嗷嗷叫")


tiger = Tiger("皮皮", 20)
tiger.cry()

# 注意事项和使用细节
# ! 抽象类不能实例化
# ! 抽象类需要继承ABC,并且需要至少一个抽象方法
# from abc import ABC, abstractmethod


# class AAA(ABC):
#     name = "tim"

#     # @abstractmethod
#     # def f1(self):
#     #     pass

#     # 如果没有一个抽象方法, 能实例化


# obj1 = AAA()
# print("ok")


# !抽象类中可以有普通方法
class AAA(ABC):
    name = "tim"

    @abstractmethod
    def f1(self):
        pass

    def hi(self):
        print("hi()~~")

    def ok(self):
        pass


class BBB(AAA):
    # 实现了父类的f1方法
    def f1(self):
        print("BBB-f1()...")


obj2 = BBB()
obj2.f1()
obj2.hi()
obj2.ok()
print("~~~")


# !如果一个类继承了抽象类,则它必须实现抽象类的所有抽象方法,否则他仍然是一个抽象类
class AAA(ABC):
    name = "tim"

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

    def hi(self):
        print("hi()~~~")

    def ok(self):
        pass


class BBB(AAA):
    # 实现父类的f1抽象方法
    def f1(self):
        print("BBB-f1()...")

    # 如果没有完全实现AAA的抽象方法
    def f2(self):
        print("BBB-f2()...")


# 会报错Can't instantiate abstract class BBB without an implementation for abstract method 'f2'

obj2 = BBB()
obj2.f1()
obj2.hi()
obj2.ok()
print("~~~")

# 编程题
"""
1.编写一个Employee类做成抽象类,包含如下三个属性:name,id,salary,提供必要的构造器和构造方法:work()
2.对于Manager类来说,他既是员工,还具备奖金(bonus)的属性
3.请使用继承的思想,设计CommonEmployee类he Manager类,要求实现work(),提示"经理/普通员工 名字 工作中... "
"""


# 父类-抽象类
class Employee(ABC):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


# 子类 CommonEmployee
class CommonEmployee(Employee):
    def work(self):
        print(f"普通员工{self.name} 工作中...")


class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus

    def work(self):
        print(f"经理{self.name}工作中...")


# 完成测试
manager = Manager("King", "1-111", 10000, 100000)
manager.work()
commonEmployee = CommonEmployee("Baikal", "1-222", 50000)
commonEmployee.work()
