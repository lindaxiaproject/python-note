# coding=utf-8
import types


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

@staticmethod
def staticfunc():
    print("---static method---")
Person.staticfunc = staticfunc
Person.staticfunc()

@classmethod
def clsfunc(cls):
    print('---cls method---')
Person.clsfunc = clsfunc
Person.clsfunc()