#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2.导入模块.py
# @Time      :2025/01/11 17:37:06
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# ? 模块的导入
# 模块Module是什么
# 1.模块是一个py文件,后缀名是.py
# 2.模块可以定义函数,类,变量,模块里也可以包含可执行的代码

# ? 模块的作用是有哪些
# 1.当函数,类,变量很多时,可以很好进行管理
# 2.开发中,程序员可以根据业务需要,把同一类型的功能代码,写入一个模块文件中,既方便管理也方便调用
# 3.一个模块就是一个工具包,供程序员开发使用,提高开发效率
# 4.python自带标准模块库,每个模块可以帮助程序员快速实现相关的功能
# !模块导入的基本语法
# ! [from 模块名] import (函数|类|变量*) [as 别名]
"""
解读
[]是可选项
可以根据需求,选择合适的形式进行导入
"""

# ! 1.导入一个或多个模块
# import 模块
# import 模块1, 模块2 ...
"""
导入一个或多个模块,建议导入多个模块时,还是一行导入一个模块
使用:模块.xx 方式来使用相关的功能, . 表示层级关系,即模块中的xx
import语句通常写在开头
"""

# import math, random
# 得到一个数的绝对值
import math
import random

print(math.fabs(-11.2))
# 从列表中随机返回一个元素
print(random.choice(['apple', 'banana', 'pear']))

# 导入模块的指定的功能
# from 模块 import 函数 、函数、类
"""
导入模块的指定功能
使用:因为导入了具体的函数 、类、变量直接使用即可,不需要再带模块名
"""
# 解读:导入math模块的fabs函数
from math import fabs
# 返回x的绝对值
print(fabs(-11.2))
# 导入模块的全部功能
# from 模块 import *
"""
导入模块的全部功能,
直接使用不需要带模块名
"""
from math import *

# 返回x的绝对值
print(fabs(-234.5))
# 返回x的平方根
print(sqrt(9))

# 给导入的模块或者功能取别名
# import 模块 as 别名
# from 模块 import 函数 类 变量 ...as 别名
"""
import 模块 as 别名 :给导入的模块取别名,使用别名:别名.xx
from 模块 import 函数 、类 、变量 ...as 别名 :给导入的某个功能取别名,使用时,直接用别名即可
"""
# import 模块 as 别名
import random as r

# from 模块 import 函数 、类 、变量 ...as 别名
from math import fabs as fa

print(r.choice([100, 200, 300, 400]))
print(fa(-900.2))
