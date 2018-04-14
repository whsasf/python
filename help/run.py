#!/usr/bin/env python3

import csv
import requests

#part1 get ids
filename = 'AIDA-YAGO2-annotations.tsv'
with open(filename) as f:
    reader = csv.reader(f,delimiter='\t')
    IDs = []
    for row in reader:
        element=str(row[3])
        if element.strip() != '':
            #print (element)
            IDs.append(element)
IDs2 = []
[IDs2.append(i) for i in IDs if not i in IDs2]   #delete deplucate

#part2 get APIs and parse json
sumfile = 'summary.log'
def geturl (id):
    url = 'https://en.wikipedia.org/w/api.php?action=query&pageids='+id+'&prop=categories&clshow=%21hidden&format=json'
    r = requests.get(url,verify=False)
    response_dict=r.json()
    try:
        List = response_dict['query']['pages'][id]['categories'] 
    except KeyError:
        print ("do not have categories!")
        return 1
    with open(sumfile,'a') as ff:
        ff.write(id+'\t')
        #ff.write("%-10s"%(id)+'\t')
    tmp=[]
    for dict in List:
        title = dict['title'][9:]
        tmp.append(title)
    categries='|'.join(tmp)
    with open(sumfile,'a') as ff:
        ff.write(categries+'\n')

with open(sumfile,'w') as ff:
    ff.write('id'+'\t\t'+'categories'+'\n\n')
for id in IDs2:
    print ('extracting pageid: '+id+' ...')
    geturl (id)
print ('Done!')
