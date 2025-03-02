#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.函数入门.py
# @Time      :2024/04/06 00:21:30
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# !为什么需要函数
# # 案例:输入两个数字,在输入一个运算符(+,-,*,/)得到结果
# # 1.接收用户的输入
# n1 = float(input("请输入一个数字"))
# n2 = float(input("请输入一个数字"))
# oper = input("请输入运算符+,-,*,/:")
# # 统计结果
# res = 0.0
# # 多分支的判断
# if oper == "+":
#     res = n1 + n2
# elif oper == "-":
#     res = n1 - n2
# elif oper == "*":
#     res = n1 * n2
# elif oper == "/":
#     res == n1 / n2
# else:
#     print("请输入正确的符号")
# print(n1, oper, n2, "=", res)
# # 如果第二次还需要计算,该怎么办(复制代码)
# # 或者在其他文件中也有这样的需求怎么办(复制代码)
# n1 = float(input("请输入一个数字"))
# n2 = float(input("请输入一个数字"))
# oper = input("请输入运算符+,-,*,/:")
# # 统计结果
# res = 0.0
# # 多分支的判断
# if oper == "+":
#     res = n1 + n2
# elif oper == "-":
#     res = n1 - n2
# elif oper == "*":
#     res = n1 * n2
# elif oper == "/":
#     res == n1 / n2
# else:
#     print("请输入正确的符号")
# print(n1, oper, n2, "=", res)
"""
!缺点:
!1.代码冗余
!2.不利于代码维护
"""

# !函数:为完成某一功能的程序指令(语句)的集合,称为函数
# !在python中函数分为系统函数和自定义函数
# !内置函数和模块中提供的函数都是系统函数,有python提供
# !自定义函数是程序员根据业务需要开发的
# * 函数的好处
# 1.提高代码复用性
# 2.可以将实现的细节封装起来,然后供其他用户调用即可
# !基本语法


def max(a, b):
    if a > b:
        return a
    else:
        return b

# 函数的定义
# 函数代码块以def关键字开头,后接函数标识符名称和圆括号()
# 函数内容以:起始,并且缩进
# 函数参数(a,b),可以有多个,也可以没有即直接是(),(a,b)也称为形参列表
# 函数可以有返回值,也可以没有,如果没有return相当于返回None,None是内置常量,通常用来代表空值的对象


# !函数调用
# !函数定义好后,并不会自动执行,需要调用才会执行
# !调用方式:函数名(实参列表),比如max(10,20)
print(max(10, 20))

# 案例:定义一个cry函数,输出"小猫喵喵叫"
"""
思路分析:
1.函数名cry
2.形参列表:无()
3.函数体:完成输出小猫喵喵叫
"""


def cry():
    print("小猫喵喵叫")


# 调用函数:就是计算机找到cry这个函数从函数体第一句开始执行
cry()

# 自定义cal01函数,可以计算1+..+100的结果
"""
思路分析
1.函数名:cal01
2.形参列表:无()
3.函数体:完成计算1+..+1000的结果
"""


def cal01():
    total = 0
    for i in range(1, 1001):
        total += i
    print("total=", total)


cal01()
# 自定义cal02函数,该函数可以接收一个数n,计算1+..+n的结果
"""
1.函数名:cal02
2.形参列表:(n)
3.函数体:完成计算1+..+n的结果
"""


def cal02(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("total=", total)


"""
cal02(3)就是调用函数cal02
(3)表示我调用函数时,传入了实参3,即把3赋值给n
"""
cal02(3)

# 案例: 自定义get_sum函数,可以计算两个数的和,并返回结果
"""
1.函数名:get_sum
2.形参列表:(num1,num2)
3.函数体:可以计算两个数的和,并返回结果
"""


def get_sum(num1, num2):
    # total = num1 + num2
    # return total
    return num1 + num2


"""
1.get_sum(10, 20)调用get_sum
2.(10, 20)表示传入了两个实参10,50,把10赋值给num1,把20赋值给num2
3.result就是接收get_sum()函数返回的结果
"""
result = get_sum(10, 20)
print(result)


# 案例使用函数解决前面的计算问题
def cal04():
    n1 = float(input("请输入一个数字"))
    n2 = float(input("请输入一个数字"))
    oper = input("请输入运算符+,-,*,/,//:")
    # 统计结果
    res = 0.0
    # 多分支的判断
    if oper == "+":
        res = n1 + n2
    elif oper == "-":
        res = n1 - n2
    elif oper == "*":
        res = n1 * n2
    elif oper == "/":
        res == n1 / n2
    elif oper == "//":
        res == n1 // n2   
    else:
        print("请输入正确的符号")
    print(n1, oper, n2, "=", res)


cal04()
# 如果还有这样的需求,调用cal04()即可
cal04()
