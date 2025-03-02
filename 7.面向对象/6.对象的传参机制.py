#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   6.对象的传参机制.py
@Time    :   2025/01/23 21:51:42
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# !对象的传参机制
class Person:
    name = None
    age = None


# 分析测试对象作为参数传递到函数/方法的机制
def f1(person):
    print(f"(2)person的地址:{id(person)}")
    person.name = "james"
    person.age += 1


# 创建对象p1
p1 = Person()
p1.name = "jordan"
p1.age = 21
print(f"(1)p1的地址是:{id(p1)} p1.name:{p1.name} p1.age:{p1.age}")
f1(p1)
print(f"(3)p1的地址是:{id(p1)} p1.name:{p1.name} p1.age:{p1.age}")
