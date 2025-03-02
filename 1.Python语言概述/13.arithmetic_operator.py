#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :13.arithmetic_operator.py
# @Time      :2024/03/20 22:33:24
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 算数运算符是对数值类型的变量进行运算的,在程序中使用的非常多
# 算数运算符
print(10 - 2)
print(10 + 2)
print(10 * 2)
print(10 / 3)  # 对于除号运算，返回的结果是小数
print(10 / 2)  # 对于除号运算，返回的结果是小数
# 对于整除//，返回商的整数部分(并且向下取整)
print(10 // 3)
print(-9 // 2)
print(-10 // 3)
# 取模% 对应的运算公式是: a % b = a - a // b * b
print(10 % 3)
print(-10 % 3)
# 分析 -10 % 3 = -10 - (-10) // 3 * 3 =-10 - (-4) *3 = -10 + 12 =2
print(10 % -3)
# 分析 10 % -3 = 10 - 10 // -3 * -3 = (-4) * (-3) =10 - 12 = -2
print(-10 % -3)
# -10 - (-10) // -3 * (-3) = -10 - (-9) = -1
# ** 幂运算
print(2**5)
print(9**2)

# 假入还有97天放假,问合xx个星期零xx天
"""
1.定义变量
days:记录总的天数
week:记录对应的星期
left_day:记录剩余天数
2.week:记录对应的星期 days // 7
  left_day:记录剩余天数 days % 7
3.输出  
"""
days = 97
week = days // 7
left_days = days % 7
print(f"假入还有{days}天放假,则合{week}个星期零{left_days}天")
# 定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为：5 / 9 *(华氏温度-100)，求出华氏温度对应的摄氏温度。[234.5]
""" 
1.定义变量 hua_shi she_shi
2.套用公式
3.输出结果
"""
hua_shi = 234.5
she_shi = 5 / 9 * (hua_shi - 100)
print("华氏温度%.2f对应的摄氏温度%.2f" % (hua_shi, she_shi))
