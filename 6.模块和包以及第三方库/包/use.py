#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :use.py
# @Time      :2025/01/12 14:32:32
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# 导入包下面的模块
# import package.module01
# import package.module02

# 使用导入的模块
# package.module01.hi()
# package.module02.ok()

# from 包名 import 模块  这种方法导入在使用时, 模块.包名, 不用带包名
# from package import module01
# # 直接使用模块名.功能名
# module01.hi()

# 导入包的模块的指定函数、类、变量
# from package.module01 import hi
# # 直接使用功能名调用即可
# hi()
# form 包名.模块 import * 表示导入包的模块的所有功能
# from package.module01 import *

# hi()
# hello()
"""
!3.__init__.py通过__all__控制允许导入的模块
在__init__.py中增加__all__=[允许导入的模块列表]
针对from 包 import * 方式生效,对import xx方式不生效
"""
# from package import *

# module02.ok()

# # 引入限制了module01模块导入,因此不能使用
# module01.hi()

# import package.module01
# import package.module02

# package.module01.hi()
# package.module02.ok()

# 导入方式一
# import package.package2.module03
# # 使用:
# package.package2.module03.cal(10, 20)

# 导入方式二
# from package.package2.module03 import cal
# # 使用:
# cal(60, 90)

# 导入方式三
from math import fabs
from package.package2 import module03
# 使用:使用模块名.功能名调用
module03.cal(90, 10)

print(fabs(-90.8))