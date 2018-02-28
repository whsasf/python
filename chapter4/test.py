#!/usr/bin/env python

print "hello ,%s ,%s enough for ya?" % ('world','hot')
print "price of eggs: %d" % 42
d=dict (name='ram',age=30)
print d
dic={'ram':30,'jim':34,'pitter':45}
print dic
print len(dic)
print dic['ram']
dic['ram']=50
print dic
del dic['jim']
print dic
flag='ram' in dic
print flag