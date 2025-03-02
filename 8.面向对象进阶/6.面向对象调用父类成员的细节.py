#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   6.面向对象调用父类成员的细节.py
@Time    :   2025/02/15 00:48:47
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# 如果子类和父类出现同名的成员,可以通过父类名,super()访问父类的成员
# 基本语法
"""
1.访问父类成员方式1
访问成员变量:父类名.成员变量
访问父类方法:父类名.成员方法(self)
2.访问父类成员方式2
访问成员变量:super().成员变量
访问父类方法:super().成员方法()
"""


# 案例
class A:
    n1 = 100

    def run(self):
        print("A-run()...")


class B(A):
    n1 = 200

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


# 注意事项
# 1.子类不能直接访问父类的私有成员
class A:
    n1 = 100
    # 私有属性
    __n2 = 600

    def run(self):
        print("A-run()...")

    # 私有方法
    def __jump(self):
        print("A-jump()...")


class B(A):
    def say(self):
        # 子类不能直接访问父类的私有成员
        # print(A.__n2)
        # print(super().n2)
        # A.jump(self)
        # super().jump()
        print("say()...")


b = B()
b.say()

# 访问不限于直接父类,而是建立从子类向上级父类的查找关系 A->B->Base


class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()...")


class A(Base):
    n1 = 100
    __n2 = 600

    def run(self):
        print("A-run()...")

    def __jump(self):
        print("A-jump()...")


class B(A):
    def fly(self):
        print("B-fly()...")

    def say(self):
        print("say()...")
        # 访问不仅限于直接父类,而是建立于从子类向上级类的查找关系,A->B->Base
        # Base.n3 表示直接访问Base类的n3属性
        # A.n3 表示直接访问A类的n3属性,A类没有,但是向上一级父类Base查找,有n3属性
        # super().n3 表示直接访问直接父类A类的n3属性,但是向上一级父类Base查找,有n3属性
        print(Base.n3, A.n3, super().n3)
        # Base.fly(self) 表示直接访问 Base的fly方法
        Base.fly(self)
        # A.fly(self) 表示直接访问 A类的fly方法->Base fly()
        A.fly(self)
        # super().fly() 表示访问直接父类的fly()方法->Base->fly()
        super().fly()
        # self.fly() 表示访问本类的fly()方法->Base->fly()
        self.fly()


b = B()
b.say()

# ! 3.建议使用super()的方式,因为如果使用父类名 方式,一但父类变化,类名需要统一修改,比较麻烦
