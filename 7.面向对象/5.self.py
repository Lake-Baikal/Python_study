#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   5.self.py
@Time    :   2025/01/22 20:58:08
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# 看下面的一段代码,分析输出的信息是什么
class Dog:
    name = "波斯猫"
    age = 2

    def info(self, name):
        print(f"name的信息:{name}")


dog = Dog()
dog.info("加菲猫")


# ! 问题分析:如果我们希望在成员方法内,访问对象的属性/成员方法,怎么办?
# class Dog:
#     name = "波斯猫"
#     age = 2

#     def info(self, name):
#         # 如果希望访问到属性name,使用self.name即可
#         # !通过self.属性名 可以访问到对象的属性/成员变量
#         print(f"name的信息:{self.name}")


# dog = Dog()
# dog.info("加菲猫")


# ! self的使用细节
# 成员方法定义的基本语法
# def 方法名(self,形参列表):
#     方法体
'''
!1.在方法定义的参数列表中,有一个self
!2.self是定义成员方法时,需要写上的,如果不写,则需要使用@staticmethod标注,否则会报错
'''


class Dog:
    name = "边牧"
    age = 2

    def info(self, name):
        print(f"name的信息:{name}")

    # ?静态方法
    # !1.通过@staticmethod 可以把方法转换为静态方法
    # !2.如果是一个静态方法,可以不带self
    # !3.静态方法的调用形式有变化
    @staticmethod
    def ok():
        print("ok()...")


dog = Dog()
dog.info("德牧")
# !调用静态方法
# 1.通过对象调用
dog.ok()
# 2.通过类名调用
Dog.ok()
# !普通方法不能使用类名调用
# Dog.info("哈哈")


# !3. self表示当前对象本身,那个对象调用,self就代表那个对象
class Dog:
    name = "边牧"
    age = 2

    def hi(self):
        print(f"hi self:{id(self)}")


# ?self 表示当前对象本身
# 创建对象dog2
dog2 = Dog()
print(f"dog2:{id(dog2)}")
dog2.hi()
# 创建对象dog2
print("----------------------")
dog3 = Dog()
print(f"dog3:{id(dog3)}")
dog3.hi()


# !4.当我们通过对象调用方法时,self会隐式的传入
# !5.在方法内部要访问成员变量和成员方法,需要使用self
class Dog:
    name = "边牧"
    age = 2

    def eat(self):
        print(f"{self.name}饿了..")

    def cry(self, name):
        print(f"{name}is crying")
        print(f"{self.name} is crying")
        self.eat()  # !调用成员方法
        # 不能直接调用
        # eat()


dog = Dog()
# ?修改dog对象的属性,name,中华田园犬
dog.name = "中华田园犬"
dog.cry("金毛")


# 课堂练习
'''
1.定义Person类
2.里面有name,age属性
3.并提供compare_to比较方法,用于判断是否和另一个人相等
4.名字和年龄都一样,就返回Ture,否则返回False
'''


# !思路分析
# 类名:Person
# 属性:name,age
# 方法:compare_to(self,other)
# 如果名字和年龄都一样,就返回Ture,否则返回False
class Person:
    name = None
    age = None

    def compare_to(self, other):
        # 如果名字和年龄都一样,就返回Ture,否则返回False
        return self.name == other.name and self.age == other.age


# 测试
p1 = Person()
p1.name = "jack"
p1.age = 13
p2 = Person()
p2.name = "jack"
p2.age = 13

print(p1.compare_to(p2))
