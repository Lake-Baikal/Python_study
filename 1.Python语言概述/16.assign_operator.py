#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :16.assign_operator.py
# @Time      :2024/03/21 23:15:04
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# 赋值运算符
"""
!1.运算顺序从右往左 num = a+b+c
!2.赋值运算符的左边是变量，右边可以是变量、表达式、字面量
"""
num1 = 10
i = 100
i += 100
print("i=", i)  # 等价于 i=i+100
i -= 100
print("i=", i)  # 等价于 i=i-100
i *= 3
print("i=", i)  # 等价于 i=i*3
i /= 5
print("i=", i)
i %= 2
print("i=", i)
i //= 2
print("i=", i)
i **= 2
print("i=", i)
"""
有两个变量a,b,要求将其进行交换，最终打印结果
1.先定义一个中间变量temp
2.temp=a 把a的值存到temp
3.a=b 把b的值赋给a
4.b=temp 把temp(即a)的值赋值给b
"""
a = 30
b = 40
# print(f"交换前 a={a},b={b}")
# temp = a
# a = b
# b = temp
# print(f"交换后 a={a},b={b}")

# 在Python中支持一个简单的方式实现变量交换 x,y=y,x 把y的值赋给x,把x的值赋给y

print(f"交换前 a={a},b={b}")
a, b = b, a
print(f"交换后 a={a},b={b}")

# 有两个变量a,b，要求将其进行交换,不使用前面两种方法
""" 
1.a,b记录值
2.a=1,b=2
a=a+b
b=a-b
a=a-b

"""
a = 1
b = 2
print(f"交换前 a={a},b={b}")
a = a + b
b = a - b
a = a - b
print(f"交换后 a={a},b={b}")
