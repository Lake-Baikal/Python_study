#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :19.input_info.py
# @Time      :2024/03/23 12:43:20
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# 可以从控制台接收用户信息
# input()是内置函数
name = input("请输入姓名")
age = input("请输入年龄")
score = input("请输入分数")
print("\n输入信息如下")
print("name:", name)
print("age:", age)
print("score:", score)

# ! input()接收到的数据类型是str字符串类型
# print(10 + score)
print(type(age))
print(type(score))
# 如果我们希望对接收到的数据类型进行算数运算符，则需要进行类型转换
print(10 + float(score))

# 我们也可以在接收数据的时候直接转换成需要的类型
age = int(input("请输入年龄"))
print("age的类型是:", type(age))
