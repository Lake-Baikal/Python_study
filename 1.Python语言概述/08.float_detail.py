#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :08.float_detail.py
# @Time      :2024/03/17 09:12:02
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔

# !Python的浮点数类型可以表示一个小数,比如123.4,7.8,-0.12
import sys
from decimal import Decimal

n1 = 4.5
n2 = -3.6
print("n1=", n1)
print("n2=", n2)

# 浮点数类型的表示形式
# 十进制数形式:如5.12,0.512(必须加小数点)或者.512但是注意必须加小数点

n3 = 5.12
n4 = 0.512
print("n4=", n4)
# 科学计数法:5.12e2或者5.12e+2,5.12E-2
n5 = 5.12e2  # 表示5.12乘以10的二次方
n6 = 5.12e-2  # 表示5.12除以10的二次方
print("n5=", n5)
print("n6=", n6)
# 浮点数有大小限制，边界值
# max = 1.7976931348623157e+308 表示最大正有限浮点数
# min = 2.2250738585072014e-308 表示最小规范化浮点数
sys.float_info
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15,
#                mant_dig=53,
#                epsilon=2.220446049250313e-16,
#                radix=2,
#                rounds=1)
# ! 浮点数类型计算后，存在精度损失，可以使用Decimal类进行精确计算
# !如果使用Decimal类，需要导入Decimal类

# b = 8.1 / 3  # 应该是2.7，可是执行结果是2.6999999999999997
# b = 8.1 / 3  # 2.6999999999999997 存在精度损失问题
b = Decimal("8.1") / Decimal("3")
print("b=", b)  # 返回准确的2.7
