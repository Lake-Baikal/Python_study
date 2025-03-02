#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   11.多态.py
@Time    :   2025/02/18 21:19:57
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# !怎么理解多态
# >1.多态顾名思义即多种状态,不同的状态调用相同的方法,表现出不同的状态，称为多态
# 2.多态通常作用在继承关系上。
# !3.一个父类，具有多个子类，不同的子类对象调用相同的方法,执行的时候产生不同的状态,就是多态
class Animal:
    def cry(self):
        pass


class Cat(Animal):
    def cry(self):
        print("小猫喵喵叫")


class Dog(Animal):
    def cry(self):
        print("小狗汪汪叫")


class Pig(Animal):
    def cry(self):
        print("小猪噜噜叫")


class Bird(Animal):
    def cry(self):
        print("小鸟喳喳叫")


# ! 在Python面向对象编程中,子类对象可以传递给父类类型
def func(animal: Animal):
    print(f"animal类型是{type(animal)}")
    animal.cry()


# 创建三个对象
cat = Cat()
dog = Dog()
pig = Pig()
bird = Bird()
# 调用函数
func(cat)
func(dog)
func(pig)
func(bird)

# !多态的好处
"""
1.增加了程序的灵活性,以不变应万变,使用者都是同一种形式去调用,如func(animal)
2.增加了程序的可扩展性,通过继承Animal类创建了一个新的类,使用者无需更改自己的代码,还是使用func(animal)去调用
"""

# Python多态的特点
# ! Python中函数/方法的参数是没有类型限制的,所以多态在Python中的体现并不是很严谨,比如和java等强类型语言对比
# ! Python并不要求严格的继承体系,关注的不是对象的类型本身,而是他是否具有要调用的方法(行为


class AA:
    def hi(self):
        print("AA-hi()...")


class BB:
    def hi(self):
        print("BB-hi...")


def test(obj):
    obj.hi()


aa = AA()
bb = BB()
test(aa)
test(bb)


# !使用多态的特性优化程序
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


class Grass(Food):
    pass


class Animal:
    name = None

    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Horse(Animal):
    pass


class Master:
    name = None

    def __init__(self, name):
        self.name = name

    # 给猫喂fish
    # def feed_cat(self, cat: Cat, fish: Fish):
    #     print(f"主人{self.name} 给动物:{cat.name}喂的食物是{fish.name}")

    # 给狗喂bond
    # def feed_dog(self, dog: Dog, bone: Bone):
    #     print(f"主人{self.name} 给动物:{dog.name}喂的食物是{bone.name}")
    # 主人给动物喂食物
    def feed(self, animal: Animal, food: Food):
        print(f"主人{self.name} 给动物:{animal.name}喂的食物是{food.name}")


# 测试
master = Master("Baikal")
cat = Cat("花猫")
fish = Fish("黄花鱼")
dog = Dog("边牧")
bone = Bone("大棒骨")
horse = Horse("小马")
grass = Grass("青草")
# master.feed_cat(cat, fish)
# master.feed_dog(dog, bone)
master.feed(cat, fish)
master.feed(dog, bone)
master.feed(horse, grass)


# 可以扩展一下Horse,Grass,体会多态的机制,带来的好处
