#!/usr/bin/env python3

def ite():
    print('hello')
    yield 'test1'
    print('world')
    yield 'test2'
    yield 'test3'
    yield 'test4'

gen = ite()   #
print(type(gen))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())



