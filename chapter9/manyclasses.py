class Resaurant():
    """this is a class named Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print ("restaurant_name=" + self.restaurant_name)
        print ("cuisine_type=" + self.cuisine_type)
    def open_restaurant(self):
        print ("The restaurant is opening!")
        
        
        
class Resaurantt():
    """this is a class named Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print ("restaurant_name=" + self.restaurant_name)
        print ("cuisine_type=" + self.cuisine_type)
    def open_restaurant(self):
        print ("The restaurant is opening!")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self,number2):
        self.number_served += number2

     