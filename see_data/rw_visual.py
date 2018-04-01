#!/usr/bin/env python3

import matplotlib.pyplot as plt

from modules.random_walk import RandomWalk

while True:

    rw=RandomWalk(500)
    rw.fill_walk()
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_value,rw.y_value,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=10)
    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c='red',edgecolor='none',s=100)
    plt.show()
    keep_running = input ("Make another walk? (y/n):")
    if keep_running == 'n':
        break