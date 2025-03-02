#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :5.函数的递归调用.py
# @Time      :2024/04/13 12:43:32
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# !函数的递归调用
# !递归就是函数自己调用自己,每次调用时传入不同的值
# !递归有助于编程者解决复杂的问题,同时可以让代码更加简洁
# 递归可以解决说明问题
"""
1.各种数学问题:8皇后问题,汉诺塔,阶乘问题,迷宫问题
2.各种算法中也会使用到递归:比如快排,归并排序,二分查找,分治算法
3.将用栈解决的问题->递归代码比较简洁
"""


def test(n):
    if n > 2:
        # 递归调用
        test(n - 1)
    print("n=", n)


# 调用执行
test(4)

# def test(n):
#     if n > 2:
#         # 递归调用
#         test(n - 1)
#     else:
#         print("n=", n)

# # 调用执行
# test(4)

# !阶乘,当执行factorial(4),返回值是多少?
# 1!的阶乘是1
# 5! = 5 × 4 × 3 × 2 × 1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return factorial(n - 1) * n

# # 执行
# print(factorial(4))
"""
!递归的重要规则
!1.执行一个函数时,就创建一个新的空间(栈空间)
!2.函数的变量是独立的,比如n变量
!3.递归必须向退出退出递归的条件逼近,否则就是无限递归,就会出现
RecursionError: maximum recursion depth exceeded
!当一个函数执行完毕,或者遇到return,就会返回,遵守谁调用,谁将结果返回给谁
"""

# 无限递归
# def test(n):
#     if n > 2:
#         # 递归调用
#         test(n)
#     print("n=", n)

# # 调用执行
# test(4)
