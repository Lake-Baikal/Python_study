#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :28.for循环.py
# @Time      :2024/03/31 12:27:32
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!for循环就是可以让你的代码循环的执行,是通过for语句来实现
基本语法:
for <变量> in <范围/序列>:
  <循环操作语句>
1.for、in是关键字,是规定好的
2.<范围/序列>可以理解为要处理的数据集,需要是可迭代的对象(比如字符串、列表等)
3.循环操作语句,这里可以有多条语句,也就是我们要循环这些的代码,也就是循环体
4.python的for循环是一种轮询机制,是对指定的数据集进行轮询处理
"""
# 定义一个列表,可以视为一个数据集
# 每次循环的时候,依次将nums中的值取出赋值给i
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums, type(nums))
# for i in nums:
#     print("hello,world", i)

# !这样写不灵活
# for i in [1, 2, 3, 4]:
#     print("hello,world", i)

# !循环时会依次把序列中的值取出来赋给变量i
# !如需要遍历数字序列,可以使用内置的range()函数,他会生成数列,range()函数生成的数列是前闭后开

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums, id(nums), nums[0], id(nums[0]))
print(nums, id(nums), nums[1], id(nums[1]))
print(nums, id(nums), nums[2], id(nums[2]))
print(id(1))
nums2 = [1, 2]
print(nums2, id(nums2), nums2[0], id(nums2[0]))
# range函数的解读
# class range(stop)
# class range(start,stop,step=1)
# 1.虽然被称为函数,但range实际上是一个不可变的序列类型
# 2.range ()默认增加的步长step是1,也可以指定,1就是每次生成的数逐次加1
# 3.start默认为0
# 4.通过list()可以查看range()生成的序列包含的数据
# 5.range()函数生成的序列是前闭后开 range(1,5)  输出1,2,3,4 包含1不包含5
# 1.需求:生成一个[1,2,3,4,5]
# r1 = range(1, 6, 1)
# 简写
# r1 = range(1, 6)
# print("r1=", list(r1))

# # 2.生成一个[0,1,2,3,4,5]
# # r2 = range(0, 6, 1)
# # print("r2=", list(r2))
# # 简写:因为start默认为0,step默认为1
# r2 = range(6)
# print("r2=", list(r2))
# # 3.需求:生成一个[1,3,5,7,9]
# r3 = range(1, 10, 2)
# print("r3=", list(r3))

# # 4.需求:使用for+range方式输出10句"hello world"
# for i in range(10):
#     print("hello world")

# for循环可以和else配合使用
# !什么情况下会进入else,就是在for循环正常的完成遍历,在遍历过程中,没有被打断(比如没有执行到break语句)
# 语法:
"""
for <variable> in <sequence>
<statements>
else:
<statements>
"""
nums2 = [1, 2, 3]
for i in nums2:
    print("hello world")
    if i == 2:
        break  # 提前结束for循环
else:
    print("没有循环数据了")

# 练习
languages = ['python', 'c++', 'c']
for i in languages:
    print(i)
