#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.数据容器概述.py
# @Time      :2024/04/22 00:05:02
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 为什么需要数据容器
# ?一只养鸡场有6只鸡,它们的体重分别是3kg,5kg,1kg,3.4kg,2kg,50kg.请问这六只鸡的总体重是多少?平均体重是多少
hen1 = 3
hen2 = 5
hen3 = 1
hen4 = 3.4
hen5 = 2
hen6 = 50
# 计算总的体重
total_weight = hen1 + hen2 + hen3 + hen4 + hen5 + hen6
# 计算平均体重
avg_weight = total_weight / 6
print(f"总体重:{total_weight},平均体重:{round(avg_weight, 2)}")
"""
1.如果不是6只鸡,而是600只鸡怎么办
2.不利于代码维护,不灵活
3.引出列表知识点
"""
"""
!1.数据容器是一种数据类型,有些地方也简称为容器/collections
!2.数据容器可以存放多个容器,每个数据也称为一个元素
!3.存放的数据和元素可以是任意类型
!4.数据容器就是一种可以存放多个数据/元素的数据类型
!5.分类:列表list,元组tuple,字符串str,集合set,字典dict
"""
