#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.类于实例的关系.py
# @Time      :2025/01/14 21:17:31
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
# 张老太养了两只猫,一只名字叫小白,今年3岁.白色.还有一致叫小花,今年100岁,花色.
# 1.请编写一个程序,当用户输入小猫的名字时,就显示该猫的名字,年龄,颜色
# 2.如果用户输入的小猫的名字错误,则显示张老太没有这只猫.

# 方案一:单独定义变量的模块
# 小白的信息
xb_name = "小白"
xb_age = 3
xb_color = "白色"
# 小花的信息
xh_name = "小花"
xh_age = 100
xh_color = "花色"
# !问题是访问非常不方便

# 方案二 使用字典解决
xb_cat_dict = {"name": "小白", "age": 3, "color": "白色"}
xh_cat_dict = {"name": "小花", "age": 100, "color": "花色"}
# 访问
print(
    f"小白的信息name:{xb_cat_dict['name']},{xb_cat_dict['age']},{xb_cat_dict['color']}"
)

# !问题是相对第一种方法好很多,但是我希望小猫有一些行为,比如小猫叫,小猫吃等
# !换言之,就是目前只有小猫的信息,但是无法关联小猫的行为,也就是功能函数
# ? OOP编程就是面向对象的编程
# 一个程序就是一个世界
# !万物皆对象
# !快速入门面向对象解决张老太太的养猫案例
# 定义一个猫类: age,name,color是属性,或者称为成员变量
# Cat类就是你定义的一个新类型


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
# !小结:通过OOP方式解决问题可以更好的管理小猫的属性问题
