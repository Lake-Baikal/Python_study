#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3.对象的布尔值.py
# @Time      :2025/01/15 22:08:57
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
# !Python一切皆对象,所有的对象都有一个布尔值,通过内置函数bool()可以获得对象的布尔值
# !下面对象的布尔值为False
"""
False
数字0
None
空字符串
空列表
空字典
空元组
空集合
"""
print("---下面对象的布尔值为False---")
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

# !因为对象的布尔值都有一个布尔值,有一些代码直接使用对象的布尔值做判断
content = "hello"
if content:
    print(f"hi{content}")
else:
    print("空字符串")
print(bool(content))
content1 = ""
if content:
    print(f"hi{content1}")
else:
    print("空字符串")
print(bool(content1))

lst = [1, 2]
if lst:
    print(f"lst:{lst}")
else:
    print("空列表")
print(bool(lst))

lst1 = []
if lst1:
    print(f"lst:{lst1}")
else:
    print("空列表")
print(bool(lst1))
