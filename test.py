#!/usr/bin/env python3
class Apple:
    def __init__(self,size):
        self.size=size
    def getsize(self):
        return self.size
bigapple=Apple(20)
print (bigapple.getsize())
smallapple=Apple(2)
print(smallapple.getsize())