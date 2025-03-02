#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :14.compare_operator.py
# @Time      :2024/03/21 20:35:22
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# 比较运算符
"""
!1.比较运算符的结果要么是True要么是False,不管多么复杂
!2.比较运算符组成的表达式，我们称为比较表达式,比如:a>b
"""
a = 9
b = 8
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)
flag = a > b
print("flag=", flag)
# is 判断两个变量引用对象是否为同一个
# is not 判断两个变量引用对象是否不同
print(a is b)
print(a is not b)
"""
True
True
False
False
False
True
flag= True
False
True
"""

str1 = "abc#"
str2 = "abc#"
print(str1 == str2)
print(str1 is str2)
