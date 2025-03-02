#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :8.函数作为参数传递.py
# @Time      :2024/04/14 12:54:36
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
""" def f1(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


def f2(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return num1 + num2, max_val """
"""
?1.f1和f2都有对两个数求最大值的需求
?2.如果有更多的函数也有对两个数求最大值的需求,在每个函数都写一份相同的代码,会冗余,不利于维护
?3.解决方法:编写一个函数(该函数可以返回两个数的最大值)
?4.将该函数作为参数传给f1,f2 ->引出知识点函数作为参数传递
"""


# 定义一个函数返回两个数的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


def f1(fun, num1, num2):
    """_summary_
  功能:调用fun返回num1和num2的最大值
  Args:
      fun (_type_): fun表示接收一个函数
      num1 (_type_): 传入数
      num2 (_type_): 传入数
  Returns:
      _type_: 返回最大值
  """

    return fun(num1, num2)


def f2(fun, num1, num2):
    """_summary_
  # 功能:调用fun函数返回num1和num2的最大值,同时返回两个数的和
  Args:
      fun (_type_): _description_
      num1 (_type_): _description_
      num2 (_type_): _description_
  Returns:
      _type_: _description_
  """
    return num1 + num2, fun(num1, num2)


# 测试
print(f1(get_max_val, 10, 20))
x, y = f2(get_max_val, 10, 20)
print(x, y)


# !函数作为参数传递,传递的不是数据,而是业务逻辑
# !一个函数可以接收多个函数作为参数传入
def f3(my_fun, num1, num2, my_fun2):
    return my_fun(num1, num2), my_fun2(num1, num2)


def get_max_value(num1, num2):
    max_value = num1 if num1 > num2 else num2
    return max_value


def get_sum(num1, num2):
    return num1 + num2


print(f3(get_max_val, 130, 190, get_sum))
