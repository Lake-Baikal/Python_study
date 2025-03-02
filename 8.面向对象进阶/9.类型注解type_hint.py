#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   9.类型注解type_hint.py
@Time    :   2025/02/16 15:49:13
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# 为什么需要类型注解
# 随着项目越来越大,代码也越辣越多,在这种情况下,如果没有类型注解,很容易记不清某个方法的参数类型是什么.
# 一但传入错误类型的参数,Python是解释性语言,只有在运行时才能发现问题,这对大型项目来说是巨大的灾难


# 案例  对字符串进行遍历
# a: str :给形参a进行类型注解,标注a的类型是str
from typing import Union


def fun1(a: str) -> str:
    for ele in a:
        print(ele)


# 如果类型传入错误,就会出现异常
fun1("100")
# ! 类型注解作用和说明
# 自python3.5开始,引入了类型注解机制,作用和说明如下
"""
1.类型提示,防止运行时出现参数类型,返回值类型,变量类型不符合
2.作为开发文档附加说明,方便使用者调用时传入和返回参数类型
3.加入后并不会影响程序的运行,不会报正式的错误,只会提醒
4.Pycharm支持类型注解,参数类型错误会报黄色提示
"""
# !变量类型注解
# 基本语法
# 变量:类型
# 基础数据类型的注解
n1: int = 10  # 对n1进行类型注解,标注n1的类型为int
n2: float = 10.0
is_pass: bool = True
name: str = "Baikal"
# ! 注意如果给出的值的类型和标注的类型不一致,则Pycharm会给黄色警告


# ! 实例对象类型注解
class Cat:
    pass


# cat: Cat :对cat进行类型注解,标注cat的类型是Cat
cat: Cat = Cat()

# !容器类型注解
my_list: list = [100, 200, 300]  # 对my_list进行类型注解,标注my_list类型为list
my_tuple: tuple = ("run", "sing", "fly")
my_set: set = {"jack", "tim", "Baikal"}
my_dict: dict = {"no1": "北京", "no2": "上海"}
# !容器类型详细注解
# 对my_list2进行类型注解:标注my_list2类型是list,而且该list元素是int
my_list2: list[int] = [100, 200, 300]
# 元组类型设置详细类型注解,需要把每个元素类型都标注一下
my_tuple2: tuple[str, str, str, float] = ("run", "string", "fly", 1.1)
my_set2: set[str] = {"jack", "tim", "baikal"}
# 字典类型设置的详细类型注解,需要设置两个类型,即[key类型,value类型]
# 对my_dict2: dict[str, int]进行类型注解,标注my_dict2的类型是dict,而且key的类型是str,values类型是int
my_dict2: dict[str, int] = {"no1": 100, "no2": 200}

# !在注释中使用注解
#  type: float 用于标注,变量n3 的类型是float
n3 = 89.9  # type: float
my_list = [100, 200, 300]  # type:list[int]
email = "123456@gmail.com"  # type:str


# ? 函数方法的类型注释
"""
基本语法
def  函数/方法名(形参名:类型,形参名:类型 ...) ->返回值类型
     函数/方法体
"""
# ! name:str 对形参name进行类型注解:标注name的类型是str
# 如果在调用方法/函数,传入的实参类型不是一样的,则出黄色的警告


def fun1(name: str) -> str:
    for ele in name:
        print(ele)


fun1("Baikal")


# a: int, b: int :对形参a,b进行类型注解,标注a,b的类型为int
# -> int:对返回值进行类型注解,标注返回值的类型外int
def fun2(a: int, b: int) -> int:
    return a + b


print(f"结果为:{fun2(10, 20)}")


# 类型注解是提示性的,并不是强制性的,如果你给的类型和指定/标注的类型不一致,Pycharm检测到会给黄色的警告但是仍然可以运行
def fun2(a: int, b: int) -> int:
    return a + b


print(f"结果是:{fun2(10.1, 20)}")

# ! Union 类型注解
#  Union 类型可以定义联合类型注解
# 在变量,函数(方法) 都可以使用Union联合类型注解
# 使用的时候,需要向导入Union :from typing import Union
# !基本语法
# Union[类型,类型...]
# 比如:联合类型:Union[X,Y]等价于X|Y ,意味着满足X或者Y之一

# !如果有使用Union联合注解,则需要导入Union
# from typing import Union

# !联合类型注解 : a可以是int或者str
a: Union[int, str] = 100

# my_list 是list类型,元素可以是int或者str
my_list: list[Union[int, str]] = [100, 200, 300, "tim"]


# !在函数或者方法中使用联合类型注解
# 接收两个数,(可以是int/float),返回数(int/float)
def cal(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return float(num1 + num2)


def cal1(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2


print(f"结果是:{cal(10, 20.2)}")
print(f"结果是:{cal1(10, 20.2)}")
