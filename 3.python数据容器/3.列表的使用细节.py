#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3.列表的使用细节.py
# @Time      :2024/04/22 21:42:22
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# ! 1.如果我们需要一个空列表,可以通过[],或者list()方式来定义。
list1 = []
list2 = list()
print(list1, type(list1))
print(list2, type(list2))

# ! 2.列表的元素可以有多个,而且数据类型没有限制,允许有重复元素,并且是有序的
list3 = [100, "jake", 4.5, True, 'jake']
print(list3)
# !嵌套列表
list4 = [100, 'tom', ["天龙八部", '笑傲江湖', 300]]
print("list4=", list4)

# ! 3.列表的索引/下标从0开始
# ! 4.列表索引必须在指定的范围内使用,否则报:IndexError:list index out of range
# 比如list1=[1,2.1,"baikal"]有效下标为0~2

list5 = [1, 2.1, "baikal"]
# ! 索引越界
# print(list5[3])  # IndexError:list index out of range

# ! 5.反向索引,索引也可以从尾部开始,最后一个元素的索引为-1,往前一位为-2,以此类推
list6 = [
    100,
    "jake",
    4.5,
    True,
]
print(list6[-1])
print(list6[-2])
# !即使是反向索引也依旧不能越界
# print(list6[-5])

# ! 6.通过列表[索引]=新值 对数据进行更新,使用列表.append(值)方法来添加元素,使用del语句来删除列表的元素,注意不能超出有效索引范围

list_a = ["天龙八部", "笑傲江湖"]
print("list_a", list_a)
list_a[0] = "雪山飞狐"
print("list_a", list_a)
list_a.append("倚天屠龙记")
print("list_a", list_a)
del list_a[1]
print("list_a", list_a)

# ! 7.列表是可变序列,要注意其使用特点
# !列表的元素是可修改的,修改后列表变量指向地址不变,只是数据内容变化,修改后的数据内容的地址发生变化
list1 = [1, 2.1, 'baikal']
print(f'list1:{list1} 地址:{id(list1)} || {list1[2]} {id(list1[2])}')
list1[2] = 'python'
print(f'list1:{list1} 地址:{id(list1)} || {list1[2]} {id(list1[2])}')

# ! 列表在赋值的特点
list1 = [1, 2.1, 'baikal']
list2 = list1
list2[0] = 500
print("list2=", list2)
print("list1=", list1)


# ! 8.列表在函数传参时的特点
def f1(list):
    list[0] = 100
    print("list的id:", id(list))


list10 = [1, 2.1, 200]
print("list10的id", id(list10))
f1(list10)
print("list10:", list10)
