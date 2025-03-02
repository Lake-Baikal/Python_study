#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :33.continue语句.py
# @Time      :2024/04/05 00:08:34
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!continue语句是for或者while循环所嵌套的代码中的
!continue语句用于结束本次循环,继续执行循环的下次轮次
!继续执行的是该continue最近是外层循环的下一次轮次
!在循环体中,如果执行continue就会结束本次循环,去执行while语句的判断条件(即下一轮的循环) 注意不会退出while循环
"""

i = 1
while i <= 4:
    i += 1
    if i == 3:
        continue
    print("i=", i)

# 代码阅读
for i in range(0, 13):
    if i == 10:
        continue
    print("i=", i)

for i in range(0, 2):
    for j in range(1, 4):
        if j == 2:
            continue
        print("i=", i, "j=", j)
