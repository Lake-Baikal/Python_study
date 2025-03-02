#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3.函数的注意事项.py
# @Time      :2024/04/07 00:38:53
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# 函数的注意事项和使用细节
# !1.函数的参数列表可以是多个(n1,n2,...),也可以没有()
# !2.函数的命名遵循标识符命名规则和规范,
"""
不可以用数字开头命名函数
def 2f():
  print("2f")

不能用减号命名函数
def a-b():
    print("a-b")
"""

# !函数中的变量是局部的,函数外不生效
"""
def hi():
    n = 10
    print("n", n)


hi()
# 函数内部定义的n在函数外部不能使用
print("n=", n)
 """

# ! 如果同一个文件,出现两个函数名相同的函数,则以就近原则进行调用
"""
def cry():
    print("cry()..hi..")


def cry():
    print("cry()..ok..")

# *这个cry 会默认就近原则,即第二个cry()
cry()
"""
"""
!调用函数时,根据函数定义的参数位置来传递参数,这种传参方式为位置传参,传递的实参和定义的形参顺序个数必须一致，同时定义的形参,不用指定数据类型,根据传入的实参决定
! 传递的实参和定义的形参顺序和个数必须一致,否则会报TypeError错误
"""

# def car_info(name, price, color):
#     print(f"name->{name} price->{price}->color->{color}")

# ! 传递的实参和定义的形参顺序和个数必须一致,否则会报TypeError错误

# car_info("宝马", 50000, "red", 11)
# car_info("宝马", 50000, "red")
# TypeError: car_info() takes 3 positional arguments but 4 were given
"""
# ! 函数可以有多个返回值
比如函数接收两个数,返回这两个数的和,差
"""

# def f2(n1, n2):
#     return n1 + n2, n1 - n2

# r1, r2 = f2(10, 20)
# print(f"r1->{r1} r2->{r2}")
"""
! 函数支持关键字参数
函数调用时,可以通过"形参名=实参值"形式传递参数
这样可以不受参数传递的顺序限制
"""


def book_info(name, price, author, amount):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 通常的调用方式,一一对应
# book_info("红楼梦", 60, "曹雪芹", 30000)
# book_info("红楼梦", "曹雪芹", 60, 30000)

# !关键字参数

# book_info(name="红楼梦", price=60, amount=30000, author="曹雪芹")
# book_info("红楼梦", 60, amount=30000, author="曹雪芹")
"""
# !函数支持默认参数/缺省参数
# !定义函数时,可以给参数提供默认值,调用函数时,指定了实参,则以指定为准,没有指定则以默认值为准
"""


def book_info2(name='《thinking in python》',
               price=66.8,
               author="龟叔",
               amount=1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 调用测试
book_info2()
# 指定第一个参数
book_info2("《study python》")

# !默认参数,需要放在参数列表之后


def book_info3(name, price, author="龟叔", amount=1000):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


# 调用测试
book_info3("《study python》", 999)

# 错误写法
# def book_info3(author="龟叔", name, price, amount=1000):
#     print(f"name->{name} price->{price} author->{author} amount->{amount}")

#  调用测试
# book_info3("《study python》", 999)
"""
# !函数支持可变参数/不定长参数
# 当调用函数时,不确定传入多少个实参情况
# 传入的多个实参会被组成一个元组(tuple),元组可以存储多个数据项
"""


# 比如我们要计算多个数字的和,但是不确定是几个数 *代表通配符,0到多个
def sum(*args):  # args->(1, 2, 100, 98)
    print(f"args->{args} 类型是->{type(args)}")
    total = 0
    for element in args:
        total += element
    return total


result = sum(1, 2, 100, 98)
print(f"result->{result}")
result = sum()
print(f"result->{result}")
"""
! 函数的可变参数/不定长参数还支持多个关键字参数,也就是多个"形参名=实参值"
# 当调用函数时,不确定传入多少个关键字参数的情况
# 传入的多个关键字参数,会被组成一个字典(dict),字典可以存储多个键=值的数据项
"""


# 比如我们需要接收一个人的信息,但是有那些信息我们不确定,就可以使用关键字可变参数(**args)
def person_info(**args):
    # 输出args的数据和类型
    print(f"args->{args} 类型->{type(args)}")
    # 遍历args,是一个字典,下面arg_name就是取出的各个参数名
    # args[arg_name]就是参数值
    for arg_name in args:
        print(f"参数名->{arg_name} 参数值->{args[arg_name]}")


person_info(name="baikal", age=18, email="baikal.com")
person_info(name="baikal", age=18, email="baikal.com", sex="男")
person_info()

# !python调用另一个.py文件的函数
# f1.py文件
# def add(x, y):
#     print(x, y)

# f2.py文件
# import f1

# f1.add(1, 2)
