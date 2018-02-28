#!/usr/bin/env python3

filename='alice_in_wonderland.txt'
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
#        print (contents)
except FileNotFoundError:
    msg="Sorry,file "+ filename + " does not exist!"
    print (msg)
else:
    words=contents.split()
    print (words)
    num_words=len(words)
    print("the file " + filename + "has about " + str(num_words) + " words!")