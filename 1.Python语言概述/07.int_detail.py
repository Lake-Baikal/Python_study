#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :07.int_detail.py
# @Time      :2024/03/16 22:02:20
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
import sys

"""
!基本数据类型
类型             描述
整型int          整形:比如 1,-1,200等
浮点数float      小数:比如1.1,-4.5,900.9等
布尔值bool       布尔值就是我们常说的逻辑,可以理解为对(True)或错(False)
字符串String     字符串就是字符组成的一串内容, Python中用成对的单引号或双引号括起来,比如"hello world"
!python中的变量在使用前都必须赋值,变量赋值以后该变量才会被创建
!我们所说的类型是变量所指的内存数据的类型
"""
a = 100
b = "Hello"

"""
1.a和b是变量,他是没有类型的
2.a,b变量指向代表的数据"hello"和100是有类型的
3."hello"和100在有些地方也成为字面量
"""

# ! 通过type()函数来查看数据的类型
# !语法: type(Object) object就是你要查看类型的数据,可以是一个具体的数据,即(字面量)也可以是变量(也就是数据的类型)
# 演示type()函数的使用
age = 24
score = 77.5
gender = "男"
name = "Baikal"
is_pass = True
# 查看变量的类型，本质上是查看变量指向的数据类型
print(type(name))
print(type(score))
print(type(gender))
print(type(age))
print(type(is_pass))

# type()可以直接查看具体的(字面量)的类型
print(f"hello的类型是{type("hello")}")
print(f"1.1的类型是{type(1.1)}")
print(f"30的类型是{type(30)}")
print(f"True的类型是{type(True)}")


# python整型就是用来存放整数值的，比如12，30，3456，-1等等

# 详解int类型的细节
# 在python,int可以表示很大的数
# the limit (4300 digits)
# n3 = 9**888
# print("n3=", n3, type(n3))


"""
# python的整数有十进制,十六进制,八进制,二进制表示
!十进制就是我们最常见的写法,比如1,66,123等
!十六进制写法:加前缀0x, 由0~9和A~F的数字和字母组合
!八进制的写法:加前缀0o,由0~7数字组合
!二进制写法:加前缀0b,只有0和1数字组合
运行时会自动转换为十进制

"""

print(10)
# 十六进制
print(0x10)  # 16
# 八进制
print(0o10)  # 8
# 二进制
print(0b10)  # 2

# python中整型占多少字节
# 字节(byte):计算机中最基本的存储单元
# 位(bit):计算机中最小存储单位
# !在编程中,存储数据的基本单位是字节
# 1byte=8bit
# ! 字节数随着数字的增大而增大,即Python整型是变长的
# !每次的增量是4个字节
n1 = 0
n2 = 1
n3 = 2
n4 = 2**15
n5 = 2**30
n6 = 2**128
# 在python中,可以通过sys.getsizeof返回对象(数据)大小(按照字节单位返回)
print(n1, sys.getsizeof((n1)), "类型", type(n1))
print(n2, sys.getsizeof((n2)), "类型", type(n2))
print(n3, sys.getsizeof((n3)), "类型", type(n3))
print(n4, sys.getsizeof((n4)), "类型", type(n4))
print(n5, sys.getsizeof((n5)), "类型", type(n5))
print(n6, sys.getsizeof((n6)), "类型", type(n6))
