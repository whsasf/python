#!/usr/bin/env python
import copy

a =  {'user':'ram','num':[1,2,3]}
print id (a)

b = a
print id (b)

c = a.copy ()
print id (c)

d = deepcopy (a)
print id (d)

