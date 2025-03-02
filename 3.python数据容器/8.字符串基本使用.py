#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :8.字符串基本使用.py
# @Time      :2024/05/02 00:08:25
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# !在python中处理文本数据是使用str对象,也称为字符串,字符串是由unicode编码构成的不可变序列
# unicode码是一种字符编码,能够表示数量为65536个字符
# unicode码是国际组织制定的可以容纳世界上所有文字和符号的字符编码方案
# ord()返回单个字符对应的unicode编码值

print(ord("苏"))
print(ord("a"))
# !字符串是字符的容器,一个字符串可以存放多个字符,比如"hi-baikal"
str_a = "red-green"
print("str_a的第三个值/字符是", str_a[2], "类型是", type(str_a[2]))
# 要取出str_a字符串的第三个值/元素"d",则通过str_a[2]就可以访问到,注意索引从0开始,取出的单个字符类型仍然是字符串

# !字符串遍历:就是将字符串里面的每个元素依次取出，进行处理的操作,就是遍历/迭代
str_b = "hi_baikal"
# !使用while循环
# 表示从第一个元素进行遍历
index = 0
while index < len(str_b):
    print(f"第{(index+1)}个元素是->{str_b[index]}")
    # 循环控制遍历增加1
    index += 1
    # 分隔符快捷写法
    # !使用for循环
print("-" * 100)

for element in str_b:
    print(element)

# 上面的分割符可以这样写
print("=", * 30)
# !字符串的注意事项和使用细节
# ! 1.字符串索引必须在指定的范围内使用,否则会报IndexError:string index out of range,
# ! 2.索引也可以从尾部开始最后一位元素的索引为-1,往前一位位-2,以此类推
# !3.字符串是不可变序列,不能修改
str_d = "hi_world"
# 通过索引可以访问指定元素
print(str_d[3])
print(id(str_d))
# 不能修改元素
# str_d[3] = "S"
# print(str_d[3])
# 'str' object does not support item assignment
str_d = "abc"
print(id(str_d))

# !在python中,字符串长度没有固定的限制,取决于计算机内存的大小
