#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :5.元组tuple.py
# @Time      :2024/04/28 23:12:52
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
! 元组(tuple)可以存放多个不同类型数据,元组是不可变序列
! 元组不可变是指当你创建tuple时,他就不能改变了
!也就是说它没有append(),insert()这样的方法,但它也有获取某个索引值的方法,但是不能重新赋值
!语法:创建一个元组,只要把逗号分隔不同的数据项,使用圆括号括起来
"""
tuple_a = (100, 200, 300, 400, 600)
tuple_b = ('red', 'blue', 'yellow', 'orange', 'white', 'black')
print(f"元组的内容是{tuple_a},类型是{type(tuple_a)}")

# !元组的使用 元组名[索引]
# !注意索引从0开始
print(f"获取第三个元素:{tuple_b[2]}")
"""
?元组的遍历:
!简单来说,就是将元组的每个元素依次取出,进行处理的操作,就是遍历/迭代
"""
# 1.使用while循环对元组进行遍历输出
tuple_color = ('red', 'blue', 'yellow', 'orange', 'white', 'black')

# index = 0表示从第一个元素进行遍历
index = 0
while index < len(tuple_color):
    print(f"第{index+1}个元素的值:{tuple_color[index]}")
    index += 1

# 使用for循环对元组进行遍历输出

for element in tuple_color:
    print(f"元素是{element}")
