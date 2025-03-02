#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :4.列表的常用操作.py
# @Time      :2024/04/26 20:56:16
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
# !1.列表的常用操作
list_a = [100, 200, 300, 400, 600]
print("list_a列表元素个数:", len(list_a))
print("list_a列表元素最大值:", max(list_a))
print("list_a列表元素最小值:", min(list_a))

# !在列表末尾添加新的对象 list.append(obj)
list_a.append(900)
list_a.append(100)
print("list_a", list_a)

# !list.count(obj):统计某个元素在列表中出现的次数

print("100出现的次数", list_a.count(100))

# ! list.extend(seq):在列表末尾一次性追加另一个序列中的多个值,(用新列表扩展原来的列表)

list_b = [1, 2, 3]
# 将list_b追加到list_a
list_a.extend(list_b)
print("list_a", list_a)

# !list_index(obj):从列表中找出某个值第一个匹配项的索引位置
# 如果找不到,就会报错:ValueError
print("300第一次出现在序列的索引是:", list_a.index(300))
# print("3000第一次出现在序列的索引是:", list_a.index(3000))

# !就地将列表中的元素逆序 s.reverse()
list_a.reverse()
print("list_a", list_a)  # [3, 2, 1, 100, 900, 600, 400, 300, 200, 100]

# ! list.insert(index,obj):将对象插入列表指定index位置
# 将666插入到index为1的位置
list_a.insert(1, 666)
print("list_a:", list_a)  # [3, 666, 2, 1, 100, 900, 600, 400, 300, 200, 100]

# ?列表生成式,就是生成列表的公式
# ! 基本语法[列表元素的表达式 for 自定义变量 in 可迭代对象]
list1 = [ele * 2 for ele in range(1, 5)]
print(list1)

list2 = [ele + ele for ele in "baikal"]
print(list2)

# 案例 要求生成一个列表,内容为[1,4,9,16,25,36,49,64,81,100]
# [1*1,2*2,3*3,4*4]
list3 = [ele * ele for ele in range(1, 11)]
print(list3)

# 循环从键盘输入5个成绩,保存到列表,并输出
"""
1.定义一个空列表保存成绩scores=[]
2.循环操作5次,接收用户的输入,每接受一个数据就添加到空列表scores
3.输出成绩即可
"""
scores = []
for i in range(5):
    score = float(input("请输入成绩"))
    scores.append(score)

print("成绩情况是:", scores)

# !如果只是想完成循环,不需要该变量,可以把 i 修改为下划线_语法也可以通过
scores = []
for _ in range(1, 6):
    score = float(input("请输入成绩"))
    scores.append(score)
print("成绩情况", scores)
