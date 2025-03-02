#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :05.format_output.py
# @Time      :2024/03/16 14:20:51
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 格式化输出案例
# 定义变量
age = 24
score = 77.5
gender = "男"
name = "Baikal"
# %操作符输出(必须要类型匹配)
"""
%s代表输出字符串
%d代表输出整数
%f代表输出浮点数 %.2f代表保留两位小数
%% 输出%
数值和%类型必须一一匹配
"""
print("个人信息: %s %d %s %.2f" % (name, age, gender, score))

# format()函数
"""
使用花括号进行占位,花括号数量和.format函数的值必须对应,如果format函数值少于花括号会报错,多了则忽略
"""
print("个人信息: {} {} {}".format(name, age, gender))

# f-string(推荐使用)变量必须先定义后使用,变量一定要一一对应
print(f"个人信息:{name} {age} {score} {gender}")
