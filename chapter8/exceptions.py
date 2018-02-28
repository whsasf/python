#!/usr/bin/env python

try:
	x=input("Enter the first number:")
	y=input("Enter the second number:")
	print x/y
except ZeroDivisionError:
	print "can no tbe"