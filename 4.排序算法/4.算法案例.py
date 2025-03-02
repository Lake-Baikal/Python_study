#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :4.算法案例.py
# @Time      :2025/01/08 20:53:20
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
import random
# !随机生成10个整数(1~100的范围),保存到列表,使用冒泡排序,对其进行从大到小的排序
lst_num = []
for _ in range(10):
    lst_num.append(random.randint(1, 100))

print("排序前", lst_num)


# 使用冒泡排序,对其从大到小排序
def bubble_sort(my_list):
    """_summary_
    # 功能:对传入的列表进行排序,从大到小或者从小到大
    Args:
        my_list (_type_): _description_ 传入的列表
        :return 无返回值
    """

    # !使用i变量来控制多少轮排序 len(my_list)-1
    for i in range(0, len(my_list) - 1):
        for j in range(0, len(my_list) - 1 - i):
            # 如果前面的元素大于后面的元素就交换
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        # print(f"第{i+1}轮排序后的结果my_list", my_list)


# 完成排序
bubble_sort(lst_num)
print("排序后", lst_num)


# !在第一题目的基础上,使用二分查找,查找是否有8这个数,如果有则返回对应的下标,如果没有则返回-1，提示这里查找的列表是从小到大
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
        if my_list[mid_index] < find_val:
            right_index = mid_index - 1
            # 如果mid_val < find_val,则到mid_val的右边查找
        elif my_list[mid_index] > find_val:
            left_index = mid_index + 1
            # 如果mid_val == find_val,则找到返回对应的下标即可
        else:
            find_index = mid_index
            break  # 找到一个就退出循环
    return find_index


# 完成排序
result_index = binary_search(lst_num, 8)
if result_index == -1:
    print("没有在列表中找到8")
else:
    print(f"在列表中找到8,对应的下标和索引是{result_index}")
