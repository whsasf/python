#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Restaurant:
	'''a test for class'''
	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.type=cuisine_type

	def describe_restaurant(self):
		print self.name.title()
		print self.type.title()

	def open_restaurant(self):
		print "the restaurant is open!"
		
restaurant1=Restaurant('好嫂子','open')
print "restaurant1 name and type are:" 
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2=Restaurant('煎饼','closed')
print "restaurant2 name and type are:"
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3=Restaurant('过钱米线','painting')
print "restaurant3 name and type are:"
restaurant3.describe_restaurant()
restaurant3.open_restaurant()


