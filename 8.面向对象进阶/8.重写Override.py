#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   8.重写Override.py
@Time    :   2025/02/16 14:22:15
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# 重写又称覆写,即子类继承父类的属性和方法后,根据业务的需要,在重新定义同名的属性个方法
class A:
    n1 = 100

    def run(self):
        print("A-run()...")


class B(A):
    # ! 子类重写了父类的n1属性
    n1 = 200
    # ! 子类重写了父类的run方法

    def run(self):
        print("B-run()...")

    # say 方法通过父类名,去访问父类的成员
    def say(self):
        print(f"父类的n1 {A.n1} 本类的n1 {self.n1}")
        # 调用父类的run
        A.run(self)
        # 调用本类的run
        self.run()

    def hi(self):
        # hi方法,通过super()方法去访问父成员
        print(f"父类的n1{super().n1}")
        # 调用父类的run
        super().run


b = B()
b.say()
b.hi()

# !案例
"""
编写一个Person类,包括属性(name,age),构造方法,say方法(返回Person自我介绍的字符串)
编写一个Student类,继承Person类,增加属性(id,score),以及构造方法,重写say方法(返回Student自我介绍的信息)
分别创建Person和Student对象,调用say方法输出自我介绍,体会重写的作用
"""


class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"名字:{self.name} 年龄:{self.age}"


class Student(Person):
    id = None
    score = None

    def __init__(self, id, score, name, age):
        # 调用父类的构造器完成继承父类的属性的初始化
        super().__init__(name, age)
        # 子类的特有的属性,我们自己完成初始化
        self.id = id
        self.score = score

    def say(self):
        return f"id:{self.id} 成绩:{self.score} {super().say()}"


person = Person("tom", 12)
print(person.say())
student = Student("8-30", 100, "Baikal", 20)
print(student.say())
