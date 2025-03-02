#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :18. 标识符的命名规则.py
# @Time      :2024/03/22 22:40:30
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# !Python对各种变量，函数和类等命名时使用的字符序列称为标识符
# 凡是自己可以起名字的地方都可以叫做标识符
"""
?标识符的命名规则(必须遵守)
1.由24个英文字母大小写,0~9,_组成
2.数字不可以开头
3.不可以使用关键字，但是能包含关键字
4.Python区分大小写
5.标识符不能包含空格
"""
# 1.由24个英文字母大小写,0~9,_组成
num9_N = 100
# num9~N=100 错误，~不是规定的符号
# 2.数字不可以开头
# 1num=300
# 3.不可以使用关键字，但是能使用关键字
# if = 200 错误，if是关键字
my_if = 200
# 4.Python使用大小写
n = 700
N = 800
print("n=", n, "N=", N)
# 5.标识符不能包含空格
# my name="Baikal"

# hello = 1 # ok
# hello12 = 2 # ok
# # 1hello=2 # no
# h - b = 3 # no
# x h=4  # no
# h$4=1  # no
# class=1 # no
# int=1 # ok
# or=2 # no
# and=3 # no
# if=1 # no
# _if=0 # ok
# syu_name=1 # yes

# 标识符命名规范
# 变量名:变量要小写,若有多个单词,使用下划线分开,常量全部大写
num = 1
my_friend_age = 10
PI = 3.1415926


# 函数名:函数名一律小写,若有多个单词,使用下划线分开,另外,私有函数以双下划线开头
def my_func(var1, var2):
    pass


def __private__func(var1, var2):
    pass


# 类名:使用大驼峰命名
"""
驼峰命名有两种,一种是大驼峰命名,一种是小驼峰命名
大驼峰命名,多个单词的首字母用大写开头,比如,MyName
小驼峰命名,第一个单词首字母小写,后面单词的首字母用大写开头,比如,myName
"""


class Foo:
    pass


# python关键字
# 定义:被Python语言赋予了特殊含义,用作专门用途的字符串(单词)
""" 
False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""
