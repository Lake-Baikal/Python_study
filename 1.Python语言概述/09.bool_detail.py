#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :09.bool_detail.py
# @Time      :2024/03/17 09:47:05
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 布尔类型也叫bool类型,取值是True 和 False
# True和False是关键字，表示布尔值
# 布尔类型适用于逻辑运算，一般用于流程控制语句

num1 = 100
num2 = 200
if num1 < num2:
    print("true")
else:
    print("false")

# 表示把num1 >num2的结果赋值给result变量
result = num1 > num2
print("result =", result)

# 看看resule的数据类型
print(f"result的数据类型{type(result)}")
print(type(1 > -1))
"""
!布尔类型只有两个值,True和False
!布尔类型可以和其他数据类型进行比较，比如数字，字符串。
!在比较时,Python会将True视为1,False视为0
"""
b1 = False
b2 = True
print(b1 + 10)
print(b2 + 10)

# b1 = 0  表示赋值，把0赋值给b
# b2 == 0 表示判断b1是否和0相等
if b1 == 0:
    print("ok")

if b2 == 1:
    print("Hi")
# !在Python中，非0被视为真值，0被视为假值
if 0:
    print("哈哈")
if -1:
    print("嘻嘻")
if "baikal":
    print("baikal你好")
