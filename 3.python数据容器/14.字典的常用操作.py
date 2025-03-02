#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :14.字典的常用操作.py
# @Time      :2024/05/20 00:51:35
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

dict_a = {"one": 1, "two": 2, "three": 3}
# ! 1.len(d):返回字典d的项数
print(f"dict_a的元素个数是:{len(dict_a)}")
# ! 2.d[key]:返回字典中以key为键的项,如果映射中不存在key则会引发keyError
print("key为three对应的value:", dict_a["three"])
# print("key为three对应的value:", dict_a["three_aa"])  # KeyError: 'three_aa'
# ! 3.d[key]=value:将d[key]设为value,如果key已经存在，则是修改value,如果key没有存在则是怎加key-value
# !注意会直接修改原来的字典
# 需求:修改key="one"对应的value为 第一
dict_a["one"] = "第一"
print(f"dict_a的值为{dict_a}")

# ! 4.添加:增加key为'four' value为4
dict_a['four'] = 4
print(f"dict_a的值为{dict_a}")
# ! 5.删除 del d[key] 将d[key]从d中移除,如果映射中不存在key则会引发keyError
# 需求:删除key为four的元素
del dict_a["four"]
print(f"dict_a的值为{dict_a}")
# del dict_a["four_aaa"]
# print(f"dict_a的值为{dict_a}")  # KeyError: 'four_aaa'
# !6.pop(key[,default])
# !如果 key存在于字典中则将其移除并返回其值,否则返回default
# !如果default未给出且key不存在于字典中,则会引发keyError
# 要求:将key为'one'的值返回,并将该元素从字典移除
# val = dict_a.pop('one')
val = dict_a.pop('one_aaa', "baikal")
print(f"val:{val}")
print(f"dict_a的值为{dict_a}")

# ! 7. keys():返回字典所有的key
dict_a_key = dict_a.keys()
print(f"dict_a_key:{dict_a_key} 类型:{type(dict_a_key)}")

# ! 8. key in d:如果d中存在键key则返回True,否则返回False
# 判断字典中是否存在key 'two'
print("two" in dict_a)

# !9. clear():移除字典中所有元素
# 将字典清空
dict_a.clear()
print(f"dict_a:{dict_a}")

# !字典生成式
# 给出两个列表如下
books = ['红楼梦', '三国演义', '水浒传', '西游记']
authors = ['曹雪芹', '罗贯中', '施耐庵', '吴承恩']
# 生成对应的字典
# {'红楼梦': '曹雪芹', '三国演义': '罗贯中', '水浒传': '施耐庵', '西游记': '吴承恩'}

# 字典生成式的基本语法
# !zip()可以将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，返回由这些元组组成的列表
# {字典key的表达式: 字典value的表达式 for 表示key的变量, 表示value的变量 in zip(可迭代对象, 可迭代对象)}
dict_book = {book: author for book, author in zip(books, authors)}
print(dict_book)

str1 = "baikal"
dict_str = {ele1: ele2 * 2 for ele1, ele2 in zip(str1, str1)}
print(dict_str)

# 案例
english_list = ['red', 'blue', 'yellow', 'white']
chinese_list = ['红色', '蓝色', '黄色', '白色']
# 生成一个字典
# {"红色": "RED", '蓝色': "BLUE", '黄色': 'YELLOW', '白色': 'WHITE'}
dict_color = {
    ele1: ele2.upper()
    for ele1, ele2 in zip(chinese_list, english_list)
}
print("dict_color: ", dict_color)

# 需求: 员工信息管理
"""
一个公司有多少个员工,请使用合适的数据类型来保存员工信息,(比如员工号,年龄,名字,入职时间,薪水)
1.员工号是入职时分配的,唯一不重复
3.根据需要可以动态的增加、删除员工
"""
clerks = {
    "0001": {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "sal": 12000
    },
    "0002": {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "sal": 10000
    },
    "0010": {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "sal": 20000
    }
}
# 2.通过员工号(0010)可以查询到员工信息

print(f"员工号为0010的信息为: 名字: {clerks["0010"]["name"]}"
      f"年龄: {clerks["0010"]["age"]}"
      f"入职时间: {clerks["0010"]["entry_time"]}"
      f"薪水: {clerks["0010"]["sal"]}")
print(115*"-")

# 3.根据需要可以动态的增加、删除员工.
# 增加:(员工号:0020,年龄:30,名字:"baikal",入职时间:"2020-08-10",薪水:10000)
clerks["0020"] = {
    "age": 30,
    "name": "Baikal",
    "entry_time": "2020-08-10",
    "sal": 10000
}
print("clerks:", clerks)

# 删除0001的员工
print(115*"-")
del clerks['0001']
print('clerks', clerks)

# 4.根据需要我们可以修改员工的信息(年龄,名字,入职时间,薪水)
# 修改员工号为0020的名字:Alan,入职时间:1999-10-10,薪水在原来的基础上增加10%

clerks["0020"]["name"] = "Alan"
clerks["0020"]["entry_time"] = "1999-10-10"
clerks["0020"]["sal"] += clerks['0020']['sal'] * 0.1

print(115*"-")
print('clerks', clerks)

# !遍历所有员工,把所有员工的薪水在原工资的基础上增加20%
keys = clerks.keys()
for key in keys:
    clerks[key]['sal'] += clerks[key]['sal'] * 0.2
print("clerks", clerks)

# 按照如下格式输出所有员工信息
# 员工号为??的信息如下:年龄:??,名字:??,入职时间:??,薪水:??
for key in keys:
    print(f"员工号为{key}的信息如下:"
          f"年龄:{clerks[key]['age']}"
          f"名字:{clerks[key]['name']}"
          f"入职时间:{clerks[key]['entry_time']}"
          f"薪水:{clerks[key]['sal']}")
for key in keys:
    clerk_info = clerks[key]
    print(f"员工号为{key}的信息如下:"
          f"年龄:{clerk_info['age']}"
          f"名字:{clerk_info['name']}"
          f"入职时间:{clerk_info['entry_time']}"
          f"薪水:{clerk_info['sal']}")
