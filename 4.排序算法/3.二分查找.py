#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3.二分查找.py
# @Time      :2025/01/07 21:40:26
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# !请对一个列表(元素是从小到大排序)进行二分查找,[1,8,10,89,1000,1234]输入一个数查看该列表是否存在此数,并求出下标,如果没有就返回-1
"""
二分查找的思路分析
前提：该列表是一个排好序的列表(为了分析方便就以从小到大的列表进行分析)
1.找到列表的中间数mid_val和find_val比较
2.如果mid_val > find_val,则到mid_val的左边查找
3.如果mid_val < find_val,则到mid_val的右边查找
4.如果mid_val == find_val,则找到返回对应的下标即可
5.不断的重复1~4步骤,这里就是不断的折半,使用while循环
6.如果while循环结束都没有找到,说明find_val没有在列表中
"""
# 要查看找的列表
num_list = [1, 8, 10, 89, 1000, 1234]
"""
# !注意事项
二分查找的前提是该列表已经是一个排好序的列表,从小到大或者从大到小
排好的顺序是从小到大还是从大到小会影响二分查找的代码逻辑
"""


# 编写二分查找的方法
def binary_search(my_list, find_val):
    """_summary_
    功能完成二分查找
  Args:
      my_list (_type_): _description_ 要查找的列表(该列表是有大小顺序的)
      find_val (_type_): _description_ 要查找的元素/值
      return:如果找到返回对应的下标,如果没有找到放回-1
  """
    # left_index表示左边的索引
    # right_index表示右边的索引
    left_index, right_index = 0, len(my_list) - 1
    # 定义找到数的下标
    find_index = -1
    # 使用while循环不断的折半比较,比较的前提是满足left_index<=right_index:
    while left_index <= right_index:
        # 中间数的下标/索引
        mid_index = (left_index + right_index) // 2
        # 如果mid_val > find_val, 则到mid_val的左边查找
        if my_list[mid_index] > find_val:
            right_index = mid_index - 1
            # 如果mid_val < find_val,则到mid_val的右边查找
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1
            # 如果mid_val == find_val,则找到返回对应的下标即可
        else:
            find_index = mid_index
            break  # 找到一个就退出循环
    return find_index


# 测试
res_index = binary_search(num_list, 1)
if res_index == -1:
    print("没有找到该数")
else:
    print(f"找到数,对应的下标{res_index}")
