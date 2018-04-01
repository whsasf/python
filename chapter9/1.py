#!/usr/bin/env python3
from manyclasses import *

restaurant1 = Resaurant('haosaozi','hot')
print (restaurant1.restaurant_name)
print (restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant() 

restaurant2=Resaurantt('xiabuxiabu','hotpot')
print ("there are " + str(restaurant2.number_served) + " people eatting here!")
restaurant2.number_served = 300
print ("there are " + str(restaurant2.number_served) + " people eatting here!")
restaurant2.set_number_served(500)
print ("there are " + str(restaurant2.number_served) + " people eatting here!")
restaurant2.increment_number_served(40)
print ("there are " + str(restaurant2.number_served) + " people eatting here!")