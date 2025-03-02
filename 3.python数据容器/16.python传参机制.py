#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :16.python传参机制.py
# @Time      :2024/09/28 22:38:55
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.


# ?列表的传参机制
def f1(my_list):
    print(f"②f1() my_list:{my_list}地址是:{id(my_list)}")
    my_list[0] = "jack"
    print(f"③f1() my_list:{my_list}地址是:{id(my_list)}")


# !测试
my_list = ['tom', 'marry', 'baikal']
print(f"①my_list:{my_list} 地址是:{id(my_list)}")
# 调用函数
f1(my_list)
print(f"④my_list:{my_list} 地址是:{id(my_list)}")

# !结论,在函数内部修改了列表的元素值会影响到函数外的列表


# !元组的传参机制
def f2(my_tuple):
    print(f"②f2()my_tuple:{my_tuple} 地址是：{id(my_tuple)}")
    # 不能修改
    # my_tuple[0] = "red"
    print(f"③f2()my_tuple:{my_tuple} 地址是：{id(my_tuple)}")


# 测试
my_tuple = ("hi", "ok", "hello")
print(f"①f2()my_tuple:{my_tuple} 地址是：{id(my_tuple)}")
f2(my_tuple)
print(f"④f2()my_tuple:{my_tuple} 地址是：{id(my_tuple)}")

# !结论,元组无法修改


# !集合传参机制
def f3(my_set):
    print(f"②f2()my_set:{my_set} 地址是：{id(my_set)}")
    my_set.add("三国演义")
    print(f"③f2()my_set:{my_set} 地址是：{id(my_set)}")


# 测试
my_set = {"水浒传", "西游记", "红楼梦"}
print(f"①f2()my_set:{my_set} 地址是：{id(my_set)}")
f3(my_set)
print(f"④f2()my_set:{my_set} 地址是：{id(my_set)}")

# !结论,在函数内部修改了集合的元素值会影响到函数外的集合


# !字典传参机制
def f4(my_dict):
    print(f"②f2()my_dict:{my_dict} 地址是：{id(my_dict)}")
    my_dict['address'] = "蓝若寺"
    print(f"③f2()my_dict:{my_dict} 地址是：{id(my_dict)}")


# 测试
my_dict = {"name": "小倩", "age": 18}
print(f"①f2()my_dict:{my_dict} 地址是：{id(my_dict)}")
f4(my_dict)
print(f"④f2()my_dict:{my_dict} 地址是：{id(my_dict)}")
# !结论,在函数内部修改了字典的元素值会影响到函数外的字典
"""
小结
!python的数据类型主要分为整数int类型/浮点数float/字符串str/布尔值bool/元组tuple/列表list/字典dict/集合set
!数据类型分为两大类,一种是可变数据类型,一种是不可变数据类型
?可变数据类型:当该数据类型的值发生了变化,如果他的内存地址不变,那么这个数据类型就是可变数据类型
?不可变数据类型:当该数据类型的变量发生了变化,如果他的内存地址改变了,那么这个数据类型就是不可变数据类型
!不可变数据类型:数值类型(int,float) bool(布尔) string(字符串) tuple(元组)
!可变数据类型 :list(列表) set(集合) dict(字典)
"""

