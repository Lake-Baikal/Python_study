#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :7.元组常用操作.py
# @Time      :2024/05/01 00:49:34
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# 元组常用操作
tuple_a = (100, 200, 300, 400, 600, 200)
print("tuple_a元组元素个数:", len(tuple_a))
print("tuple_a元组最大元素:", max(tuple_a))
print("tuple_a元组最小元素:", min(tuple_a))

# tuple.count(obj):统计某个元素在元组中出现的次数
print("100出现的次数是", tuple_a.count(100))
print("200出现的次数是", tuple_a.count(200))

# tuple.index(obj):从列表中找出某个值第一个匹配项的索引位置
# 如果找不到,会报错: ValueError:x is not in tuple
print("200第1次出现在元组的索引是:", tuple_a.index(200))
# !方法2
# 如果 s 中的某项等于 x 则结果为 True,否则为 False
print(300 in tuple_a)
print(3000 in tuple_a)

# 案例:定义一个元组,("大话西游","周星驰",80,["周星驰","小甜甜"])
# 信息为(片名,导演,票价,演员列表)
# 1.查询票价对应的索引
# 2.遍历所有演员
# 3.删除小甜甜,增加演员"牛魔王","猪八戒"

tuple_movie = ("大话西游", "周星驰", 80, ["周星驰", "小甜甜"])
# 1.查询票价对应的索引
print("票价对应的索引是:", tuple_movie.index(80))
# 2.遍历所有演员
for element in tuple_movie[3]:
    print(f"演员的名字是{element}")

# 3.删除小甜甜,增加演员"牛魔王","猪八戒"
del tuple_movie[3][1]
print(f"删除后的结果{tuple_movie}")
tuple_movie[3].append("牛魔王")
tuple_movie[3].append("猪八戒")
print(f"增加后的结果{tuple_movie}")
