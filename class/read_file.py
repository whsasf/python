#!/usr/bin/env python3

#with open('../pi.txt') as file_object:
#    contents=file_object.read()
#    print(contents.rstrip())
    
with open('../pi.txt') as file_object:
    for line in file_object:
        print ('haha')
        print(line.rstrip())