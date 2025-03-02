#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :9.匿名函数lambda.py
# @Time      :2024/04/14 14:12:08
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# !如果我们有这样的一个需求,需要将函数作为参数进行传递,但是这个函数只是用一次,这时我们考虑使用lambda匿名函数
# !函数的定义
"""
- def关键字,可以定义带有名称的函数,可以重复使用
- lambda关键字,可以定义匿名函数(无名称),匿名函数只能使用一次
- 匿名函数用于临时创建一个函数,只使用一次的场景
!语法:
lambda 形参列表: 函数体(一行代码)
lambda关键字,表示定义匿名函数
形参列表:比如num1,num2表示接收两个参数
函数体:完成的功能,只能写一行,不能写多行
"""
# 案例:编写一个函数,可以接收刚匿名函数和两个数,通过匿名函数计算,返回两个数的最大值


def f1(fun, num1, num2):
    """_summary_
    # 完成功能:调用fun返回num1和num2最大值
  Args:
      fun (_type_): 接收一个匿名函数
      num1 (_type_): _description_
      num2 (_type_): _description_
  Returns:
      _type_: _description_
  """
    print(f"fun类型: {type(fun)}")
    return fun(num1, num2)


# !1.lambda  a, b: a if a > b else b就是匿名函数
# !2.不需要return,运算结果就是返回值
max_val = f1(lambda a, b: a if a > b else b, 12, 10)
print(max_val)
