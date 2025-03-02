#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test1.module.py
# @Time      :2025/01/11 22:07:21
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.

# !表示如果其他文件使用的是from tets1_module import * 导入,则只能导入ok这个函数
__all__ = ['ok']


def hi():
    print('baikal hi')


def ok():
    print('baikal ok')


# 有时我们在模块中,会写一下测试代码
# hi()
# print("test_module", __name__)

if __name__ == "__main__":
    hi()
print("test_module", __name__)
