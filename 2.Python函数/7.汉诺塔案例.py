#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :7.汉诺塔案例.py
# @Time      :2024/04/14 12:04:12
# @Author    :Baikal
# @Motto     :我亦无他,唯手熟尔
"""
?z汉诺塔问题是一个经典的问题。汉诺塔(Hanoi Tower),又称河内塔,源于印度一个古老传说.大梵天创造世界的时候做了三根金刚石柱子
?在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘.大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定,任何时候,在小圆盘上都不能放大圆盘,且在三根柱子之间一次只能移动一个圆盘.问应该如何操作？
"""


def hanoi_tower(num, a, b, c):
    """_summary_
  输出指定的num个盘中移动的顺序
  Args:
      num (_type_): 指定盘子数
      a (_type_): 表示A柱子
      b (_type_): 表示B柱子
      c (_type_): 表示C柱子
  """
    # 如果只有一个盘
    if num == 1:
        print("第1个盘从:", a, "->", c)
    else:
        # 有多个盘,我们认为只有两个,上面所有的盘和最下面的盘
        # 移动上面所有的盘到B柱子,这个过程会借助到我们C柱子
        hanoi_tower(num - 1, a, c, b)
        # 移动最下面的盘
        print(f"第{num}个从:{a}->{c}")
        # 把上面所有的盘从B柱子移动到C柱子,这个过程会用到A柱子
        hanoi_tower(num - 1, b, a, c)


#
hanoi_tower(8, "A", "B", "C")
