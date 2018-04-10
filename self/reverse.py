#!/usr/bin/env python3

sentence="i love u china!"
List=sentence.split()
length=len(List)
for i in range (1,length+1):
    print(List.pop(),end=' ')
    
sentence2="i love u big!"
List2=sentence2.split()
List2.reverse()
length2=len(List2)
for i in range(0,length2):
    print (List2[i],end=' ')
