#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :4.函数的传参机制.py
# @Time      :2024/04/11 22:33:23
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔


# !字符串和数值类型的传参机制
def f1(a):
    print(f"f1() a的值:{a} 地址是:{id(a)}")
    a += 1
    print(f"f1() a的值:{a} 地址是:{id(a)}")


# 定义变量a=10
a = 10
print(f"调用f1()前 a的值:{a} 地址是:{id(a)}")
# 调用f1(a)
f1(a)
print(f"调用f1()后 a的值:{a} 地址是:{id(a)}")


# !字符串传参机制
def f2(name):
    print(f"f2() name的值: {name}的地址是:{id(name)}")
    name += " hi"
    print(f"f2() name的值: {name} 地址是:{id(name)}")


print("-----------------------------")

name = 'tom'
print(f"调用f2()前 name的值:{name} 地址是:{id(name)}")
f2(name)
print(f"调用f2()后 name的值:{name} 地址是:{id(name)}")

# !字符串和数值类型是不可变数据类型,当对应的变量的值发生变化时,它对应的内存地址会发生改变
