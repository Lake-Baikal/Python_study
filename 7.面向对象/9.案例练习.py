#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   9.案例练习.py
@Time    :   2025/01/29 16:23:25
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# 1.编写类A01,定义方法max,实现求某个float列表list=[1.1,2.9,-1.9,67.9]的最大值,并返回
'''
思路分析
1.类名A01
2.方法max(self,lst),功能返回列表的最大值
'''


class A01:
    def max(self, lst):
        return max(lst)


# 完成测试
a = A01()
print("最大值=", a.max([1.1, 2.9, -1.9, 67.9]))


# 2.编写Book类,定义方法update_price,实现更改某本书的价格,具体:如果价格>150,则更改为150,如果价格>100,则更改为100,否则不变.
'''
思路分析
1.类名Book
2.属性:name,price
3.构造器:__init__(self,name,price)
4.方法:update_price 完成功能:如果价格>150,则更改为150,如果价格>100,则更改为100,否则不变.
'''


class Book:
    # name = None
    # price: None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def updete_prtice(self):
        # 如果价格>150,则更改为150,如果价格>100,则更改为100,否则不变.
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100
        else:
            pass

    # 增加一个输出书籍信息的方法
    def info(self):
        print(f"书的信息:{self.name} {self.price}")


# 测试
book = Book("天龙八部", 50)
book.info()
book.updete_prtice()
book.info()

# 3.定义一个圆类Circle,定义属性:半径,提供显示圆周长的方法,提供显示圆面积的方法.
'''
思路分析
1.类名Circle
2.属性:radius
3.构造器:__init__(self,radius)
4.方法:len(self):显示圆周长 area:显示圆面积
'''

# 导入math模块
# import math


# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def len(self):
#         len = 2 * math.pi * self.radius
#         print("圆周长:", round(len, 2))

#     def area(self):
#         area = math.pi * self.radius * self.radius
#         print("圆面积", round(area, 2))


# # 测试
# circle = Circle(6)
# circle.len()
# circle.area()

# 4.编程创建一个Cal计算类,在其中定义2个成员变量表示两个操作数,定义四个方法实现求和,差,乘,商(要求除数为0的话,要提示)并创建对象,分别测试
'''
思路分析
1.类名Cal
2.属性:num1,num2
3.构造器:__init__(self,num1,num2)
4.方法:定义四个方法实现求和 def sum(),差def minus(),乘def mul(),商def div()
5.(要求除数为0的话,要提示)并创建对象,分别测试
'''


class Cal:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            print("num2不能为0")
            return None
        else:
            return self.num1 / self.num2


# 测试
cal = Cal(2, 0)
print("和=", cal.sum())
print("差=", cal.minus())
print("乘=", cal.minus())
print("除=", cal.div())


# 5.定义Music类,里面有音乐名name,音乐时长times,并有播放play功能,和方法本身属性信息的方法get_info
'''
思路分析
1.类名Music
2.属性:name,times
3.构造器:__init__(self,name,times)
4.方法:play(self),get_info(self)
'''


class Music:
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print(f"音乐名{self.name} 正在播放中,时长是多少{self.times}")

    def get_info(self):
        # return self.name, self.times
        return f"音乐的名字name:{self.name} 音乐的时长是times:{self.times}"


# 测试
music = Music("我心永恒", 300)
music.play()
print(music.get_info())


# 6.写出以下代码的运行结果
class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i=", self.i)
        print("j", j)


d1 = Demo()
d2 = d1
d2.m()
print(d1.i)
print(d2.i)

# 7.猜拳
'''
1.有一个了叫Tom设计他的成员变量,成员方法,可以进行电脑猜拳,电脑随机生成随机数0,1,2
2.0表示石头,1表示剪刀,2表示布
3.并且可以显示Tom的输赢次数(清单)
'''


'''
创建 Tom 类：

成员变量：
wins: 用于记录 Tom 的胜利次数，初始值为 0。
losses: 用于记录 Tom 的失败次数，初始值为 0。
成员方法：
__init__(self): 构造函数，初始化 wins 和 losses 为 0。
play(self): 游戏的主要逻辑。
show_record(self): 显示 Tom 的输赢记录。
实现 play 方法：

choices 列表：存储有效的用户输入（"0"、"1"、"2"）。
使用 while True 循环，让游戏可以持续进行，直到玩家选择退出。
获取玩家的输入，并存储在字符串变量 player_choice_str 中。
检查 player_choice_str 是否在 choices 列表中。如果在，则将其转换为整数 player_choice。否则，退出循环。
生成电脑的随机选择。
根据石头剪刀布的规则判断胜负：
如果玩家和电脑的选择相同，则为平局。
如果玩家赢了，则 wins 加 1。
否则，玩家输了，losses 加 1。
输出游戏结果。
实现 show_record 方法：

打印 Tom 的胜利次数和失败次数。
主程序：

创建 Tom 类的实例 tom。
调用 tom.play() 开始游戏。
调用 tom.show_record() 显示游戏记录。
'''
import random


class Tom:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def play(self):
        choices = [0, 1, 2]
        while True:
            play_choices = int(input("请选择:0-石头,1-剪刀,2,布"))
            if play_choices not in choices:
                break
            computer_choice = random.randint(0, 2)
            print(f"电脑选择了:{computer_choice}")
            if play_choices == computer_choice:
                print("平局")
            elif (play_choices - computer_choice) % 3 == 1:
                print("你赢了")
                self.wins += 1
            else:
                print("你输了")
                self.losses += 1

    def show_record(self):
        print(f"Tom 的战绩: WINS:{self.wins},LOSSES:{self.losses}")


tom = Tom()
tom.play()
tom.show_record()
