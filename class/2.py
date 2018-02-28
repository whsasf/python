#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Restaurant:
	'''a test for class'''
	def __init__(self,restaurant_name,cuisine_type):
		self.name=restaurant_name
		self.type=cuisine_type
		self.number_served=10
	def set_number_served(self,newvalue):
		self.number_served=newvalue

	def describe_restaurant(self):
		print self.name.title()
		print self.type.title()
		print self.number_served

	def open_restaurant(self):
		print "the restaurant is open!"
	def increment_number_served(self,cerment):
		self.number_served+=cerment
		
restaurant1=Restaurant('好嫂子','open')
print "restaurant1 name and type are:" 
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.number_served=20
#restaurant1.describe_restaurant()
print restaurant1.number_served
restaurant1.set_number_served(30)
print restaurant1.number_served
restaurant1.increment_number_served(50)
print restaurant1.number_served