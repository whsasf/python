#!/usr/bin/env python3

from modules.sendmails import send_mail
from modules.remote_operations import remote_operation

#reate summary file and debug files:
#sumfile = 'sumary.log'
#dbgfile = 'debug.log'
#with open(sumfile, 'a') as file_object:
#    file_object.write(attdata)

mtahost = '10.49.58.239'
mtaport = 20025
sshtarget = '10.49.58.239'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@openwave.com>'

#define all the variables needed
testcases = {
't1':{'casename':'MX-11540','receivers':['u1 <u1+INBOX@openwave.com>','u3 <u3+INBOX>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't2':{'casename':'MX-11541','receivers':['u1 <u1+Trash@openwave.com>','u3 <u3+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't3':{'casename':'MX-11542','receivers':['u1 <u1+Trash/folder@openwave.com>','u3 <u3+Trash/folder>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't4':{'casename':'MX-11543','receivers':['u1 <u1+Trash/folder/folder1/folder2/folder3@openwave.com>','u3 <u3+Trash/folder/folder1/folder2/folder3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't5':{'casename':'MX-11544','receivers':['u1 <INBOX--u1@openwave.com>','u3 <INBOX--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't6':{'casename':'MX-11545','receivers':['u1 <Trash--u1@openwave.com>','u3 <Trash--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't7':{'casename':'MX-11546','receivers':['u1 <Trash/folder--u1@openwave.com>','u3 <Trash/folder--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't8':{'casename':'MX-11547','receivers':['u1 <Trash/folder/folder1/folder2/folder3--u1@openwave.com>','u3 <Trash/folder/folder1/folder2/folder3--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't9':{'casename':'MX-11548','receivers':['u1 <u1+test@openwave.com>','u3 <u3+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't10':{'casename':'MX-11549','receivers':['u1 <u1+test/folder@openwave.com>','u3 <u3+test/folder>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't11':{'casename':'MX-11550','receivers':['u1 <u1+test/folder/folder1/folder2/folder3@openwave.com>','u3 <u3+test/folder/folder1/folder2/folder3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't12':{'casename':'MX-11551','receivers':['u1 <test--u1@openwave.com>','u3 <test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't13':{'casename':'MX-11552','receivers':['u1 <test/folder--u1@openwave.com>','u3 <test/folder--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't14':{'casename':'MX-11553','receivers':['u1 <test/folder/folder1/folder2/folder3--u1@openwave.com>','u3 <test/folder/folder1/folder2/folder3--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't15':{'casename':'MX-11554','receivers':['<u1+Trash@openwave.com>','<u3+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't16':{'casename':'MX-11555','receivers':['<u1+test@openwave.com>','<u3+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't17':{'casename':'MX-11556','receivers':['u1 <u1+++test@openwave.com>','u3 <u3+++test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't18':{'casename':'MX-11557','receivers':['u1 <u1+++Trash@openwave.com>','u3 <u3+++Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't19':{'casename':'MX-11558','receivers':['u1 <u1+--Trash@openwave.com>','u3 <u3+--Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't20':{'casename':'MX-11559','receivers':['u1 <u1+--test@openwave.com>','u3 <u3+--test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't21':{'casename':'MX-11560','receivers':['u1 <u1+!test@openwave.com>','u3 <u3+!test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't22':{'casename':'MX-11561','receivers':['u1 <u1+test\'@openwave.com>','u3 <u3+test\'>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't23':{'casename':'MX-11562','receivers':['u1 <"u1+te st@openwave.com">','u3 <"u3+te st">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't24':{'casename':'MX-11563','receivers':[r'u1 <"u1+te\"st@openwave.com">',r'u3 <"u3+te\"st">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't25':{'casename':'MX-11564','receivers':['u1 <Trash--u1@openwave.com>','u3 <Trash--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't26':{'casename':'MX-11565','receivers':['u1 <test--u1@openwave.com>','u3 <test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't27':{'casename':'MX-11566','receivers':['u1 <test----u1@openwave.com>','u3 <test----u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't28':{'casename':'MX-11567','receivers':['u1 <Trash----u1@openwave.com>','u3 <Trash----u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't29':{'casename':'MX-11568','receivers':['u1 <!test--u1@openwave.com>','u3 <!test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't30':{'casename':'MX-11569','receivers':['u1 <test\'---u1@openwave.com>','u3 <test\'---u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't31':{'casename':'MX-11570','receivers':[r'u1 <"te st---u1@openwave.com">',r'u3 <"te st---u3">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't32':{'casename':'MX-11571','receivers':[r'u1 <"te\"st---u1@openwave.com">',r'u3 <"te\"st---u3">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't33':{'casename':'MX-11572','receivers':['u1 <u1--+test@openwave.com>','u3 <u3--+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't34':{'casename':'MX-11573','receivers':['u1 <u1--+Trash@openwave.com>','u3 <u3--+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't35':{'casename':'MX-11574','receivers':['u1 <test--!u1@openwave.com>','u3 <test--!u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't36':{'casename':'MX-11575','receivers':['u1 <Trash--!u1@openwave.com>','u3 <Trash--!u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't37':{'casename':'MX-11576','receivers':['u1--- <u1++test\'@openwave.com>','u3--- <u3++test\'>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't38':{'casename':'MX-11577','receivers':['u1+++ <test\'---u1@openwave.com>','u3+++ <test\'---u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't39':{'casename':'MX-11578','receivers':['u1 <u1@openwave.com','u3+ <u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
            }
#set  subAddressAllowedIPs=[]
print ("---->Set subAddressAllowedIPs=[] ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=\"\'','10.49.58.239','root','letmein',0)

# restart mta server
print ("---->Restarting mta server ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.239','root','letmein',1,'imservctrl: done',1)

print ('---->Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 if exists
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)
    
print ('---->Create u1,u2,u3 ...                  ',end='') #creaet account u1,u2,u3
remote_operation('su - imail -c \
  "account-create u1@openwave.com p default;account-create u2@openwave.com p default;account-create u3@openwave.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',3)

print ('---->Clear mta.log firsltly ...           ',end='') #clear mta.log firstly
remote_operation('su - imail -c "> log/mta.log"','10.49.58.239','root','letmein',0)

#set quote for sender and recepients
#ssdsdsd

print ('###############Beginning testing...######################')
for tck ,tcv in sorted(testcases.items(),key=lambda testcases:testcases[0]):
    print ('---->run imrecalcmboxstats for u1 ...           ',end='')
    remote_operation("su - imail -c \"msgid=\$(imboxstats u1@openwave.com|grep Statistics|awk '{print \$5}');echo \$msgid >xx.txt;imrecalcmboxstats mx1 repair \$msgid ''\"",'10.49.58.239','root','letmein',0)
    print ('---->run imrecalcmboxstats for u3 ...           ',end='')
    remote_operation("su - imail -c \"msgid=\$(imboxstats u3@openwave.com|grep Statistics|awk '{print \$5}');echo \$msgid >xx.txt;imrecalcmboxstats mx1 repair \$msgid ''\"",'10.49.58.239','root','letmein',0)

    print ('\033[1;45mRunning testing testcase: '+tck+'---------->'+tcv['casename']+'\033[0m')
    sendnum = len(tcv['receivers'])
    #print ('recivers numbers are:'+str(sendnum))
    print ('Sending message in proper formats ...',end='')
    send_mail(mtahost,mtaport,sender,tcv['receivers'])
    print ('Checking mta.log ...                 ',end='')
    remote_operation(tcv['commands'],sshtarget,sshaccount,sshpasswd,1,tcv['check_flags'],sendnum)
print ('###############Endding testing...######################') 

print ('---->Delete u1,u2,u3 ...',end='') #delete u1,u2,u3 at last
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)