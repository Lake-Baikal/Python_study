#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :9.字符串的常用操作.py
# @Time      :2024/05/02 13:07:36
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

str_names = "jack tom mary baikal nono tom"
# !1. len(str)字符串长度,也就是包含多少个字符
print(f"{str_names}有{len(str_names)}个字符")
#  !2. str.replace(old,new[,count]):返回字符串的副本, 其中出现的所有子字符串old都将替换为new
#  !如果给出了可选参数count,则只替换前count次出现,如果没有给出count,默认全部替换
#  !返回字符串的副本,表示原来的字符串不变,而是返回一个新的字符串
# 将"jack"替换成"杰克",只替换一个
# 如果count什么都不写默认全部替换
str_names_new = str_names.replace("jack", "杰克")
print("str_names_new:", str_names_new, id(str_names_new))
print("str_names:", str_names, id(str_names))

# !3. str.split(sep=None,maxsplit=-1)
# !返回一个由字符串内单词组成的列表,使用sep作为分隔字符串,
# !如果给出了maxsplit,则最多进行maxsplit次拆分,因此列表最多会有maxsplit+1个元素。
# !如果maxsplit未指定为-1,则不限拆分次数(进行所有有可能的拆分)
# 对str_name按照""进行分割
str_names_split = str_names.split(" ")
print(f"str_name_split 内容是{str_names_split}类型是{type(str_names_split)}")
print(f"str_names内容是:{str_names}")
# !str.count(sub):统计指定字符串中出现的次数
# 统计tom在字符串中出现的次数
print("tom在字符串中出现的次数", str_names.count("tom"))
# ! 4.str.index(sub):从字符串中找出指定字符串第一个匹配项的索引位置
print(f"tom出现的索引是:{str_names.index('tom')}")

# ! 5.str.strip([chars]):返回原字符串的副本,移除其中的前导和末尾字符,chars为指定要移除字符的字符串
# !这个方法通常可以用于除去前后空格,或者去除指定的某些字符
print("  jack  ".strip(" "))
print("123tom321".strip("123"))
print("123t123om321".strip("123"))

str_names_strip = str_names.strip(" ")
print("str_names_strip:", str_names_strip)

# ! 6.str.lower():返回原字符串小写副本,不影响原来字符
# 将字符串字母全部改成小写
str_names = "BaiKal"
str_names_lower = str_names.lower()
print("str_names_lower:", str_names_lower)
print("str_names:", str_names)
# ! 7.str.upper():返回字符串大写的副本,不影响原来字符
str_names_upper = str_names.upper()
print("str_names_upper:", str_names_upper)
print("str_names:", str_names)

# ! 字符串比较
"""
!1.运算符:>,>=,<,<=,!=,==
!2.比较规则:首先比较两个字符串中的第一个字符,如果相等则继续比较下一个字符,依次比较下去,直到两个字符串中的字符不相等时,其比较结果就是两个字符串的比较结果,两个字符串中的所有后续字符将不再被比较
!3.比较原理:两个字符进行比较时,比较的是其ordinal value(原始值/码值)调用内置函数ord可以得到指定字符ordinal value
!4.与内置函数ord对应的是内置函数chr,调用内置函数chr时指定ordinal value 可以得到其对应的字符
"""
print(ord("1"))
print(ord("2"))
print(ord("a"))
print(ord("b"))
print(ord("苏"))
print(chr(49))
print(chr(50))
print(chr(33487))
# 比较示例
print("tom" > "baikal")
print("tom" > "ba")  # tom还有剩余的码值,ba没有了所以tom大
print("tom" > "tomcat")  # tom码值,tomcat还有剩余的码值所以tomcat大
print("tom" < "苏")
print("tom" <= "tom")

# 案例:定义一个字符串,str_names="tom jack mary nono smith baikal"
# 1.统计一共多少个人名
# 使用split方法进行分割" "
# 然后统计有多少个人名即可
# 2.如果有"baikal"替换为"贝加尔"
# 3.如果人们是英文,则把首字母替换为大写

str_names = "tom jack mary nono smith baikal"
str_names_list = str_names.split(" ")
print(f"一共有{len(str_names_list)}人名")

str_names_replace = str_names.replace("baikal", "贝加尔")
print(str_names_replace)

# "tom jack mary nono smith baikal " ->"Tom Jack Mary Nono Smith Baikal "
# 1.定义字符串 str_names_upper来保存新的结果
# 2.遍历str_name_list列表,如果发现是引文名,则将首字母改为大写str.capitalize
# 3.拼接到str_names_upper
str_names_upper = ""
for element in str_names_list:
    if element.isalpha():
        str_names_upper += element.capitalize() + " "
# 去掉两边的" "
str_names_upper = str_names_upper.strip(" ")
print("结果是:", str_names_upper)
