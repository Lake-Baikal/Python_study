#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :34.return语句.py
# @Time      :2024/04/05 01:23:58
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!return使用在函数,表示跳出所在的函数
"""


# 案例阅读代码
# f1是一个函数
def f1():
    for i in range(1, 5):
        if i == 3:
            # return  #  结束整个函数,不输出print("结束了for循环") , 就是跳出函数,在那个地方调用就返回到那个地方
            # break
            continue
        print("i=", i)
    print("结束了for循环")


# 调用函数相当于执行f1()函数
f1()

# 案例
"""
某人有 100000元,每经过一次路口需要缴费,规则如下
当现金>50000时,每次需要交5%
当现金<=50000时,每次需要交1000
计算该人可以经过多少次路口,使用while-break方式完成
"""

# 思路分析
# 1.先定义变量,money=100000表示钱的数量
money = 100000
# 2.定义变量count=0用来统计经过多少个路口
count = 0
# 3.使用while无限循环,按照过路口的规则来减少money,直到不够过路口为止,break
while True:
    if money > 50000:
        count += 1
        money -= money * 0.05
    elif money >= 1000:
        count += 1
        money -= 1000
    else:
        break

# 4.最后输出count即可
print(f"可以经过{count}路口,剩余的钱为{money}")
