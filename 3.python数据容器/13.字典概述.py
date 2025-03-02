#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :13.字典概述.py
# @Time      :2024/05/19 10:13:38
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# 需求: 员工信息管理
"""
一个公司有多少个员工,请使用合适的数据类型来保存员工信息,(比如员工号,年龄,名字,入职时间,薪水)
1.员工号是入职时分配的,唯一不重复
2.通过员工号可以查询到员工信息
3.根据需要可以动态的增加、删除员工
4.根据需要我们可以修改员工的信息(年龄,名字,入职时间,薪水)
"""
# 目前这种需求是通过xx查询yy的需求
# 在编程中我们通常称为基于key查询value场景需求,是一种映射关系,key我们称为(键/关键字),value称为(值)
# 在前面学习的列表,元组,集合都是单值存储的,处理映射关系就不方便了
# 解决方案->字典dict

# !字典的定义,创建一个字典,只要用逗号分隔不同的元素,用{}括起来即可,存储的元素是一个一个的"键值对",
# !dict_a={key1:value1,key2:value2,key3:value3}
# !通过key取出对应的value值->字典名[key]

# dict_a[key1]

# 定义字典
tel = {'jack': 4098, 'tom': 4039}
print(f"dict_tel:{tel}类型是:{type(tel)}")
# 查询jack的tel
print('jack的tel:', tel['jack'])
# 如果键不存在会报KeyError的错误
# print('jack的tel:', tel['jack!'])

# 字典的使用细节和注意事项
# !字典的Key(关键字)通常是字符串或数字,Value可以是任意数据类型

dict_a = {
    'jack': [100, 200, 300],
    'mary': (10, 20, 'hello'),
    'alan': {'apple', 'pear'},
    'smith': '计算机老师',
    'baikal': {
        '性别': '男',
        'age': 18,
        '地址': '北京'
    },
    'key1': 100,
    'key2': 9.8,
    'key3': True
}
print(f'dict_a:{dict_a}类型是:{type(dict_a)}')

# ! 1.字典不支持索引,会报KeyError
# print(dict_a[0])
# ! 2.既然字典不支持索引,所以对字典进行遍历不支持while,只支持for,注意直接对字典进行遍历,遍历得到的是key
dict_b = {'one': 1, 'two': 2, 'three': 3}
# 1.方法一依次取出key,在通过dict[key]取出对应的value
for key in dict_b:
    print(f"key: {key} value:{dict_b[key]}")
# 2.方法二依次取出value
for value in dict_b.values():
    print(f"value : {value}")
# 3.方法三依次取出key-value
for k, v in dict_b.items():
    print(f"key:{k} value:{v}")

# ! 3.创建空字典可以通过{}或者dict()
dict_c = {}
dict_d = dict()
print(f"dict_c:类型是{type(dict_c)}")
print(f"dict_d:类型是{type(dict_d)}")

# ! 4.字典的key必须是唯一的,如果你指定了多个相同的key,后面的键值对会覆盖前面的
# dict_e = {'one': 1, 'two': 2, 'two': 200}
# print(f"dict_e:{dict_e}")  # {'one': 1, 'two': 200}
