#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :第三方库.py
# @Time      :2025/01/12 17:05:47
# @Author    :Baikal
# @Motto     :追风赶月莫停留,平芜尽处是春山.
"""
第三方库/包:就是非python官方提供的库,python语言有很多第三方库,覆盖几乎所有的领域,比如网络爬虫、自动化、数据可视化分析、web开发、机器学习等
使用第三方库,可以大大提高开发效率

!pip介绍:pip是python的包管理器,是一个工具,允许你安装和管理第三方库和依赖
!pip的使用方式
1.进入命令控制台
2.语法:pip install 库名/包名
3.注意:pip是通过网络安装的,需要网络是连通的
4.pip除了安装还有其他用法,可以根据需求选择使用
5.pip的基本语法: pip <command> [options]
command:
install
download
uninstall
freeze
inspect
list
show
check
config
search
"""
# ! 通过pip安装第三方库requests
# ! pip install requests
# ! 安装完成后使用 命令: pip list查看是否安装成功
# ! 卸载第三方库requests 命令: pip uninstall requests

# ?指定pip源
# 1.默认的pip源是http://pypi.python.org/simple  因为在国外,所以下载速度比较慢
# 2.国内知名是几个源:
# 豆瓣 https://pypi.douban.com/simple
# 清华大学源 https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云源 https://mirrors.aliyun.com/pypi/simple
# 中国科学技术大学源 https://pypi.mirrors.ustc.edu.cn/simple
# 腾讯云源 https://mirrors.cloud.tencent.com/pypi/simple
# 3.指定源,安装 第三方库
# !语法: pip install -i 指定源 库名/包名
# pip install https://mirrors.aliyun.com/pypi/simple requests
