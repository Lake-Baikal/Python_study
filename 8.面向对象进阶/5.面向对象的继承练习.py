#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   5.面向对象的继承练习.py
@Time    :   2025/02/14 23:10:05
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# 代码分析
class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()
print(f"son.name{son.name} son.age{son.age} son.hobby{son.hobby}")


# 编程题
"""
编写Computer类,包含CPU,内存,硬盘等属性
1.get_details 方法返回Computer的详细信息
2.编写PC子类,继承Computer 类,添加特有的属性[品牌brand]
3.编写NotePad的子类,继承Computer类,添加特有的属性[color]
4.完成测试,创建PC和NotePad对象,分别给对象特有的属性赋值,以及从Computer类继承属性和方法,并使用方法打印输出信息
"""
"""
思路分析
1.父类:Computer
2.公共属性:CPU(cpu),内存(memory),硬盘(disk)
3.构造器:__init__(self,cpu,memory,disk)
4.方法:get_details(self):
5.子类:PC(computer)
6.公共属性:brand
7.构造器:__init__(self,brand,cpu,memory,disk)
8.方法:print_info(self):完成功能,输出PC对象的信息(即属性的信息)
"""


class Computer:
    cpu = None
    memory = None
    disk = None

    def __init__(self, cpu, memory, disk):
        self.cpu = cpu
        self.disk = disk
        self.memory = memory

    def get_details(self):
        return f"cup:{self.cpu}\t内存大小:{self.memory}\t硬盘:{self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, cpu, memory, disk, brand):
        # 初始化子类的属性 -方式一
        # self.cpu = cpu
        # self.memory = memory
        # self.disk = disk
        # self.brand = brand
        # 通过super().xx的方式可以调用父类的方法
        # 在这里我们通过super().__init__(cpu, memory, disk)调用父类的构造器,完成对父类的初始化任务
        # self.brand = brand :表示子类的特有属性,由子类的构造器完成初始化

        super().__init__(cpu, memory, disk)
        self.brand = brand

    def print_info(self):
        # 完成打印当前任务的信息
        print(f"品牌{self.brand} {self.get_details()}")


# 测试
pc = PC("intel", 32, 1000, "戴尔")
pc.print_info()
