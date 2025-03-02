#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6.函数递归案例.py
# @Time      :2024/04/13 15:33:28
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# ? 请使用递归的方式求出斐波那契数1,1,2,3,5,8,13...给你一个整数n,求出它的值是多少.
"""
n=1 fbn=1
n=2 fbn=1
n=3 fbn=1+1=2
n=4 fbn=1+2=3
...
n=7 fbn=5+8=13

"""

# def fbn(n):
#     """_summary_
#     功能:返回n对应的斐波那契数

#   Args:
#       n (_type_): 接收一个整数 n>=1
#   Returns:
#       _type_: 返回斐波那契数
#   """
#     if n == 1 or n == 2:
#         return 1
#     # 如果n>2则对应的斐波那契数为n-1和n-2对应的斐波那契数的和
#     else:
#         return fbn(n - 1) + fbn(n - 2)

# # 完成调用
# print(fbn(7))

# ?猴子吃桃的问题,有一堆桃子,猴子第一天吃了其中的一半,并且再多吃一个,以后每天猴子都吃掉其中的一半,然后再多吃一个,当到第十天时,想再吃时,发现只有一个桃子了,问最初共有多少个桃子
"""
思路分析
1.day==10时有桃子数是1
2.day==9时 day9的桃子数/2-1=(day10+1)*2
3.day==8时 day8的桃子数/2-1=(day9+1)*2
4.day==7时 day7的桃子数/2-1=(day8+1)*2
"""

# 定义函数返回对应天数的桃子数
# def peach(day):
#     if day == 10:
#         return 1
#     # 如果1<=day<=10的范围就是从后一天开始推导
#     else:
#         return (peach(day + 1) + 1) * 2

# # 完成测试
# print(peach(1))

# ? 求函数值,已知f(1)=3,f(n)=2*fn(n-1)+1;请使用递归思想编程,求出f(n)的值
"""
思路分析:
1.这个题已经给出推导公式
2.我们翻译成代码即可
"""


def fn(n):
    if n == 1:
        return 3
    else:
        return 2 * fn(n - 1) + 1


print(fn(10))

