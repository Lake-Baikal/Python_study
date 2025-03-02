#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2.函数调用机制.py
# @Time      :2024/04/06 13:57:33
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
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
# ! 如果没有return相当于返回None,None是内置常量,通常用来代表空值的对象


def f1():
    print("hi")


r = f1()
print("r:", r, id(r))  # 输出None
