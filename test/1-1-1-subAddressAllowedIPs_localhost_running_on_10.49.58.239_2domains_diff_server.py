#!/usr/bin/env python3

from modules.sendmails import send_mail
from modules.remote_operations import remote_operation
import time
#reate summary file and debug files:
#sumfile = 'sumary.log'
#dbgfile = 'debug.log'
#with open(sumfile, 'a') as file_object:
#    file_object.write(attdata)

mtahost = '127.0.0.1'
mtaport = 20025
sshtarget = '10.49.58.130'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@whsasf.com>'

#define all the variables needed
testcases = {
't1':{'casename':'MX-11003','receivers':['u1 <u1+INBOX@bigworld.com>','u3 <u3+INBOX@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to INBOX folder'},
't2':{'casename':'MX-10892','receivers':['u1 <u1+Trash@bigworld.com>','u3 <u3+Trash@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't3':{'casename':'MX-10893','receivers':['u1 <u1+Trash/folder@bigworld.com>','u3 <u3+Trash/folder@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder folder'},
't4':{'casename':'MX-10894','receivers':['u1 <u1+Trash/folder/folder1/folder2/folder3@bigworld.com>','u3 <u3+Trash/folder/folder1/folder2/folder3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder/folder1/folder2/folder3 folder'},
't5':{'casename':'MX-11010','receivers':['u1 <INBOX--u1@bigworld.com>','u3 <INBOX--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to INBOX folder'},
't6':{'casename':'MX-10895','receivers':['u1 <Trash--u1@bigworld.com>','u3 <Trash--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't7':{'casename':'MX-10896','receivers':['u1 <Trash/folder--u1@bigworld.com>','u3 <Trash/folder--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder folder'},
't8':{'casename':'MX-10897','receivers':['u1 <Trash/folder/folder1/folder2/folder3--u1@bigworld.com>','u3 <Trash/folder/folder1/folder2/folder3--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder/folder1/folder2/folder3 folder'},
't9':{'casename':'MX-10898','receivers':['u1 <u1+test@bigworld.com>','u3 <u3+test@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't10':{'casename':'MX-10899','receivers':['u1 <u1+test/folder@bigworld.com>','u3 <u3+test/folder@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder folder'},
't11':{'casename':'MX-10900','receivers':['u1 <u1+test/folder/folder1/folder2/folder3@bigworld.com>','u3 <u3+test/folder/folder1/folder2/folder3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder/folder1/folder2/folder3 folder'},
't12':{'casename':'MX-10901','receivers':['u1 <test--u1@bigworld.com>','u3 <test--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't13':{'casename':'MX-10902','receivers':['u1 <test/folder--u1@bigworld.com>','u3 <test/folder--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder folder'},
't14':{'casename':'MX-10903','receivers':['u1 <test/folder/folder1/folder2/folder3--u1@bigworld.com>','u3 <test/folder/folder1/folder2/folder3--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder/folder1/folder2/folder3 folder'},
't15':{'casename':'MX-11212','receivers':['<u1+Trash@bigworld.com>','<u3+Trash@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't16':{'casename':'MX-11213','receivers':['<u1+test@bigworld.com>','<u3+test@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't17':{'casename':'MX-11214','receivers':['u1 <u1+++test@bigworld.com>','u3 <u3+++test@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to ++test folder'},
't18':{'casename':'MX-11215','receivers':['u1 <u1+++Trash@bigworld.com>','u3 <u3+++Trash@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to ++Trash folder'},
't19':{'casename':'MX-11216','receivers':['u1 <u1+--Trash@bigworld.com>','u3 <u3+--Trash@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to --Trash folder'},
't20':{'casename':'MX-11217','receivers':['u1 <u1+--test@bigworld.com>','u3 <u3+--test@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to --test folder'},
't21':{'casename':'MX-11218','receivers':['u1 <u1+!test@bigworld.com>','u3 <u3+!test@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !test folder'},
't22':{'casename':'MX-11219','receivers':['u1 <u1+test\'@bigworld.com>','u3 <u3+test\'@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to test' folder"},
't23':{'casename':'MX-11220','receivers':['u1 <"u1+te st@bigworld.com">','u3 <"u3+te st@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to te st folder'},
't24':{'casename':'MX-11221','receivers':[r'u1 <"u1+te\"st@bigworld.com">',r'u3 <"u3+te\"st@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to te"st folder'},
't25':{'casename':'MX-11222','receivers':['u1 <Trash--u1@bigworld.com>','u3 <Trash--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't26':{'casename':'MX-11223','receivers':['u1 <test--u1@bigworld.com>','u3 <test--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't27':{'casename':'MX-11224','receivers':['u1 <test----u1@bigworld.com>','u3 <test----u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't28':{'casename':'MX-11225','receivers':['u1 <Trash----u1@bigworld.com>','u3 <Trash----u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't29':{'casename':'MX-11226','receivers':['u1 <!test--u1@bigworld.com>','u3 <!test--u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !test folder'},
't30':{'casename':'MX-11227','receivers':['u1 <test\'---u1@bigworld.com>','u3 <test\'---u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"UserDataException"},
't31':{'casename':'MX-11228','receivers':[r'u1 <"te st---u1@bigworld.com">',r'u3 <"te st---u3@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't32':{'casename':'MX-11229','receivers':[r'u1 <"te\"st---u1@bigworld.com">',r'u3 <"te\"st---u3@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't33':{'casename':'MX-11230','receivers':['u1 <u1--+test@bigworld.com>','u3 <u3--+test@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't34':{'casename':'MX-11231','receivers':['u1 <u1--+Trash@bigworld.com>','u3 <u3--+Trash@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't35':{'casename':'MX-11232','receivers':['u1 <test--!u1@bigworld.com>','u3 <test--!u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't36':{'casename':'MX-11233','receivers':['u1 <Trash--!u1@bigworld.com>','u3 <Trash--!u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't37':{'casename':'MX-11234','receivers':['u1--- <u1++test\'@bigworld.com>','u3--- <u3++test\'@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to +test' folder"},
't38':{'casename':'MX-11235','receivers':['u1+++ <test\'---u1@bigworld.com>','u3+++ <test\'---u3@bigworld.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"UserDataException"},
            }
#set  subAddressAllowedIPs=127.0.0.1/10.49.58.239  on source server
print ("---->Set  subAddressAllowedIPs=127.0.0.1 ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=127.0.0.1\n10.49.58.239\";imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=127.0.0.1\n10.49.58.239\"\'','10.49.58.239','root','letmein',0)

#set  subAddressAllowedIPs=127.0.0.1/10.49.58.239  on dest serevr
print ("---->Set  subAddressAllowedIPs=127.0.0.1 ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=127.0.0.1\n10.49.58.239\";imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=127.0.0.1\n10.49.58.239\"\'','10.49.58.130','root','letmein',0)


#set relaySourcePolicy
print ("---->Set  relaySourcePolicy=allowALL ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/relaySourcePolicy=allowAll";imconfcontrol -install -key \"/inbound-standardmta-direct/mta/relaySourcePolicy=allowAll\"\'','10.49.58.239','root','letmein',0)


#set smtprelaytabl
print ("---->Set  smtprelay...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/mailRoutingTable=bigworld.com:10.49.58.130#20025";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/mailRoutingTable=bigworld.com:10.49.58.130#20025\"\'','10.49.58.239','root','letmein',0)



# restart mta server
print ("---->Restarting mta server ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.239','root','letmein',1,'imservctrl: done',1)
print ("---->Restarting mta server ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.130','root','letmein',1,'imservctrl: done',1)
time.sleep(5)

print ('---->Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 if exists
remote_operation('su - imail -c \
  "account-delete u2@whsasf.com;imdbcontrol dd whsasf.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',1)
  
remote_operation('su - imail -c \
  "account-delete u1@bigworld.com;account-delete u3@bigworld.com;imdbcontrol dd bigworld.com"',\
  '10.49.58.130','root','letmein',1,'Mailbox Deleted Successfully',2)
  
    
print ('---->Create u1,u2,u3 ...                  ',end='') #creaet account u1,u2,u3
remote_operation('su - imail -c \
  "imdbcontrol cd whsasf.com local;account-create u2@whsasf.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',1)

remote_operation('su - imail -c \
  "imdbcontrol cd bigworld.com local;account-create u1@bigworld.com p default;account-create u3@bigworld.com p default"',\
  '10.49.58.130','root','letmein',1,'MailboxId',2)
  

print ('---->Clear mta.log firsltly ...           ',end='') #clear mta.log firstly
remote_operation('su - imail -c "> log/mta.log"','10.49.58.130','root','letmein',0)

#set quote for sender and recepients
#ssdsdsd

print ('###############Beginning testing...######################')
for tck ,tcv in sorted(testcases.items(),key=lambda testcases:testcases[0]):
    print ('\033[1;45mRunning testing testcase: '+tck+'---------->'+tcv['casename']+'\033[0m')
    sendnum = len(tcv['receivers'])
    #print ('recivers numbers are:'+str(sendnum))
    print ('Sending message in proper formats ...',end='')
    send_mail(mtahost,mtaport,sender,tcv['receivers'])
    time.sleep(8)
    print ('Checking mta.log ...                 ',end='')
    remote_operation(tcv['commands'],sshtarget,sshaccount,sshpasswd,1,tcv['check_flags'],sendnum)
print ('###############Endding testing...######################') 

print ('---->Delete u1,u2,u3 ...',end='') #delete u1,u2,u3 at last
remote_operation('su - imail -c \
  "account-delete u1@bigworld.com;account-delete u3@bigworld.com;imdbcontrol dd bigworld.com"',\
  '10.49.58.130','root','letmein',1,'Mailbox Deleted Successfully',2)
remote_operation('su - imail -c \
  "account-delete u2@whsasf.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',1)