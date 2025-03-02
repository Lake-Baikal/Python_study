#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :06.+号的使用.py
# @Time      :2024/03/16 20:23:42
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!当+两边都是数值型时，则作加法运算
!当+两边都是字符串时，则作拼接运算
"""
name = 'Baikal'
score = 50.8
print(score + 90)  # 加法运算
print(name + " hi")  # 字符串拼接
print("100" + "98")  # 加引号两个字符串拼接
print(34.5 + 100)  # 数值相加
# print("100" + 3)  # 报错，不允许数值和字符串相加，类型不符合

