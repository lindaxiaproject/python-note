# coding=utf-8
from typing import TypeAlias

newname : TypeAlias = str
def newFunc(param:str) -> newname:
    return param + param


print(newFunc('全干程序员'))
