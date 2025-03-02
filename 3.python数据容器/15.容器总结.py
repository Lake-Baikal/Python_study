#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :15.容器总结.py
# @Time      :2024/05/22 21:23:36
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# 数据容器通用转换
str_a = "hello"
list_a = ['jack', 'tom', 'mary']
tuple_a = ('baikal', 'tim')
set_a = {'red', 'black'}
dict_a = {'0001': '小倩', '0002': '宁采臣'}

# ! 1. list([iterable])
# iterable可以是序列,支持迭代的容器或其他可迭代对象
# 也就是将指定容器转换为列表
print(f"str_a转换成list,{list(str_a)}")
print(f"tuple_a转换成list,{list(tuple_a)}")
print(f"set_a转换成list,{list(set_a)}")
print(f"dict_a转换成list,{list(dict_a)}")

# ! 2. str(容器):将指定容器转换为字符串
print(f"list_a转换为str:{str(list_a)} 类型:{type(str(list_a))}"
      )  # "['jack', 'tom', 'mary']"
print(f"tuple_a转换为str:{str(tuple_a)} 类型:{type(str(tuple_a))}")
print(f"set_a转换为str:{str(set_a)} 类型:{type(str(set_a))}")
print(f"dict_a转换为str:{str(dict_a)} 类型:{type(str(dict_a))}")

# ! 3. tuple([iterable])
# iterable可以是序列,支持迭代的容器或其他可迭代对象
# 也就是将指定容器转换为元组

print(f"str_a转换成tuple,{tuple(str_a)}")
print(f"list_a,{tuple(tuple_a)}")
print(f"set_a转换成list,{tuple(set_a)}")
print(f"dict_a转换成list,{tuple(dict_a)}")

# ! 4.set([iterable])
# iterable可以是序列,支持迭代的容器或其他可迭代对象
# 也就是将指定容器转换为集合

print(f"str_a,{set(str_a)}")
print(f"list_a,{set(list_a)}")
print(f"tuple_a转换成set,{set(tuple_a)}")
print(f"dict_a转换成set,{set(dict_a)}")
