#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :12.数据类型转换.py
# @Time      :2024/03/17 22:18:55
# @Author    :Baikal
# @Motto     :我亦无他，唯手熟尔

# n1 = 100
# result = "n1 的值是" + n1
# print(result)
# !Python 变量的类型不是固定的，会根据变量当前值在运行时决定的，可以通过内置函数 type(变量) 来查看类型，这种方式就是隐式转换 (自动转换)

# ?Python 根据该变量使用的上下文 (即当前值) 在运行时决定的类型
var1 = 10
print(type(var1))
var1 = 1.1
print(type(var1))
var1 = "hello word"
print(type(var1))

# ! 在运算时，数据类型会向高精度转换，float 的精度高于 int
var2 = 10
var3 = 1.2
var4 = var2 + var3
print("var4=", var4, "var4 的类型是：", type(var4))
var2 = var2 + 0.1
print("var2=", var2, "var2 的类型是：", type(var2))
"""
! 显示转换
! 如果需要对变量的数据类型进行转换，只需要将数据类型作为函数名即可，这种方式就是显示转换/强制转换
! 以下几个内置函数可以完成数据类型之间的转换。函数会返回一个新的对象/值，就是强制转换后的结果
"""
i = 10
j = float(i)
print("j 的类型是：", type(j), "j=", j)  # 10.0

k = str(i)
print("k 的类型是：", type(k), "k=", k)  # "10"
# print(k + 90)  # 此时 k 是字符串，字符串与整数相加一定会报错

# ! 显示转换的注意事项
# !.不管什么值的 int,float 都可以转成 str,str(x) 将对象 x 转换为字符串
n1 = 100
n2 = 123.6
print(str(n1))
print(str(n2))
"""
!int 转成 float 时，会增加小数部分，比如 123->123.0
!float 转成 int 时，会去掉小数部分，比如 123.65->123
"""
print(float(n1))  # 123.0
print(int(n2))  # 123

# !str 转换为 int,float,使用 int(x),float(x) 将对象转换为 int / float
# ! 在将 str 类型转换成基本数据类型时，要确保 str 的值能够转换为有效的数据比如我们可以将"123",转换成一个整数,而12.3则不能
# ! 但是不能将"hello",转换成整数和浮点数，会报 valueError, 程序终止

n3 = "12.3"
print(float(n3))
# print(int(n3))  # "123"可以转换
# n4 = "hello"
# print(int(n4))
# print(float(n4))

# ! 对一个变量进行强制转换，会返回一个数据/值，注意，强制转换后，并不会影响原变量的数据类型 (即：不会影响原变量指向的数据/值的数据类型)。
i = 10
j = float(i)
print("i 的值：", i, "i 的类型：", type(i))
print("j 的值：", j, "j 的类型：", type(j))

k = str(i)
print("i 的值：", i, "i 的类型：", type(i))
print("k 的值：", k, "k 的类型：", type(k))

# homework
i = 10
j = float(i)  # 10.0
print(type(i))  # int
print(type(j))  # float

i = j + 1
print(type(i))  # float  11.0
print(type(j))  # float

print(i)  # float
print(int(i))  # 11
print(type(i))  # float

# homework
n1 = 13
n2 = 17
n3 = n1 + n2
print("n3=", n3)
n4 = 38
n5 = n4 - n3
print("n5=", n5)
str1 = "\n \t \r \\ 1 2 3"
print(str1)

bookName1 = "骆驼祥子"
bookName2 = "西游记"
print(bookName1 + "\t" + bookName2)
bookPrice1 = 98.6
bookPrice2 = 100
print(bookPrice1 + bookPrice2)

# 定义需要的变量

name = "Baikal"
age = 20
score = 90.2
gender = "男"
hobby = "打篮球"
# 按照规定格式输出信息
print("姓名\t年龄\t成绩\t性别\t爱好\n" + name + "\t" + str(age) + "\t" + str(score) +
      "\t" + gender + "\t" + hobby)
