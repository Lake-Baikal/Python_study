#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2.对象形式和传递机制.py
# @Time      :2025/01/14 22:13:45
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
1.类是抽象的,概念的,代表一类事物,比如人类,猫类,...即他是数据类型
2.对象是具体的, 实际的,代表一个具体的事物,即实例
3.类是对象的模板,对象是类的一个个体,对应一个实例
"""


# !对象在内存中存在的形式
# 1.定义Cat类
class Cat:
    # 属性列表age,name,color
    age = None  # 年龄属性
    name = None  # 名字属性
    color = None  # 颜色属性
    weight = None  # 体重属性


# 2.通过Cat类来创建实例对象
cat1 = Cat()
# 通过对象名.属性名,可以给各个属性赋值
cat1.name = "小白"
cat1.age = 2
cat1.color = "白色"
cat1.weight = 3
# 通过对象名.属性名可以访问到属性
print(
    f"cat1的信息为:name:{cat1.name} age:{cat1.age} color:{cat1.color} 体重{cat1.weight}"
)
"""
!属性和成员变量
1.类中定义的属性(变量),我们也称为成员变量
2.属性是类的一个组成部分,一般是字符串,数值,也可是其他类型(list,dict等),比如前面定义的Cat类的name,age就是属性
!注意事项
属性的定义语法同变量, 属性名 = 值 ,如果没有值,可以赋值None
!None是Python的内置常量,通常用来代表空值的对象
3.如果给属性指定的有值,那么创建的对象,属性就有值
"""


class Cat:
    age = 2
    name = "小白"
    color = "white"


cat1 = Cat()
cat1.age = 100  # 对age重新赋值则以自己赋值为主
print(f"cat1的信息为:name:{cat1.name} age:{cat1.age} color:{cat1.color}")

# !定义类的语法
"""
class 类名:
   属性
   行为
"""
# ! class是关键字,表示后面定义的是类
# ! 属性,即定义在类中的变量(成员变量)
# ! 行为,即定义在类中的函数(成员方法)

# !如何创建对象
"""
语法:对象名=类名()
如cat1=Cat()
"""
# !访问属性
"""
语法:对象名.属性名
cat1.name
cat1.age
cat1.color
cat1.weight=xxx 是给属性赋值
"""
"""
!对象的传递机制
我们定义一个Person类,包括名字,年龄
 1.p2.age是多少
 2.id(p1.name)和id(p2.name)是否相同
 3.画内存图
"""


class Person:
    age = None
    name = None


p1 = Person()
p1.age = 10
p1.name = "小明"
p2 = p1  # 把p1赋值给了p2:即让p2指向p1
print(p2.age)
print(f"p1.name地址:{id(p1.name)} p2.name的地址{id(p2.name)}")

# 练习
a = Person()
a.age = 10
a.name = "jack"
b = a
print(b.name)
b.age = 200
b = None
print(a.age)
# print(b.age) # 'NoneType' object has no attribute 'age'
print(type(b))  # !None是NoneType类型的唯一实例
