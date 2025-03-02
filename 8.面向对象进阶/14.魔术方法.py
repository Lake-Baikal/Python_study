#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   14.魔术方法.py
@Time    :   2025/02/23 17:34:44
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# !什么是魔术方法
"""
1.在python中,所有以下划线__包起来的方法,统称为Magic Method(魔术方法),他是一种特殊的方法,普通方法需要调用,而魔术方法不需要调用就即可自动执行
2.魔术方法在类或者对象的某些事件发生时会自动执行,让类具有神奇的魔力,如果希望根据自己的程序定制特殊的功能的类,那么就需要对这些方法进行重现写
3.Python中常见的运算符,for循环,以及类的操作等都是运行在魔术方法之上的
"""
# !常见的魔术方法
"""
1.__init__:初始化对象的成员
2.__str__(self):定义对象转字符串行为,print(对象)或者str(对象)
3.__eq__(self,other):定义等于号的行为:x==y
4.__lt__(self,other):定义小于号的行为:x<y
5.__le__(self,other):定义小于等于的号的行为:x<=y
6.__ne__(self,other):定义不等于号的行为:x!=y
7.__gt__(self,other):定义大于号的行为:x>y
8.__ge__(self,other):定义大于等于号的行为:x<=y
"""


# 1.__str__ 打印对象默认返回:类型名+对象内存地址,子类往往重写__str__,用于返回对象的属性信息
# 2.重新__str__方法,print(对象)或str(对象)时,都会自动调用该对象的__str__


# ! 请输出Monster[name,job,sal]对象的属性信息
class Monster:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        # 请输出Monster[name,job,sal]对象的属性信息
        # 可以根据需求重写__str__
        # !在默认情况下,调用的是父类的object的__str__
        # !父类object的__str__返回的就是类型+地址
        # !可以根据需要重写str方法

    def __str__(self):
        # return ""
        # return super().__str__()
        return f"{self.name} {self.age} {self.gender}"


m = Monster("baikal", 25, "boy")
print(m, hex(id(m)))  # 默认输出对象的类型+对象的地址

# ! eq方法:
"""
==是一个比较运算符,对象之间进行比较时,比较的是内存地址是否相等,即判断是不是同一个对象
重写__eq__方法,可以用于判断对象内容/属性是否相等
"""
# 案例
"""
判断两个Person对象的内容是否相等,如果两个Person对象的各个属性值都一样,则返回true,反之false
Person类,属性(name,age,gender)
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __eq__(self, other):
        # 判断other是不是Person
        if isinstance(other, Person):
            return (
                self.name == other.name
                and self.age == other.age
                and self.gender == other.gender
            )
        return False

    # 根据Person对象的年龄进行比较大小,重新相应的魔术方法
    # 重写__lt__
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return "类型不一致,不能进行比较"

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return "类型不一致,不能进行比较"

    def __ne__(self, other):
        return not self.__eq__(other)


class Dog:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# ! 没有重写 __eq__前,==比较的是内存地址
p1 = Person("smith", 20, "男")
p2 = Person("smith", 21, "男")
dog = Dog("smith", 20, "男")
print(f"p1==p2,{p1 == p2}")
print(f"p1==dog,{p1 == dog}")

# ! 重写__lt__

print(f"p1<p2,{p1 < p2}")
# 重写__le__
print(f"p1<=p2,{p1 <= p2}")
# 重写__ne__
print(f"p1!=p2,{p1 != p2}")
