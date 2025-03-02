#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   18.模板设计练习.py
@Time    :   2025/03/01 21:47:22
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# ? 定义一个Person类,属性:name,age,job,创建Person列表,有三个Person对象,并按照age从大到小进行排序


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"{self.name}--{self.age}--{self.job}"


p1 = Person("smith", 20, "java工程师")
p2 = Person("king", 18, "学生")
p3 = Person("Baikal", 26, "老师")
my_list = [p1, p2, p3]
for p in my_list:
    print(p)
# 思路分析
"""
1.解决方案:冒泡排序 根据需求做了改进
2.解决方案:直接使用列表的sort方法
"""


def bubble_sort(my_list: list[Person]):
    """_summary_
    # 功能:对传入的列表进行排序,从大到小或者从小到大(按照年龄)
    Args:
        my_list (_type_): _description_ 传入的列表
        :return 无返回值
    """
    """
    通过分析此我们发现每一轮的比较逻辑是一样的
    我们只需要考虑变化的部分即可,使用外层的for循环来处理
    """
    # !使用i变量来控制多少轮排序 len(my_list)-1
    for i in range(0, len(my_list) - 1):
        for j in range(0, len(my_list) - 1 - i):
            # 如果前面的元素的年龄小于后面的元素的年龄就交换
            if my_list[j].age < my_list[j + 1].age:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


# bubble_sort(my_list)
print("排序后".center(32, "-"))

for p in my_list:
    print(p)


# 解决方案:冒泡排序 根据需求做了改进
"""
1.key=lambda ele: ele.age 表示我指定按照列表元素的age属性进行排序
2. reverse=True 表示逆序， reverse=False 表示顺序
"""
my_list.sort(key=lambda ele: ele.name, reverse=True)
print("排序后".center(32, "-"))
for p in my_list:
    print(p)


# ? 有三个类,Grand,Father,和Son,问父类和子类中通过self和super()都可以调用那些属性和方法
class Grand:
    """
    Grand类
    """

    name = "AA"
    __age = 100

    def g1(self):
        print("Grand-g1()")


class Father(Grand):
    id = "001"
    __score = None

    def f1(self):
        """
        :return
        """
        # super()可以访问那些成员(属性和方法)
        super().name
        super().g1()
        # self可以访问那些成员
        self.id
        self.f1()
        self.name
        self.g1()
        print("Father-f1()...")


# son类
class Son(Father):
    name = "BB"

    def g1(self):
        print("Son-g1()")

    def __show(self):
        # super()可以访问那些成员(属性和方法)
        super().id
        super().name
        super().f1()
        super().g1()
        # self可以访问那些成员
        self.name
        self.g1()
        self.__show()
        self.id
        self.f1()
        print("Son-__show()...")

    # def h1(self):
    #     self.__show()


# !思路分析继承关系 Son->Father->Grand


# ?编写Doctor类,属性:name,age,job,gender,sal,5个参数的构造器,重写__eq__()方法,并判断测试类中创建的两个对象是否相等(相等就是判断属性是否相同)
class Doctor:
    def __init__(self, name, age, job, gender, sal):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender
        self.sal = sal

    # 重新__eq__
    def __eq__(self, other):
        # 如果other类型不是Doctor直接返回false
        if not isinstance(other, Doctor):
            return False
        # 如果所有的属性都相同,就返回True
        return (
            self.job == other.job
            and self.sal == other.sal
            and self.age == other.age
            and self.job == other.job
            and self.gender == other.gender
            and self.name == other.name
        )


# 测试
doctor1 = Doctor("king", 20, "牙科医生", "男", 10000)
doctor2 = Doctor("king", 20, "牙科医生", "男", 10000)
print("doctor1 == doctor2", doctor1 == doctor2)
