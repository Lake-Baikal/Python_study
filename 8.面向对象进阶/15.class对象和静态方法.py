#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   15.class对象和静态方法.py
@Time    :   2025/02/24 22:27:46
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# ! 类本身也是对象,即class对象
class Monster:
    name = "蝎子精"
    age = 300

    def hi(self):
        print(f"hi() {self.name}--{self.age}")


# 下一个断点,可以看到Master的情况
print(Monster)
# 通过Class对象,可以引用属性(没有创建实例对象也可引用/访问)
print(f"Monster.name:{Monster.name} Monster.age:{Monster.age}")
# 通过类名如何调用非静态成员方法
Monster.hi(Monster)

# ! 静态方法
"""
@staticmethod将方法转换为静态方法
静态方法不会接收隐式的第一个参数,要声明一个静态方法,语法:
class C:
    @staticmethod
    def f(arg1,arg2,argN):...
        pass
# 静态方法既可以由类调用(如C.f()),也可以有实例调用,如(C().f())
"""


class Monster:
    name = "Baikal"
    age = 300

    def hi(self):
        print(f"hi() {self.name}=={self.age}")

    @staticmethod
    def ok():
        print("ok()...")


# 不需要实例化,通过类即可调用静态方法
Monster.ok()
# 通过实例对象,也可调用静态方法
monster = Monster()
monster.ok()
Monster().ok()
