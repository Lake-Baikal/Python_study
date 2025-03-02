#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   3.面向对象的继承.py
@Time    :   2025/02/03 18:23:32
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# 为什么需要继承
# 我们编写两个类,一个Public类(小学类),一个是Graduate类(大学毕业生类)
# 问题:两个类的属性和方法很多是一样的,怎么办.
# ?没有使用继承前的代码
# 小学类
# class Pupil:
#     name = None
#     age = None
#     __score = None

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f"name={self.name} age={self.age} score={self.__score}")

#     def set_score(self, score):
#         self.__score = score

#     def testing(self):
#         print("..小学生在考数学")


# class Graduate:
#     name = None
#     age = None
#     __score = None

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f"name={self.name} age={self.age} score={self.__score}")

#     def set_score(self, score):
#         self.__score = score

#     def testing(self):
#         print("..大学生在考数学")


# 测试
# student1 = Pupil("alan", 10)
# student1.testing()
# student1.set_score(80)
# student1.show_info()

# student2 = Graduate("Baikal", 22)
# student2.testing()
# student2.set_score(80)
# student2.show_info()

'''
# 分析问题
1.Pupli和Graduate有很多相同的属性和方法
2.目前这样的方法,代码复用性很差
3.不利于代码的维护和管理
'''

# ! 继承的基本介绍
'''
1.继承可以解决代码的复用,让我们的编程更加靠近人类思维
2.当多个类存在相同的属性(成员变量)和方法时,可以从这些类中抽取象出父类,在父类中定义这些相同的属性和方法,所有的之类不需要重新定义这些属性和方法
'''
# !继承的基本语法
''' DerivedClassName(BaseClassName):
    <statemant-1>


    <statemant-N>

1.派生类就会自动拥有基类定义的属性和方法
2.基类习惯上也叫父类
3.派生类习惯上也叫子类
'''


# 使用继承的代码
# 编写父类
class Student:
    name = None
    age = None
    __score = None
    gebder = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

    def set_score(self, score):
        self.__score = score


# Pupil继承Student类
class Pupil(Student):

    def testing(self):
        print("..小学生在考数学")


# Granduate继承Student类
class Graduate(Student):

    def testing(self):
        print("..大学生在考数学")


# 测试
student1 = Pupil("alan", 10)
student1.testing()
student1.set_score(80)
student1.show_info()

student2 = Graduate("Baikal", 22)
student2.testing()
student2.set_score(80)
student2.show_info()

# ? 继承给编程带来的便利就是
# 1.代码的复用性提高了
# 2.代码的拓展性和维护性提高了
