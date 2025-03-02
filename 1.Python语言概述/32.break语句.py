#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :32.break语句.py
# @Time      :2024/04/04 21:03:13
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
!随机生成1-100的一个数,直到生成97这个数,看看一共用了几次
!使用循环, 但是不知道循环次数(无限循环)
!当判断条件满足时使用break语句可以提前终止循环
!break语句是用在for或while循环所嵌套的代码
"""
# random.randint(a, b)的使用,用来生成随机数
# 导入random模块
import random
"""
思路分析
1.定义一个变量count统计一共用了多少次
2.使用while true 无限循环生成随机数,判断直到生成97就退出
3.输出count即可
"""
# 导入random模块
# 统计一共用了多少次
count = 0
while True:
    n = random.randint(1, 100)
    # 统计次数
    count += 1
    if n == 97:
        break
print(f"生成97一个用了{count}次")
# !break语句是用在for循环和while循环所嵌套的代码
# !他会终结最近的外层循环,如果循环有可选的else子句,也会跳过该子句
count = 0
while True:
    print("hi while")
    count += 1
    if count == 3:
        break
    while True:
        print("OK while")
        break
else:
    print("hello while")
# !如果一个for循环被break所终结,该循环的控制变量会保持其当前值
nums = [1, 2, 3, 4, 5, 6]
for i in nums:
    if i > 3:
        break

print("i=", i)

# 案例1-100以内求和,求出当和第一次大于20的当前控制循环的变量值是多少
"""
思路分析
1.定义sum变量求和
2.for遍历1-100当sum>20时,就退出for-break
3.输出当前控制循环的变量即可
"""
sum = 0
for i in range(1, 101):
    sum += i
    if sum > 20:
        break
print("i=", i)

# 2.实现登录验证,有三次机会,如果用户名为"baikal",密码"888"提示登录成功,否则提示还有几次机会，使用for-break完成
"""
!思路分析
1.实现登录验证,有三次机会使用for循环3次
2.接收用户的输入(两个变量userName,userName)如果满足条件就break
3.根据登录情况,提示成功/还有几次机会
"""
# for i in range(1, 4):
#     userName = input("请输入用户名")
#     passWord = input("请输入密码")
#     if userName == "baikal" and passWord == "888":
#         print("登录成功")
#         break

#     else:
#         print(f"还有{3-i}次机会")
change = 3
for i in range(1, 4):
    userName = input("请输入用户名")
    passWord = input("请输入密码")
    change -= 1
    if userName == "baikal" and passWord == "888":
        print("登录成功")
        break

    else:
        print(f"还有{change}次机会")
