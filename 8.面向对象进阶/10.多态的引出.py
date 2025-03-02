#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   10.多态的引出.py
@Time    :   2025/02/18 22:39:33
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# 多态的引出
# ? 请编写一个程序,Master类中有一个feed方法(喂食)方法,可以完成主人给动物喂食的信息
# 请用传统的方法解决
"""
Master类:主人类
Food食物类 :子类->fish鱼肉类 Bone:骨头类
Animal动物类:Cat猫类,Dog 狗类
"""


class Food:
    name = None

    def __init__(self, name):
        self.name = name


class Fish(Food):
    # 特有的属性和方法
    pass


class Bone(Food):
    # 特有的属性和方法
    pass


class Animal:
    name = None

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Master:
    name = None

    def __init__(self, name):
        self.name = name

    # 给猫喂fish
    def feed_cat(self, cat: Cat, fish: Fish):
        print(f"主人{self.name} 给动物:{cat.name}喂的食物是{fish.name}")

    # 给狗喂bond
    def feed_dog(self, dog: Dog, bone: Bone):
        print(f"主人{self.name} 给动物:{dog.name}喂的食物是{bone.name}")


# 测试
master = Master("Baikal")
cat = Cat("花猫")
fish = Fish("黄花鱼")
dog = Dog("边牧")
bone = Bone("大棒骨")
master.feed_cat(cat, fish)
master.feed_dog(dog, bone)
# 问题分析
# 问题是代码的复用性不高,而且不利于代码的维护和功能拓展
# 问题解决:引出我们要讲的多态
