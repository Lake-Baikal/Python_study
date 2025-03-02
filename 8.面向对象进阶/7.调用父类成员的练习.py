#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   7.调用父类成员的练习.py
@Time    :   2025/02/16 13:55:12
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


class A:
    n1 = 300
    n2 = 500
    n3 = 600

    def fly(self):
        print("A-fly...")


class B(A):
    n1 = 200
    n2 = 400

    def fly(self):
        print("B-fly()...")


class C(B):
    n1 = 100

    def fly(self):
        print("C-fly()...")

    def say(self):
        print(self.n1)  # 100
        print(self.n2)  # 400
        print(self.n3)  # 600
        print(super().n1)  # 200
        print(B.n1)  # 200
        print(self.n2)  # 400

        # 针对上面的程序，想在C的say()中，调用C的fly()和A的fly()应该如何调用
        self.fly()
        A.fly(self)
        super(B, self).fly()


c = C()
c.say()
