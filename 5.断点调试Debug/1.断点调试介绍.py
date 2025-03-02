#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.断点调试介绍.py
# @Time      :2025/01/09 20:58:19
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
!在开发中, 新手程序员在查找错误时,有经验的程序员会提示使用断点调试,一步一步查看源码执行的过程从而发现错误在哪里
! 1.断点调试是指在程序的某一行设置一个断电,调试时,程序运行到这一行就会停住,然后你可以一步一步往下调试,调试过程中可以看各个变量当前的值,
! 出错的话调试到出错的代码行即可显示错误,停下来找到错误分析从而找到这个bug
!断点调试是我们程序员必须掌握的技能,断点调试也能帮助我们进入到函数/方法内,学习别人是怎么样实现功能的,提高程序员的编程水平
"""

# ? 1.查看变量的变化情况 (F10:逐行执行代码)
# sum = 0
# # debug for循环过程
# for i in range(0, 10):
#     sum += i
#     print(f"i={i}")
#     print(f"sum={sum}")
# print("end...")

# ?查了list越界的异常 (F10:逐行执行代码)
# names_list = ["jordan", "kobe", "james", "Baikal"]
# i = 0
# # debug list索引越界
# while i <= len(names_list):
#     print(f"names_list:{i}={names_list[i]}")
#     i += 1


# ? 进入函数和方法体内(shift+f11)
def f2(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res


def f1(name):
    print(f"name={name} 1")
    print(f"name={name} 2")
    print(f"name={name} 3")
    print(f"name={name} 4")
    print(f"name={name} 5")
    r = f2(6)
    print(f"r={r}")
    print(f"name={name} 6")
    print(f"name={name} 7")
    print(f"name={name} 8")


f1("baikal")
print("end...")

# ?如何执行到下一个断点(F5快捷键)
# ! 1.直接执行到下一个断点
# ! 2.可以在debug的过程中动态下断电
