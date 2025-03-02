#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :10.str_detail.py
# @Time      :2024/03/17 13:12:16
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 字符串是Python中很常用的数据类型，通俗来说，字符串是字符组成的一串内容
# 使用引号('或者")包括起来，创建字符串
# str就是String的缩写，在使用type()查看数据类型时，字符串类型显示的就是str
# 字符串使用的注意事项
str1 = 'baikal说:"hello"'
print(str1)
str2 = "jack说:'hi'"
print(str2)
print(f"str2的数据类型{type(str2)}")

# 通过+可以拼接字符串
print("hi" + " tom")

# !Python中不支持单字符类型，单字符在Python中也是作为一个字符串使用
str3 = "A"
print("str3的类型是:", type(str3))

# !用三个单引号 '''内容''',或者三个双引号 """内容"""可以使字符串内容保持原样输出
# !在输出格式复杂的内容是比较有用的，比如输出一段代码,保留原格式
content = '''
Python的字符串只能存储少量的数据，且数据类型太单一。在我们储存大量数据或多种数据类型时，会选择使用列表。

列表以[]括起来，用逗号分隔，里面可以存放各种数据类型，每个位置代表一个元素。

常见的列表操作有：增加、插入、删除、查询等。

增加：在列表最后一个位置添加一个内容。
'''
print(content)
# !在字符串前面加 r 可以使得整个字符串不被转义
str4 = r"jack\ntome\tking"
print(str4)
