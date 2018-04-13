#!/usr/bin/env python3

#first install tsv modul if not existed using :"pip install tsv" or "pip3 install tsv" 
import csv
import requests

#part1 get ids
filename = 'AIDA-YAGO2-annotations.tsv'
with open(filename,encoding='utf-8') as f:
    reader = csv.reader(f,delimiter='\t')
    IDs = []
    for row in reader:
        element=str(row[3])
        if element.strip() != '':
            #print (element)
            IDs.append(element)

#part2 get APIs and parse json
sumfile = 'summary.log'
def geturl (id):
    url = 'https://en.wikipedia.org/w/api.php?action=query&pageids='+id+'&prop=categories&clshow=%21hidden&format=json'
    r = requests.get(url)
    response_dict=r.json()
    try:
        List = response_dict['query']['pages'][id]['categories'] 
    except KeyError:
        print ("do not have categories!")
        return 1
    with open(sumfile,'a',encoding='utf-8') as ff:
        ff.write(id+'\t')
    tmp=[]
    for dict in List:
        title = dict['title'][9:]
        tmp.append(title)
    categries='|'.join(tmp)
    with open(sumfile,'a') as ff:
        ff.write(categries+'\n')

with open(sumfile,'w',encoding='utf-8') as ff:
    ff.write('id'+'\t\t'+'categories'+'\n\n')
for id in IDs:
    print ('extracting pageid: '+id+' ...')
    geturl (id)
print ('Done!')
