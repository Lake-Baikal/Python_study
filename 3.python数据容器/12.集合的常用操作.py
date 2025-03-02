#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :12.集合的常用操作.py
# @Time      :2024/05/13 22:10:55
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# ! len(集合):集合元素个数,去重后的结果
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("basket的元素个数:", len(basket))
# ! x in s:检测x是否为s中的成员 在返回True否则返回False
# 需求判断apple是否在集合中
print("apple" in basket)
# !add(elem):将元素添加到集合中
# 需求将grape添加到集合中,集合是无序的,添加的顺序和显示的顺序不一致
basket.add("grape")
print("basket的元素个数:", basket)
# ! remove(elem):从集合中移除元素elem如果elem不存在于集合中则会引发keyError
# 需求:将apple从集合中移除
# basket.remove("apple")
# basket.remove("aaa")  # KeyError: 'aaa'
print("basket的元素个数:", basket)
# !pop():从集合中移除并返回任意一个元素,如果elem不存在于集合中则会引发keyError
ele = basket.pop()
print("ele:", ele, "类型是:", type(ele))
# !注意pop()操作会影响到原集合
print("basket的元素个数:", basket)
# ! union(*others):返回一个新集合,求并集
# !其中包含来自原集合以及others指定的所有集合中的元素(两个集合的并集并且去重后的结果)
# 需求:将books和books_2进行合集操作,即求出books集合或者在books_2集合的元素
books = {"天龙八部", "雪山飞狐"}
books_2 = {"笑傲江湖", "神雕侠侣", "天龙八部"}
books_3 = books.union(books_2)
# 写法2
books_3 = books | books_2
print(books_3)

# !intersection(*other) 返回一个新集合,其中包含原集合以及others指定的所有集合中共有的元素,求交集
# 对books和books_2求交集,即求出既在books又在books_2集合中的元素
books_4 = books.intersection(books_2)
# 写法2
books_4 = books & books_2
print("books_4->", books_4)

# !求差集 difference(*others):返回一个新集合,其中包含原集合中在others指定的其他集合中不存在的元素
# 求出只存在books集合的元素
books_5 = books.difference(books_2)
# 写法2
books_5 = books - books_2
print("books_5", books_5)
# 求出只存在books_2集合的元素
books_6 = books_2.difference(books)
books_6 = books_2 - books
print("books_6", books_6)

# !集合生成式
# !基本语法 {集合元素表达式for 自定义变量 in 可迭代对象}
set = {ele * 2 for ele in range(1, 5)}
print("set:", set)
set2 = {ele + ele for ele in "baikal"}
print(set2)
# !集合生成式和列表生成式的区别在于,集合生成式使用{},列表生成式使用[]

# 案例
s_history = {"小明", "张三", "李四", "王五", "lily", "Bob"}
s_politic = {"小明", "小花", "小红", "baikal"}
s_english = {"小明", "Tom", "李四", "lily", "Bob"}
# 求选课学生总共多少人
# 求只选了第一个学科history的学生数量和学生名字
# 求只选了一门学科的学生数量和学生名字
# 求选了三门学科的学生数量和学生名字
"""
1.对三个集合求并集,自动去重,对新的集合求len()
2.求出只选s_history学员,使用差集即可,s_history - s_politic -s_english
3.先求出只选择了history的学生,在求出只选择了politic的学生,在求出只选择english的学生,然后求并集集合
4.求出既在s_history 又在 s_politic 还在 s_english 就是对三个集合求交集
"""
print(f"求选课总人数有多少人:{len(s_history | s_english | s_politic)}人")
print(
    f"求只选了第一个学科history的学生数量{len(s_history - s_politic - s_english)}和学生名字{s_history - s_politic - s_english}"
)
s1 = s_history - s_politic - s_english
s2 = s_politic - s_english - s_history
s3 = s_english - s_politic - s_history
print(f"求只选了一门学科的学生数量{len(s1 | s2 | s3)}和学生名字{s1 | s2 | s3}")
print(
    f"选了三门学科的学生数量{len(s_history & s_politic & s_english)}和学生名字{s_history & s_politic & s_english}"
)
