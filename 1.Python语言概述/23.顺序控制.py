#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :23.顺序控制.py
# @Time      :2024/03/24 16:50:46
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
顺序控制就是程序从上到下依次执行,中间没有任何判断和跳转
"""
print("start------")
print("小明去上学")
print("小明上学中")
print("小明放学了")
print("end--------")
# Python在定义变量时采取了合法的前向引用，必须先定义变量在使用变量
# 正确
# num1 = 20
# num2 = 10 + num1
# print(num2)

# 错误
# num2 = num1 + 2
# num1 = 30
# print(num2)



