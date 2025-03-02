#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6.元组的使用细节.py
# @Time      :2024/04/30 17:23:37
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# !1.如果我们需要一个空元组,可以通过()或者tuple()方式来定义
# tuple_a = ()
# tuple_b = tuple()
# print(f"tuple_a的内容是{tuple_a} 类型是{type(tuple_a)}")
# print(f"tuple_b的内容是{tuple_b} 类型是{type(tuple_b)}")

# !2.元组的元素可以有多个,而且数据类型没有限制(甚至可以嵌套元组),允许有重复元素,而且是有序的

# tuple_c = (100, 'jack', 4.5, True, 'jack')
# print(tuple_c)
# tuple_d = (100, 'jack', ('天龙八部', '笑傲江湖', 300))
# print(tuple_d)

# !3.元组的索引/下标从0开始
# !4.元组索引必须在指定的范围内使用,否则报IndexError:list index out of range
# tuple_d = (1, 2, "baikal")有效下标为0-2
# tuple_d = (1, 2, "baikal")
# # 索引越界
# print(tuple_d[3])
# !5.元组是不可变序列,不能修改
# tuple_e = (1, 2.1, 'baikal')
# tuple_c = (100, 'jack', 4.5, True, 'jack')
# tuple_c = (100, 'jack', 4.5, True, 'jack')
# tuple_e[2] = "python"  # 'tuple' object does not support item assignment

# !6.可以修改元组内list内容(包括修改,增加,删除等)
tuple_f = (1, 2.1, 'baikal', ['jack', True, False])
# 访问元组中list及元素
print(tuple_f[3])
print(tuple_f[3][0])
# 修改
tuple_f[3][0] = "Tom"
print(f"tuple_f内容是{tuple_f}")

# !错误的修改
# !不能替换整个列表元素,因为元组里面的元素不能修改,所以不能更改元组里面的列表
# tuple_f[3] = [1, 2, 3]
# print(f"tuple_f内容是{tuple_f}")

# 删除
del tuple_f[3][0]
print(tuple_f)

# 增加
tuple_f[3].append("smith")
print(f"tuple_f的内容是{tuple_f}")
# 如下语法错误
# tuple_f.append("abc")

# !7.索引也可以从尾部开始,最后一个元素的索引为-1,往前一位是-2,以此类推
tuple_g = (1, 2.1, 'baikal', ['jack', 'Tom', 'mary'])
print(tuple_g[-2])

# !8.定义只有一个元素的元组,需要带上逗号,否则就不是元组类型,而是int 类型
tuple_h = (100)
print(f"tuple_h的类型是{type(tuple_h)}")  # tuple_h的类型是<class 'int'>
# !正确写法
tuple_h = (100, )
print(f"tuple_h的类型是{type(tuple_h)}")

# !9.既然有了列表,python设计者为什么还要提供元组这样的数据类型?
"""
!1.在项目中,尤其是多线程环境中,有经验的程序员会考虑使用不变对象,一方面是因为对象状态不能修改,可以避免由此引发的不必要程序错误,另一方面一个不变的对象自动线程就是安全的,这样可以省掉处理同步化的开销,可以方便被共享访问,所以,如果不需要对元素进行添加删除修改的情况下,可以考虑使用元组
!2.元组在创建时间和占用的空间上面优于列表
!3.元组能够对不需要修改的数据写保护
"""
