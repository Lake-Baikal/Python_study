#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   7.作用域.py
@Time    :   2025/01/29 00:19:25
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''


# 1.在面向对象的编程中,主要的变量就是成员变量(属性)和局部变量
# class Cat:
#     # 属性
#     name = None
#     age = None

#     # n1,n2,result就是局部变量
#     def cal(self, n1, n2):
#         result = n1 + n2
#         print(f"result={result}")


# 2.我们说的局部变量,一般就是指在成员方法中定义的方法
# 3.作用域的分类:属性作用域为整个类,比如Cat: cry eat 等方法使用属性
# class Cat:
#     # 属性
#     name = None
#     age = None

#     def cal(self, n1, n2):
#         result = n1 + n2
#         print(f"result={result}")
#         print(f"cal()使用属性name{self.name}")

#     def cry(self):
#         print(f"cry()使用属性name{self.name}")

#     def eat(self):
#         print(f"eat()使用属性name{self.name}")


# cat = Cat()
# cat.cal(10, 20)
# cat.cry()
# cat.eat()
# 4.局部变量:也就是方法中定义的变量,作用域实在他的方法中
# class Cat:
#     # 属性
#     name = None
#     age = None

#     def cal(self, n1, n2):
#         result = n1 + n2
#         print(f"result={result}")
#         print(f"cal()使用属性name{self.name}")

#     def cry(self):
#         print(f"cry()使用属性name{self.name}")

#     def eat(self):
#         print(f"eat()使用属性name{self.name}")


# cat = Cat()
# cat.cal(10, 20)
# cat.cry()
# cat.eat()


# 5.属性和局部变量可以重名,访问时带上self,表示访问的属性,没有带self,则是访问局部变量
class Cat:
    # 属性
    name = None
    age = None

    def hi(self):
        name = '皮皮'
        print(f"name={name}")
        print(f"name={self.name}")


cat = Cat()
cat.name = "Baikal"
print("-" * 60)
cat.hi()
