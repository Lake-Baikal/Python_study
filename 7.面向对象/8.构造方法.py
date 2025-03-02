#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   8.构造方法.py
@Time    :   2025/01/29 12:04:40
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# 前面我们在创建Person类时,是先把一个对象创建好,在给他的年龄,姓名赋值.
# 如果限制我要求,在创建Person类的对象时,就直接指定这个对象的属性(年龄,姓名),该怎么做->使用构造方法(也叫构造器)
'''
构造方法的基本语法
def __init__(self,参数列表):
    代码

! 解读构造方法
1.在初始化对象时,会自动执行__init__方法
2.在初始化对象时,将传入的参数,自动传递给__init__方法
3.构造方法是python预定义的,名称是__init__,注意init前后有两个_
'''


# ? 1.在初始化对象时,会自动执行__init__方法
# class Person:
#     # 构造方法/构造器
#     def __init__(self):
#         print("__init__执行了")


# p1 = Person()
# p2 = Person()
# ? 2.在初始化对象时,将传入的参数,自动传递给__init__方法
class Person:
    name = None
    age = None

    # 构造方法/构造器
    # !构造方法时完成对象的初始化任务
    def __init__(self, name, age):
        print(f"__init__执行了{name} {age}")
        # !把接收到的name和age赋值给属性name和age
        # !self就是你当前创建的对象
        print(f"self的id:{id(self)}")
        self.name = name
        self.age = age


# 创建对象
p1 = Person("baikal", 20)
print(f"p1的id:{id(p1)}")
print(f"p1的信息是 {p1.name} {p1.age}")

p2 = Person("alan", 30)
print(f"p2的id:{id(p2)}")
print(f"p2的信息是 {p2.name} {p2.age}")


# 构造方法的注意事项和使用细节
# ! 1.一个类只有一个__init__方法,即使写了多个也只有最后一个生效
class Person:
    name = None
    age = None

    # def __init__(self, name, age):
    #     print(f"__init__执行了...得到了{name}{age}")
    #     self.name = name
    #     self.age = age

    def __init__(self, name):
        print(f"__init__执行了...得到了{name}")
        self.name = name


# 报错
# p1 = Person("baikal", 20)
# Person.__init__() takes 2 positional arguments but 3 were given
# !后面的__init__会生效
p1 = Person("Baikal")
print(f"p1的name={p1.name} age={p1.age}")


# ! 2.Python可以动态的生成对象属性
# !3.构造方法不能有返回值,比如你返回字符串,会报TypeError: __init__() should return None, not 'str'


class Person:
    # name = None
    # age = None
    def __init__(self, name, age):
        print(f"__init__执行了...,得到了{name} {age}")
        # 将得到到的name和age赋值给当前对象的name,age属性
        # !Python执行动态生成对象属性
        self.name = name
        self.age = age
        # return "hello"  # TypeError: __init__() should return None, not 'str'


p1 = Person("baikal", 20)
print(f"p1的name={p1.name} age={p1.age}")
