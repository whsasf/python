#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class User:
	def __init__(self,first_name,last_name):
		self.first_name=first_name
		self.last_name=last_name
		self.login_attempts=0
	def describe_user(self):
		user_info="firstname:"+self.first_name+"\n"+"last_name:"+self.last_name+"\n"+"login_attempts:"+str(self.login_attempts)
		print (user_info)
	def greet_user(self):
		great_info="hi "+self.first_name+" "+self.last_name+",welcome!"
		print (great_info)
	def increment_login_attempts(self):
		self.login_attempts+=1
	def reset_login_attempts(self):
		self.login_attempts=0

ram=User('ram','wang')
ram.describe_user()
ram.greet_user()
ram.increment_login_attempts()
ram.describe_user()
ram.reset_login_attempts()
ram.describe_user()