#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :29.while循环.py
# @Time      :2024/03/31 23:41:01
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
while 循环是用于在表达式为真的情况下,重复的(循环的)执行,是通过while语句实现的
!基本语法
while 判断条件(condition)
  循环操作语句(statements)
1.while是关键字,是规定好的
2.当判断条件为True时,就执行循环操作语句,如果为False就退出while
3.循环操作语句,可以有多条语句,也就是我们要执行的代码,循环体
"""
# 使用while循环输出10条hello world
"""
分析:
1.定义变量 i=1
2.使用while循环判断i<=10,然后为真就执行hello world
3.注意i的值,要不断增加i+=1,如果不增加就会导致无限循环
"""
# i = 1  # 循环遍历初始化
# while i <= 10:
#     print("hello world", i)
#     i += 1
"""
while循环可以和else配合使用
语法:
while 判断条件(condition):
循环操作语句(statements)
else:
其他语句<additional_statements(s)>
!在while...else判断条件为false时,会执行else的语句块,即在遍历过程中,没有被打断(比如没有执行到break语句)执行到break语句不会执行else语句
"""
# i = 0
# while i < 3:
#     print("python语言,简单易学", i)
#     i += 1
#     if i == 1:
#         break
# else:
#     print("i<3不成立,i=", i)

# 案例1:打印1~100之间所有能被3整除的数
"""
思路分析
1.定义一个变量i=1 max_num=100表示我们要遍历的范围
2.如果i % 3==0说明当前i可以被3整除
3.满足条件输出即可,注意遍历时i+=1

"""
# i = 1
# max_num = 100
# while i <= max_num:
#     # 如果i%3==0成立,说明i可以被3整除
#     if i % 3 == 0:
#         print(i)
#     i += 1

# 案例2:打印40~200之间所有的偶数
"""
思路分析
1.定义一个变量i=40 max_num=200表示我们要遍历的范围
2.如果i % 2==0说明当前i可以被2整除
3.满足条件输出即可,注意遍历时i+=1
"""
i = 40
max_num = 200
while i <= max_num:
    if i % 2 == 0:
        print(i)
    i += 1

# 案例3:不断输入姓名,直到输入exit为止
""" 思路分析
1.定义一个变量name,接收用户输入
2.使用while判断,如果name !="exit"就循环的输入即可
"""
# name = input("请输入名字:")
# while name != "exit":
#     name = input("请输入名字:")
#     print("输入的内容是:", name)

# 案例4: 打印1~100之间所有9的倍数的整数,统计个数及总和
"""
思路分析
1.定义一个变量i=1 max_num=100表示我们要遍历的范围
2.如果i % 9==0则说明i是9的倍数
3.定义count来统计个数 count+=1
4.定义sum来累加和 sum+=1

"""
# i = 1
# max_num = 100
# count = 0
# sum = 0
# while i <= max_num:
#     if i % 9 == 0:
#         print(i)
#         count += 1
#         sum += i
#     i += 1
# print(f"count={count},sum={sum}")

# 案例5:输入一个整数输出如下表达式
# 0 + 6 = 6
# 1 + 5 = 6
# 2 + 4 = 6
# 3 + 3 = 6
# 4 + 2 = 6
# 5 + 1 = 6
# 6 + 0 = 6
"""
1.定义一个变量num,接收用户输入的整数,定义一个i=0,循环的起始值
2.遍历0-num,第一个加数0-num,第二个加数num-0
使用while循环
"""
num = int(input("请输入一个整数:"))
i = 0
# 遍历0~num
while i <= num:
    print(f"{i}+{num-i}={num}")
    i += 1
