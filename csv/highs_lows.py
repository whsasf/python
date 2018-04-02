#!/usr/bin/env python3

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='sitka_weather_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,hights,lows=[],[],[]
    [ (hights.append(int((int(row[1])-32)/1.8)),lows.append(int((int(row[3])-32)/1.8)),dates.append(datetime.strptime(row[0], "%Y-%m-%d")))  for row in reader ]
    #[ dates.append(datetime.strptime(row[0], "%Y-%m-%d")) for row in reader ]
    #print(hights)

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,hights,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,hights,lows,facecolor='green',alpha=0.5)

plt.title('Daily temperatures ,July 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()