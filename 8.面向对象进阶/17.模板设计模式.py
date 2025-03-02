#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   17.模板设计模式.py
@Time    :   2025/02/27 22:04:45
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
from abc import ABC, abstractmethod
import time

# 设计模式
# 1.设计模式是在大量的实践中总结和理论化之后的代码结构,编程风格,以及解决问题的思考方式
# 2.设计模式就像是经典的棋谱,不同的棋局,免去我们自己再思考和摸索

"""
抽象类体现的就是一种模板设计模式,抽象类作为多个子类的通用模板,子类在抽象类的基础上进行扩展,改造,但是子类总体上会保留抽象类的行为方式
! 模板设计模式能解决的问题
1.当功能内部一部分实现是确定,一部分实现是不确定.这时就可以把不确定的部分暴露出去,让子类去实现
2.编写一个抽象父类,父类提供了多个子类的通用方法,并把一个或多个方法留个其子类实现,就是一种模板模式
"""

# ? 案例
"""
1.有多个类,完成不同的任务job
2.要求统计得到各自完成任务的时间'
3.请编程实现
"""


# class AA:
#     def job(self):
#         # 得到开始的时间,秒数
#         start = time.time()
#         num = 0
#         for i in range(1, 800001):
#             num += i
#         end = time.time()
#         print("计算任务 执行时间", (end - start))


# class BB:
#     def job(self):
#         start = time.time()
#         num = 1
#         for i in range(1, 9000):
#             num -= i
#         end = time.time()
#         print("计算任务 执行时间", (end - start))


# # 测试
# if __name__ == '__main__':
#     aa = AA()
#     aa.job()
#     bb = BB()
#     bb.job()


# !优化以上代码
"""
# * 使用模板设计模式
设计一个抽象基类(Template),能完成如下功能
1.编写方法cal_time(),可以计算某段代码的耗时时间
2.编写抽象方法job()
3.编写一个子类,继承抽象类Template,并实现job方法
4.完成测试
"""


class Template(ABC):
    @abstractmethod
    def job(self):
        pass

    # 统计任务执行的时间
    def cal_time(self):
        # 得到开始的时间,秒数
        start = time.time() * 1000
        self.job()
        end = time.time() * 1000
        print("计算任务 执行时间(毫秒)", (end - start))


class AA(Template):

    def job(self):
        num = 0
        for i in range(1, 800001):
            num += i


class BB(Template):
    def job(self):
        num = 1
        for i in range(1, 9000):
            num -= i


# 测试
if __name__ == '__main__':
    aa = AA()
    aa.cal_time()
    bb = BB()
    bb.cal_time()

