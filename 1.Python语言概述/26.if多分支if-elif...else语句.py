#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :26.if多分支if-elif...else语句.py
# @Time      :2024/03/26 21:53:56
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# 多分支语句相当于多选一
"""
基本语法
if 条件表达式:
   执行代码块1
elif 条件表达式2:
   执行代码块2
...... 此处省略多个elif语句
else:
   执行代码块n+1

1.如果条件表达式1成立,执行代码块1
2.如果条件表达式1不成立,才去判断条件表达式2是否成立
3.如果条件表达式2成立,就执行代码块2
4.以此类推,如果所有的表达式都不成立,则执行else代码块
"""
"""
案例:判断成绩可以拿到什么样的奖励
如果成绩为100分时奖励Macbook pro14
如果成绩为(80,99]奖励ipad
如果成绩为[60,80]奖励iphone
其他什么都不奖励
请从键盘输入成绩加以判断
"""
# !案例分析
# 定义变量接收成绩score,整数类型注意转换int
# 根据成绩进行判断,输出相应的提示信息即可
# 使用多分支语句
score = int(input("请输入您的成绩(整数):"))
if 0 >= score <= 100:
    if score == 100:
        print("奖励Macbook pro14")
    elif 80 > score <= 99:
        print("奖励ipad")
    elif 60 >= score <= 80:
        print("奖励iphone")
    else:
        print("什么都不奖励")
else:
    print("您输入的成绩不在0~100范围")
# !在Python中支持这样的一种链式比较 80 >= score <= 99
# 案例二分析代码说出结果
b = True
if b == 0:
    print("a")
elif b:
    print("b")
elif not b:
    print("c")
else:
    print("d")

# 案例三:择偶
"""
男大当婚,女大当嫁,那么女方家嫁女儿一定会有条件
男方:身高180,财富千万,帅:是。
条件从控制台输入
如果同时满足这三个条件,女方:我一定嫁给他
如果有一个条件为真,则嫁吧,女方:比上不足比下有余
如果一个条件都不满足,则不嫁。

"""
# 思路分析
# 1.定义三个变量height , money ,handsome
# 2.根据题干分析需要使用多分支判断,输出相应的提示
height = float(input("请输入身高(cm)"))
money = float(input("资产(万)"))
handsome = input("颜值(帅,不帅)")

if height > 180 and money > 1000 and handsome == "帅":
    print("我一定嫁给他")
elif height > 180 or money > 1000 or handsome == "帅":
    print("嫁吧,比上不足比下有余")
else:
    print("不嫁")
