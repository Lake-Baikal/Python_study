#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :11.集合的概述.py
# @Time      :2024/05/09 20:30:40
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# !python支持集合这种数据类型,集合是由不重复元素组成的无序容器
# 不重复元素:简单来说就是集合中不会有相同的元素
# 无序:集合中元素取出的顺序和定义时元素顺序并不能保持一致
# !集合对象支持合集,交集,差集等数学运算
# !在开发中我们可能会有这些需求,需要记录一些数据,而这些数据必须保证不重复,而且数据类型顺序并没有要求就可以考虑集合

# !集合的定义:创建一个集合,只要用逗号分隔不同的数据项,并且用{}括起来即可
set_a = {100, 200, 300, 400, 500}
basket = {'apple', 'orange', 'pear', 'banana'}
print(f"set_a的内容是{set_a}类型是{type(set_a)}")

# !注意事项和使用细节

# !1.集合是由不重复元素组成的无序容器,不重复元素组成可以理解为自动去重
basket = {'apple', 'apple', 'orange', 'orange', 'pear', 'banana'}
print(basket)

# !2.无序也就是你定义的元素顺序和取出顺序不能保持一致
# !集合低层会按照自己的一套算法来存储和取数据,所以每次取出顺序是不变的
set_a = {100, 200, 300, 400, 500}
print(f"set_a:{set_a}")
print(f"set_a:{set_a}")
print(f"set_a:{set_a}")

# !3.集合不支持索引
# set_b = {100, 200, 300, 400, 500}
# print(set_b[0])

# !4.集合不支持索引,所以对集合进行遍历不支持while循环,只支持for循环

basket = {'apple', 'apple', 'orange', 'orange', 'pear', 'banana'}
for element in basket:
    print(element)

# !5.创建空集合只能用set(),不能使用set={},{}创建的是空字典
set_c = {}
set_d = set()
print(f"set_c:{set_c} 类型:{type(set_c)} set_c:{set_d} 类型:{type(set_d)}")
