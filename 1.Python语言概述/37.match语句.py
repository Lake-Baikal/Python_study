#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   37.match语句.py
@Time    :   2025/02/02 01:23:50
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# !语法
'''
match <表达式>:
     case <值1>:
          <语句块1>
     case <值2>:
          <语句块2>
    case _:
          <语句块3>
语法二
match <表达式>:
     case <值1>:
          <语句块1>
     case <值2> | <值3> | <值4>:
          <语句块2>
    case_:
          <语句块3>  #匹配不到任何模式时的默认情况(类似else)
'''
# match 语句接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较。
# match 语句语意,计算表达式的值,依次匹配case 后面的值,一旦匹配到,就执行对应的语句块,语句块结束.
# 如果所有的case都匹配不上就执行case_:对应的语句块,语句结束,下划线_代表匹配所有的情况,及默认情况
# case后必须跟"字面量",也就是说,不能是表达式

# command = input("请输入你的操作")

# match command:
#     case "start":
#         print("开始执行了")
#     case "stop":
#         print("暂停执行了")
#     case "restart":
#         print("重置")
#     case _:
#         print("没有匹配")

# score = float(input("请输入成绩"))

# match score:
#     case score if score >= 60:
#         print("及格了")
#     case _:
#         print("成绩不合格")


# match-case的高级使用
# ! match-case不仅可以匹配简单的常量,还可以进行更加复杂的模式匹配,包括列表,元组,集合和字典,类
# x = int(input("请输入x的坐标值"))
# y = int(input("请输入y的坐标值"))

# match (x, y):
#     case (0, 0):
#         print("您输入的坐标为原点:", x, y)
#     case (x, 0):
#         print(f"您输入在Y轴上面,X轴坐标为:{x}")
#     case (0, y):
#         print(f"您输入在x轴上面,Y轴坐标为:{y}")
#     case _:
#         print(f"您输入的坐标为原点:{x},{y}")

# 匹配字典,通过字典的键值对来匹配
name = "baikal"
age = 18
dic = {"name": name, "age": age}
match dic:
    case {"age": 18}:
        print("年龄为18", dic)
    case {"name": baikal}:
        print("名字为baikal", dic)
    case {"name": baikal, "age": 18}:
        print("名字为baikal,年龄为18", dic)


