#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :15.bool_operator.py
# @Time      :2024/03/21 21:07:42
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# 逻辑运算符 与  或  非  and  or  not
"""
!1. and:  x and y 布尔“与” 如果x为False ,x and y 返回x的值,否则返回y的计算值。
and是一种短路运算符,只有当第一个值为True时才去验证第二个值
在Python中,非0被视为真值,0被视为假值
!2. or:  x or y 布尔“或” 如果x为True ,x or y 返回x的值,否则返回y的计算值。
or是一种短路运算符,只有当第一个值为False时才去验证第二个值,如果第一个为True时,就直接返回第一个值
!1. not:  not x  布尔“非” 如果x为True ,如果x是False返回True (取反)
"""
a = 10
b = 20
c = 0
print(a and b)  # 20
print(c and b)  # 0
print(a or b)  # 10
print(c or b)  # 20
print(not (a and b))  # False
print(not (c and b))  # True

a = 1
b = 99
print(a and b)  # 99
# 在Python中()括起来的运算优先级最高
print((a > b) and b)  # False
print((a < b) and b)  # 99

# and案例
score = 70
if score >= 60 and score <= 80:
    print("成绩不错")

# or案例
score = 70
if score <= 60 or score >= 80:
    print("hi~~")

a = 1
b = 99
print(a or b)  # 1
print((a > b) or b)  # 99
print((a < b) or b)  # True
# not案例
print("------------------")
a = 3
b = not (a > 3)
print(b)  # True
print(not False)  # True
print(not True)  # False
print(not 0)  # True
print(not "Hello World")  # False
print(not 1.99)  # False
print(not a)  # False
