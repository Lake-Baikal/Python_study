#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   12.isinstance函数.py
@Time    :   2025/02/20 20:32:22
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# ! isinstance()用于判断对象是否为某个类或其子类的对象
# !基本语法 isinstance(object,classinfo)
# object:对象
# classinfo:可以是类名,基本类型或者由他们组成的元组
class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


# 创建两个对象
obj = BB()
obj2 = AA()
# 分析输出的结果
print(f"obj是不是BB的对象{isinstance(obj, BB)}")
print(f"obj是不是AA的对象{isinstance(obj, AA)}")
print(f"obj是不是CC的对象{isinstance(obj, CC)}")
num = 9
print(f"num是不是int:{isinstance(num, int)}")
print(f"num是不是str:{isinstance(num, str)}")

# 是元组中的一个返回True
print(f"num 是不是str/int/list:{isinstance(num, (str, int, list))}")


# 代码阅读题
class A:
    i = 10

    def sum(self):
        # self到底是A还是B
        # !当调用对象成员的时候,会和对象本身动态关联
        return self.getI() + 10

    def sum1(self):
        return self.i + 10

    def getI(self):
        return self.i


class B(A):
    i = 20

    # def sum(self):
    #     return self.i + 20

    def getI(self):
        return self.i

    # def sum1(self):
    #     return self.i + 10


# 创建了一个B的对象b
b = B()
print(b.sum())
print(b.sum1())
# !当调用对象成员的时候,会和对象本身动态关联
