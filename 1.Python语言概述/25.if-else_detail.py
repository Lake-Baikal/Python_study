#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :25.if-else_detail.py
# @Time      :2024/03/24 23:20:14
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# if双分支语句
"""
!基本语法
if 条件表达式:
   执行代码块1
else:
   执行代码块2
if和else是关键字,是规定好的
当条件表达式成立,执行执行代码块1,如果不成立则执行代码块2,注意不可以少冒号:
"""
# 案例:编写一个程序,可以输入人的年龄,如果大于18岁则输入"你的年龄大于18岁,请对自己的行为负责",如果不成立则输出"这次放过你"
"""
思路:
1.定义变量age,接收用户输入(注意默认是字符串类型，要转换为整数)
2.使用if else语句判断即可
"""
age = int(input("请输入你的年龄"))
if age > 18:
    print("你的年龄大于18岁,请对自己的行为负责")
else:
    print("这次放过你")
# ! if else 双分支结构执行是一个二选一的过程,要么为真,要么为假,不可能两个都执行
# ! if语句执行完毕只是退出if else控制结构,不是退出程序
# 案例
x = 4
y = 1
if x > 2:  # true 执行下面代码
    if y > 2:  # false 不执行
        print(x + y)
    print("人生苦短,我学python")  # 属于if x > 2:这个代码块的所以执行，因为缩进是if x > 2:
else:
    print("x is", x)

x = 4
y = 1
if x < 2:
    if y > 2:
        print(x + y)
    print("人生苦短,我学python")
else:
    print("x is", x)
# 编写程序,定义两个整数变量,并赋值,判断两数之和,如果大于等于50,就打印hello word
"""
思路分析
1.定义两个变量并赋值,num1和num2
判断num1+num2是否>=50,用if单分支语句
"""
num1 = int(input("请输入一个整数"))
num2 = int(input("请再输入一个整数"))
if num1 + num2 >= 50:
    print("hello world")

# 编写程序,定义2个float型变量并赋值,如果第一个数大于10.0,且第二个数小于20.0,打印两数之和
"""
思路分析
1.定义两个变量并赋值,num3和num4
判断num3>10.0 and num4 < 20.0,用if单分支语句
根据判断结果输出num1+num2结果
"""
num3 = 11.0
num4 = 15.0
if num3 > 10.0 and num4 < 20.0:
    print(f"{num3}+{num4}={num3+num4}")

# 定义两个变量int类型,判断二者之和,是否能被3又能被5整除，打印提示信息
"""
1.定义两个变量并赋值,num5和num6
2.判断(num5+num6)%3==0 and (num5+num6)%5==0
3.输出结果,使用双分支结构
"""
num5 = 10
num6 = 5
if (num5 + num6) % 3 == 0 and (num5 + num6) % 5 == 0:
    print(f'{num5+num6}可以被3又能被5整除')
else:
    print(f'{num5+num6}不可以被3又能被5整除')

# 判断一个年份是否是闰年,闰年的条件是符合以下二者之一的,1.年份能被4整除但不能被100整除,或者能被400整除
"""
1.定义一个年份year变量并赋值
2.判断(year % 4 == 0 and year % 100 != 0) or year % 400 == 0
3.如果成立就是闰年,否则不是闰年
3.输出结果,使用双分支结构
"""
year = 2025
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year}该年份是闰年')
else:
    print(f'{year}不是闰年')
