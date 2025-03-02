#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2.顺序查找.py
# @Time      :2025/01/07 00:09:45
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
顺序查找案例:有一个列表,alan,baikal,tom,jacky猜名字游戏,从键盘中任意输入一个名称,判断列表中是否包含此名[顺序查找]
要求如果找到了就提示找到了,并给出下标值
!如果我们只是完成查找功能,我们可以直接使用list的方法index如下
"""
names_list = ['alan', 'baikal', 'baikal', 'tom', 'jacky']
find_name = "baikal"

# 使用list.index完成查找
# res_index = names_list.index(find_name)
# print("res_index", res_index)


# !除了掌握系统提供的index(),程序员也应该掌握一些基本的查找方法
def seq_search(my_list, find_val):
    """_summary_
      Args:
          my_list (_type_): _description_ # 顺序查找指定的元素 my_list:传入的列表(即要查找的列表)
          find (_type_): _description_ # find_val 要查找的值,即要返回的值和元素
          return:如果找到返回对应的索引值,否则返回-1
    """
    """
        思路分析:
        1.对列表进行遍历,如果找到了,则返回对应的下标
        2.如果遍历结束则没有找到则返回-1
    """

    find_index = -1
    # 遍历列表
    for i in range(len(my_list)):
        # 开始比较,如果当前的元素就是比较的值则返回当前的元素
        if my_list[i] == find_val:
            print(f"恭喜,找到对应的值{find_val}下标是{i}")
            find_index = i
            break  # 退出for循环
    else:
        print(f"没有找到对应的值{find_val}")

    return find_index


# 测试
res_index = seq_search(names_list, find_name)
print("res_index", res_index)
"""
如果一个列表中有多个要查找的元素/值,比如两个baikal,请思考怎么把满足查询条件的元素的下标,都返回
"""
# !思路分析
# !1.顺序查找列表,把满足查询条件的元素的下标都返回
# !2.定义一个空列表,用空列表保存查找到的索引下标,发现一个就动态添加到列表
# !3.最后返回列表


def seq_search2(my_list, find_val):
    # 定义一个空列表
    find_index = []
    # 遍历列表
    for i in range(len(my_list)):
        # 开始比较,如果当前的元素就是比较的值则保存到空列表中find_index = []
        if my_list[i] == find_val:
            # 将找到的下标添加到find_index
            find_index.append(i)

    return find_index


res_index = seq_search2(names_list, find_name)
print("res_index", res_index)
