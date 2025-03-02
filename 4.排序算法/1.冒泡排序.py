#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.冒泡排序.py
# @Time      :2025/01/05 16:26:49
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
排序算法有
1.冒泡排序
2.选择排序
3.插入排序
4.希尔排序
5.归并排序
6.快速排序
7.堆排序
"""
# !排序是将多个数据按照指定的顺序进行排序的过程
"""
!冒泡排序(bubble Sorting)的基本思想是:重复地走访需要排序的元素列表,依次比较两个相邻的元素,如果顺序(如从大到小或者从小到大)错误就交换他们的位置.重复的进行直到没有相邻的元素需要交换。则元素列表排序完成。
!在冒泡排序中,值最大或最小的元素会通过交换慢慢的"浮"到元素的列表和"顶端"。就像冒泡一样,所以称为冒泡排序。
"""

# !冒泡排序的案例
# 列表:[24,69,80,57,13]有五个元素,使用冒泡排序法将其排成一个从小到大的有序列表
# !如果只是完成排序功能,我们可以直接使用list的方法sort,如下
# 排序的列表
num_list = [24, 69, 80, 57, 13, 0, 900, -30]

# print("排序前".center(32, '-'))
# print(f"num_list:{num_list}")

# 使用sort方法完成排序
# num_list.sort()
# print("排序后".center(32, '-'))
# print(f"num_list:{num_list}")


# !使用冒泡排序,自己完成排序,目的了解底层原理,深入理解(以后遇到不同的业务,需要定制排序,也能处理)
# !定义函数完成排序
def bubble_sort(my_list):
    """_summary_
    # 功能:对传入的列表进行排序,从大到小或者从小到大
    Args:
        my_list (_type_): _description_ 传入的列表
        :return 无返回值
    """
    """
    通过分析此我们发现每一轮的比较逻辑是一样的
    我们只需要考虑变化的部分即可,使用外层的for循环来处理
    """
    # !使用i变量来控制多少轮排序 len(my_list)-1
    for i in range(0, len(my_list) - 1):
        for j in range(0, len(my_list) - 1 - i):
            # 如果前面的元素大于后面的元素就交换
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i + 1}轮排序后的结果my_list", my_list)
    """
   第一轮排序：把最大的数放到最后面的位置
   第1次比较的结果[24,69,80,57,13]
   第2次比较的结果[24,69,80,57,13]
   第3次比较的结果[24,69,57,80,13]
   第4次比较的结果[24,69,80,13,80]
"""
    # !使用j变量用来控制比较的次数同时可以作为比较元素的索引和小标

    # for j in range(0, 4):
    #     # 如果前面的元素大于后面的元素就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    # print("第一轮排序后的结果my_list", my_list)
    """
    第二轮排序：把第二大的数放到倒数第二的位置
    第1次比较的结果[24,69,80,13,80]
    第2次比较的结果[24,57,69,13,80]
    第3次比较的结果[24,57,13,69,80]
    """
    # for j in range(0, 3):
    #     # 如果前面的元素大于后面的元素就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    # print("第二轮排序后的结果my_list", my_list)
    """
    第三轮排序：把第三大的数放到倒数第三的位置
    第1次比较的结果[24,57,13,69,80]
    第2次比较的结果[24,13,57,69,80]

    """
    # for j in range(0, 2):
    #     # 如果前面的元素大于后面的元素就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    # print("第三轮排序后的结果my_list", my_list)
    """
    第四轮排序：把第四大的数放到倒数第四的位置
    第1次比较的结果[13,24,57,69,80]
    """
    # for j in range(0, 1):
    #     # 如果前面的元素大于后面的元素就交换
    #     if my_list[j] > my_list[j + 1]:
    #         my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    # print("第四轮排序后的结果my_list", my_list)


bubble_sort(num_list)
print("排序后".center(32, '-'))
print(f"num_list:{num_list}")
