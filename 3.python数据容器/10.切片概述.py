#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :10.切片概述.py
# @Time      :2024/05/06 20:47:44
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
!什么是切片:从一个序列中,取出一个子序列,在实际开发中,经常对序列进行切片操作
!什么是序列:序列是指,内容连续,有序,可使用索引的一类数据容器
!前面学过的列表,元组,字符串都可视为序列
"""
# ?基本语法:
# !表示从序列中,从指定的起始索引开始,按照指定步长,依次取出元素,到指定结束索引为止,截取到一个新的序列
# !切片操作是前闭后开,也就是,[起始索引:结束索引:步长),即截取的子序列,包括起始索引,但不包括结束索引的部分
"""
!步长表示依次取出元素的间隔
!-步长为1:一个个取出元素
!-步长为2:每次跳过一个元素取出
!-步长为N:每次跳过N-1个元素取出
"""
# 对字符串切片
str = "hello,world"
# 需求:截取"hello"
str_slice = str[0:5:1]
print("str_slice:", str_slice)
# 对列表切片
list_a = ['tom', 'baikal', 'jack', 'alan', 'tom']
# 需求:截取"baikal","alan"
list_slice = list_a[1:4:2]
print("list_slice:", list_slice)
# 对元组切片
tuple_a = (100, 200, 300, 400, 500, 600)
# 截取(200,300,400,500)
tuple_slice = tuple_a[1:5:1]
print("tuple_slice", tuple_slice)

# !注意事项和使用细节
# !1.切片语法:序列[起始索引:结束索引:步长],起始索引如果不写,默认为0,结束索引如果不写,默认为截取到结尾,步长如果不写,默认为1
str = "hello,world"
str_slice01 = str[:5:1]
print("str_slice01->", str_slice01)
str_slice02 = str[1::1]
print("str_slice02->", str_slice02)
str_slice03 = str[::1]
print("str_slice03->", str_slice03)
str_slice04 = str[2:5:]
print("str_slice04->", str_slice04)
# !2.序列[起始索引:结束索引:步长]步长为负数表示反向取,同时注意起始索引和结束索引也要反向标记
str = '123456'
str_slice05 = str[-1::-1]
print("str_slice05->", str_slice05)
str_slice06 = str[-1:-6:-1]
print("str_slice06->", str_slice06)
# !3.切片操作并不会影响原序列,而是返回了一个序列
str = "ABCD"
str_slice07 = str[1:3:1]
print(f"str->{str}str_slice07->{str_slice07}")

# 案例定义列表list_name=["jack","lisa","baikal","smith","kobe"]
# 1.取出前三个名字
# 2.取出后三个名字,并且保持原来顺序

list_name = ["jack", "lisa", "baikal", "smith", "kobe"]
# slice_a = list_name[0:3:1]
slice_a = list_name[:3:]
print(slice_a)
# 思路分析
# 1.使用反向切片
# 2.步长-1 起始索引-1 结束索引-4
slice_b = list_name[-1:-4:-1]
slice_b.reverse()  # 对元素进行逆序操作
print(slice_b)

