#!/usr/bin/env python3
import pygal
from modules.dies import Die

die1=Die()
die2=Die(10)
results=[]

[results.append(die1.roll()+die2.roll()) for roll_num in range(5000)]
#print (results)

frequencies=[]
max_result= die1.num_sides + die2.num_sides
[frequencies.append(results.count(value)) for value in range(2,max_result+1)]
#print (frequencies)

hist=pygal.Bar()
hist.title='Resultss of rolling one D6 and D10 5000 times'
hist.x_labels=[x for x in range(2,max_result+1)]
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6+D10',frequencies)
hist.render_to_file('dies_visual.svg')