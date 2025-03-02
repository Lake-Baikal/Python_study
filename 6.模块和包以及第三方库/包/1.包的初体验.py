#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.包的初体验.py
# @Time      :2025/01/12 14:11:46
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
一个实际的项目中,可能需要很多模块,当模块文件越来越多,如果我们将所有的模块文件都放入同一个文件夹中,就会带来很多问题,不利于管理和调用.
!从结构上看,包就是一个文件夹,在该文件夹下包含一个__init__.py文件,该文件夹可以用于包含多个模块文件,从逻辑上看,包可以视为模块的集合
!导入包和使用包的基本语法
导入:import 包名.模块
from 包名 import 模块
这种方法导入在使用时,模块.包名 ,不用带包名
使用:包名.模块.功能
"""
"""
!包的注意事项和使用细节
!1.导入包和使用包的基本语法
导入:import 包名.模块
from 包名 import 模块
这种方法导入在使用时,模块.包名 ,不用带包名  直接使用模块名.功能名
使用:包名.模块.功能
!2.导入包的模块的指定函数、类、变量
from 包名.模块 import 函数、类、变量
上面是导入包的模块的指定函数、类、 变量
在使用时,直接调用功能即可
form 包名.模块 import * 表示导入包的模块的所有功能

!3.__init__.py通过__all__控制允许导入的模块
在__init__.py中增加__all__=[允许导入的模块列表]
针对from 包 import * 方式生效,对import xx方式不生效

__all__=[允许导入的模块列表]不能限制下面的导入形式
import package.module01
import package.module02

package.module01.hi()
package.module02.ok()

! 4.包可以有多个层级
包下面可以在创建包
在使用时,通过. 来确定层级关系
导入方式一  看起来麻烦,但是使用起来好理解,层次分明
import package.package2.module03
使用:
package.package2.module03.cal(10,20)
导入方式二
from package.package2.module03 import cal
使用: 直接调用即可
cal(60,90)
导入方式三
from package.package2 import module03
module03.cal(90,10)

4.快捷键shift + space(空格键)快速修复
"""
