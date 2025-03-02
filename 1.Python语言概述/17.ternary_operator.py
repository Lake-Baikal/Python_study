#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :17.ternary_operator.py
# @Time      :2024/03/22 22:05:33
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# 三元运算符
"""
!1.python是一种极简主义的编程语言,他没有引入?:这个运算符，而是使用if else关键字来实现相同的功能
!语法是: max = a if a > b else b
1.如果a>b成立,就把a作为整个表达式的值，并赋值给max
2.如果a<b成立,就把b作为整个表达式的值，并赋值给max
"""
# 比较两个数最大值，最小值
a = 80
b = 10
max = a if a > b else b
print(f"max={max}")
min = a if a < b else b
print(f"min={min}")
# 比较三个数最大值，最小值
"""
1.a,b,c三个数
2.先求出a,b的最大值max1
3.在求出max1和c的最大值 max2
"""
a = 50
b = 30
c = -1

max1 = a if a > b else b
max2 = max1 if max1 > c else c
print("max2=", max2)

# 一条语句完成,支持嵌套使用，可读性差，不推荐
max = (a if a > b else b) if (a if a > b else b) > c else c

# 运算符有不同的优先级,所谓优先级就是表达式的运算顺序
# 运算符优先级 从左到右由高到低
# ! 算数运算->位运算->比较运算->逻辑运算->赋值运算
# ! 加小括号的表达式优先级最高
