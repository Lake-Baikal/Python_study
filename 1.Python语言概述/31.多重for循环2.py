#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :31.多重for循环2.py
# @Time      :2024/04/04 14:06:17
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 案例:统计3个班成绩情况,每个班5名同学,要求完成
# 1.求出各个班的平均分和所有班级的平均分,学生成绩从键盘输入
# 2.统计三个班及格人数
# 重要编程思想,化简为繁,先死后活
# 1.先统计一个班的成绩情况,求出一个班的平均分
# 2.统计三个班的成绩情况,求出各个班的平均分,所有班级的平均分和及格人数
# # !定义相关变量
# # !定义班级个数
# class_num = 3
# # !定义学生个数
# student_num = 5
# # !统计所有班级的总分
# total = 0.0
# # !统计所有的及格人数
# pass_num = 0
# # !循环的处理三个班级成绩
# for i in range(1, class_num + 1):
#     # 统计一个班的成绩情况,求出一个班的平均分数for循环5次,接收学员成绩
#     # !统计每个班的总分之前sum清零
#     sum = 0.0
#     for j in range(1, student_num + 1):
#         score = float(input(f"请输入第{i}个班级第{j}学生成绩"))
#         # !判断是否及格累加到pass_num
#         if score >= 60.0:
#             pass_num += 1
#         # 累加到sum
#         sum += score
#     print(f'第{i}班级平均分:平均分{sum / 5}')

#     # 将sum累加到total
#     total += sum
# # 输出所有班级的平均分和及格人数
# print(f"所有班级的平均分{total / (student_num * class_num)}及格人数:{pass_num}")

# 作业打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}*{i}={i*j}\t", end="")
#     print(" ")

line = 9
i = 1
while i <= line:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t", end="")
        j += 1
    i += 1
    print(" ")
