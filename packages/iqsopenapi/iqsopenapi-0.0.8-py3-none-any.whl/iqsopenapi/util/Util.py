# -*- coding: utf-8 -*-
import time
import sys
import os

def ExecutedTime(func):
    start = time.time()
    result = func()
    end = time.time()
    escape = end - start
    return escape, result

def Minimum(values, func):
    value = None
    last = None
    for x in values:
        result = func(x)
        if not last or last > result:
            value = x
            last = result
    return value
            
def GetRootPath():
    """路径处理工具类"""
    # 判断调试模式
    debug_vars = dict((a, b) for a, b in os.environ.items() if a.find('IPYTHONENABLE') >= 0)
    # 根据不同场景获取根目录
    rootPath = ''
    if len(debug_vars) > 0:
        """当前为debug运行时"""
        rootPath = sys.path[2]
    elif getattr(sys, 'frozen', False):
        """当前为exe运行时"""
        rootPath = os.getcwd()
    else:
        """正常执行"""
        rootPath = sys.path[1]
    # 替换斜杠
    return rootPath.replace("\\", "/")