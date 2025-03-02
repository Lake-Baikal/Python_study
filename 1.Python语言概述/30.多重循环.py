#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :30.多重循环.py
# @Time      :2024/04/02 23:44:11
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!重点
!多重循环就是将一个循环放在另一个循环体内,就形成了嵌套循环,其中for循环,while循环均可以作为外层循环和内层循环.
!实质上,嵌套循环就是把内层循环当成外层循环的循环体
!如果外层循环次数m次,内层为n次,则内层循环体实际上需要执行m*n次
"""
# for i in [0, 1]:
#     for j in [0, 1, 2]:
#         print("i=", i, "j=", j)

# for i in range(2):
#     for j in range(3):
#         print("i=", i, "j=", j)

# count = 0
# for i in range(3):
#     for j in range(5):
#         for k in range(2):
#             count += 1
#             print("ok", count)
"""
!案例:打印金字塔,编写一个程序,可以接收一个整数,表示层数,打印空心金字塔
先死后活
1.我们先不考虑层数的变化,假定就5层,后面做活
化繁为简
1.打印矩形
2.打印直角三角形
3.打印金字塔
4.打印空心金字塔
"""
# 1.打印矩形
"""
*****
*****
*****
*****
*****
"""
# i用来控制层数
# j用来控制每层输出*号的个数
# for i in range(1, 6):
#     for j in range(1, 6):
#         # 这里的end=""表示输出不换行
#         print("*", end="")
#         # 每次输出后换行
#     print("\n")

# !打印直角三角形
"""
*
**
***
****
*****
"""
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         # 这里的end=""表示输出不换行
#         print("*", end="")
#         # 每次输出后换行
#     print("\n")

# for i in range(1, 6):
#     for j in range(i):
#         # 这里的end=""表示输出不换行
#         print("*", end="")
#         # 每次输出后换行
#     print("\n")

# !3.打印金字塔
"""
        *     1层:1个星2*1-1 空格 4  5-1
       ***    2层:3个星2*2-1 空格 3  5-2
      *****   3层:5个星2*3-1 空格 2  5-3
     *******  4层:7个星2*4-1 空格 1  5-4
    ********* 5层:9个星2*5-1 空格 0  5-5
"""

# for i in range(1, 6):
#     # k:输出空格数 5-层数就是空格数
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         # 这里的end=""表示输出不换行
#         print("*", end="")
#         # 每次输出后换行
#     print("\n")

# 打印空心金字塔,每层的两边输出*和最后一层输出*
#     *
#    * *
#   *   *
#  *     *
# *********

# for i in range(1, 6):
#     # k:输出空格数
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * (i - 1) or i == 5:  # 第五层输出*
#             # 这里的end=""表示输出不换行
#             print("*", end="")
#         else:
#             print(" ", end="")
#             # 每次输出后换行
#     print("\n")

# 可以接收一个整数,表示层数
# total_level = 15
# for i in range(1, total_level + 1):
#     # k:输出空格数
#     for k in range(total_level - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         if j == 0 or j == 2 * (i - 1) or i == total_level:
#             # 这里的end=""表示输出不换行
#             print("*", end="")
#         else:
#             print(" ", end="")
#             # 每次输出后换行
#     print("\n")

# 作业打印空心菱形
#     *

#    * *

#   *   *

#  *     *

# *       *

#  *     *

#   *   *

#    * *

#     *

# for i in range(1, 6):
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):

#         if j == 0 or j == 2 * (i - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n")

# *******  7
#  *****   5
#   ***    3
#    *     1

# for i in range(1, 5):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(2 * (5 - i) - 1):
#         if j == 0 or j == 2 * (5 - i) - 2 or i == 4:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("\n")

# 使用while实现
#     *
#    * *
#   *   *
#  *     *
# *********

line = 5
i = 1
while i <= line:
    k = 1
    while k <= line - i:
        print(" ", end="")
        k += 1
    j = 1
    while j <= (2 * i) - 1:
        if j == 1 or j == (2 * i) - 1 or i == line:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    i += 1
    print("\n")
