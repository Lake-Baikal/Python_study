#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   4.面向对象的继承细节.py
@Time    :   2025/02/06 21:31:36
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# ! 1.子类继承了所有的属性和方法,非私有的属性和方法可以在子类中直接访问,但是私有属性和方法不能在子类直接访问,要通过父类提供公共的方法访问
class Base:
    # 公共属性
    n1 = 100
    # 私有属性
    __n2 = 200

    def __init__(self):
        print("Base构造方法...")

    def hi(self):
        print("hi()公共方法")

    def __hello(self):
        print("__hello()私有方法")

    # !提供公共的方法访问私有属性和方法
    def test(self):
        print("属性:", self.n1, self.__n2)
        self.__hello()


class Sub(Base):
    # 子类构造器
    def __init__(self):
        print("Sub构造方法")

    def say_ok(self):
        # 我们发现父类的非私有属性和方法可以访问
        print("say_ok()", self.n1)
        self.hi()
        # 我们发现父类的私有属性和方法不可以访问
        # print(self.__n2)
        # self.__hello()


# 创建子类对象
sub = Sub()
sub.say_ok()
# 调用子类继承父类的公共方法实现访问父类的私有成员的效果
sub.test()


# ! 2.Python语言中Object是所有其他类的基类

# ! 3. python支持多重继承,即一个类可以继承多个父类
"""
class DerviedClass(Base1, Base2, Base3):

    <statments-1>


    <statments-n>
"""


class A:
    n1 = 100

    def sing(self):
        print("A sing()...", self.n1)


class B:
    n2 = 200
    n1 = 300

    def dance(self):
        print("B dance()...", self.n2)

    def sing(self):
        print("B sing()...", self.n1)


# C类继承了A和B两个类(多重继承)
class C(A, B):
    pass


c = C()

print(f"属性的信息{c.n1} {c.n2}")
# 调用继承的方法
c.sing()
c.dance()

# ! 4.在多重继承中,如果有同名的成员,遵守从左到右的继承优先级,即写左边的父类优先级高,写在右边的父类优先级低


# 案例 分析题
class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()
print(f"son.name:{son.name} son.age={son.age} son.hobby={son.hobby}")

"""
编写Computer类,包含CPU,内存,硬盘等属性
1.get_details()方法,返回Computer的详细信息
2.编写PC类,继承Computer类,并添加特有属性[品牌brand]
3.编写NotePad子类,继承Computer类,并添加特有属性[颜色color]
4.完成测试,创建PC和NotePad对象,分别给对象中特有的属性赋值,以及从Computer类中继承的属性赋值,并使用方法打印输出信息
"""
# 思路分析
"""
1.父类:Computer
2.公共属性:CPU,内存(memory),硬盘(disk)
3.构造器:__init__(self,cpu,memory,disk)
4.方法:get_details(self)
5.子类:PC(Computer)
6.公共属性:brand
7.构造器:__init__(self,cpu,memory,disk,brand),有一个新的知识
8.方法:print_info(self) 输出PC对象的信息(即属性的信息)
"""


class Computer:
    cpu = None
    memory = None
    disk = None

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def details(self):
        return f"cup:{self.cpu}\t内存:{self.memory}\t硬盘:{self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, cpu, memory, disk, brand):
        # 初始化子类的属性-方式一
        # self.cpu = cpu
        # self.memory = memory
        # self.disk = disk
        # self.brand = brand
        # !初始化子类的属性-方式二
        # 通过super().xx的方式调用父类的构造方法
        # 在这里我们通过super().__init__(cpu, memory, disk)去调用父类的构造方法完成对父类属性的初始化
        # self.brand = brand 表示子类特有的属性由子类的构造器去完成初始化

        super().__init__(cpu, memory, disk)
        self.brand = brand

    # 完成打印当前对象的信息
    def print_info(self):
        print(f"品牌:{self.brand}\t{self.details()}")


# 测试
pc = PC('intel', 32, 1000, '戴尔')
pc.print_info()
