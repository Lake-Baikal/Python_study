#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename    :   2.面向对象-封装细节.py
@Time    :   2025/02/01 16:57:44
@Author  :   Baikal
@Motto     :追风赶月莫停留,平芜尽处是春山.
'''
# ! Python语言的动态特性,会出现伪私有属性的情况


class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共的方法, 对私有属性进行操作(根据实际的业务进行编写即可)

    def get__job(self):
        return self.__job


clerk = Clerk("alan", "Python工程师", 20000)
# ! 如果这样使用,因为Python语言的动态特性,会动态的创建属性__job,但是这个属性我们在类中定义的私有属性__job 并不是同一个变量,
# !我们在类中的定义的__job,私有属性完整的名字是 _Clerk__job

clerk.__job = 'Go工程师'
print(f"job={clerk.__job}")
print("ok")
# 获取真正的私有属性__job
print(f"{clerk.get__job()}")


# 练习
'''
!定义Account类
1.Account类要求具有属性,姓名(长度2~4位),余额(必须>20),密码(必须是六位),如果不满足,则给出提示信息,并给默认值(程序员直接定)
2.通过set_xxx的方法会Account的属性赋值
3.编写方法query_info()接收姓名和密码,如果姓名和密码正确,则返回该账号的信息
'''

'''
思路分析
1.类名:Account
2.私有属性:姓名(长度2~4位),余额(必须>20),密码(必须是六位)
3.构造器:无 默认为无参构造器
4.方法:set_xxx(self,属性名)进行赋值,并且对各个接收到的数据进行校验
5.方法:query_info(self,name,pwd)而且需要验证,才返回响应信息
'''


class Account:
    __name = None
    __balance = None
    __pwd = None

    def set_name(self, name):
        # 姓名(长度2~4位)
        if 2 <= len(name) <= 4:
            self.__name = name
        else:
            print("名字不在2~4位之间,请修改")

    def set_balance(self, balance):
        # 余额(必须 > 20)
        if balance > 20:
            self.__balance = balance
        else:
            print("余额(必须 > 20)")

    def set_pwd(self, pwd):
        # 密码(必须是六位)
        if len(pwd) == 6:
            self.__pwd = pwd
        else:
            print("密码(必须是六位)")

    def query_info(self, name, pwd):
        if name == self.__name and pwd == self.__pwd:
            return f"账号信息{self.__name} {self.__balance}"
        else:
            return "请输入正确的名字和信息"


# 验证
account = Account()
account.set_name("Alan")
account.set_pwd("000000")
account.set_balance(1000)
print(account.query_info("Alan", "000000"))
