#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :3.自定义模块.py
# @Time      :2025/01/11 21:59:10
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
1.自定义模块:在实际开发中,Python提供的标准库模块不能满足开发需求,程序员需要一些个性化的模块,就可以进行自定义模块的实现.
! 注意事项
! 1.使用 __name__可以避免模块中测试代码的执行
! 2.使用__all__可以控制import *时,那些功能被导入,注意:import模块的方式不受__all__的限制
"""
# !出现了一个问题是当导入模块文件时也会执行测试代码
# !如何解决导入模块文件会执行测试代码的问题呢.
"""
如果我们并不希望导入模块时,去执行测试代码hi(),就可以使用__name__
当一个Python模块被导入时,__name__会被设为模块的名称
如果直接执行__name__会被设置为__main__
print(__name__)
如果当前文件的__name__的值为__name__才执行
if __name__ =='__main__'
    hi()
"""
"""
在test_module.py中,没有__all__时会被导入所有的功能
使用__all__ ==["ok"] 在其他文件使用from test_module import * 只会导入ok()
注意:import模块方式,不受__all__的限制
__all__=["ok"]
"""
"""
! 注意:这种import模块导入方式,不受__all__的限制
# import test1_module
# test1_module.hi()
# test1_module.ok()
"""
