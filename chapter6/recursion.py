#!/usr/bin/env python
def jiecheng (number):
    if number == 1:
        return 1
    else:
        return number * jiecheng(number-1)
print jiecheng(1)
print jiecheng(2)
print jiecheng(10)
print jiecheng(100)
