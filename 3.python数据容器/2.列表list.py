#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2.列表list.py
# @Time      :2024/04/22 00:05:18
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 1.列表可以存放多个不同类型数据,即列表就是一列数据(多个数据)
# 2.列表也是一种数据类型
# 3.列表中的每一个数据称为元素

# !列表的定义:创建一个列表,只要用逗号分隔的不同的数据项使用方括号括起来即可
list1 = [100, 200, 300, 400, 500]
list2 = ["red", "green", "blue", "yellow", "while", "black"]
print(list)  # 输出列表的所有数据项(元素)
print(type(list1))  # 输出列表的数据类型

# !列表的使用语法:列表名[索引]
# !注意索引是从0开始计算
# 比如使用list2列表的第三个值“blue”,则通过list2[2]就可以访问到
print("第三个元素:", list2[2])

# !列表的遍历:就是将列表的每个元素依次取出,进行处理的操作,就是遍历/迭代
list_color = ["red", "green", "blue", "yellow", "while", "black"]
# while循环遍历列表
"""
! 1.先定义变量index = 0,表示从第一个元素开始取出
! 2.列表list_color的个数6,这里其实有一个内置函数len(列表),可以返回个数
! 3.每取出一个就输出/或者自己的业务处理
"""
# !得到list元素个数
# print(len(list_color))

# 1.先定义变量index = 0,表示从第一个元素开始取出
index = 0
while index < len(list_color):
    print(f"第{index+1}个元素是{list_color[index]}")
    index += 1

# for循环遍历列表
"""
! 因为for循环是直接从列表中依次取出,所以直接操作即可
! 每取出一个就输出/或者自己的业务处理
"""
list_color = ["red", "green", "blue", "yellow", "while", "black"]
for element in list_color:
    print(f"元素是:{element}")

# 列表解决养鸡场问题
# ?一只养鸡场有6只鸡,它们的体重分别是3kg,5kg,1kg,3.4kg,2kg,50kg.请问这六只鸡的总体重是多少?平均体重是多少?
hens = [3, 5, 1, 3.4, 2, 50]
# 计算总体重
total_weight = 0.0
# 遍历hens
for elements in hens:
    # 累加
    total_weight += elements
print(f"总体重:{total_weight}平均体重:{round(total_weight/len(hens), 2)}")
