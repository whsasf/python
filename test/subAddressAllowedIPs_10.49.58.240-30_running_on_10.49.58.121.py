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
't1':{'casename':'MX-11072','receivers':['u1 <u1+INBOX@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't2':{'casename':'MX-11073','receivers':['u1 <u1+Trash@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't3':{'casename':'MX-11074','receivers':['u1 <u1+Trash/folder@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't4':{'casename':'MX-11075','receivers':['u1 <u1+Trash/folder/folder1/folder2/folder3@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't5':{'casename':'MX-11076','receivers':['u1 <INBOX--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't6':{'casename':'MX-11077','receivers':['u1 <Trash--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't7':{'casename':'MX-11078','receivers':['u1 <Trash/folder--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't8':{'casename':'MX-11079','receivers':['u1 <Trash/folder/folder1/folder2/folder3--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't9':{'casename':'MX-11080','receivers':['u1 <u1+test@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't10':{'casename':'MX-11081','receivers':['u1 <u1+test/folder@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't11':{'casename':'MX-11082','receivers':['u1 <u1+test/folder/folder1/folder2/folder3@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't12':{'casename':'MX-11083','receivers':['u1 <test--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't13':{'casename':'MX-11084','receivers':['u1 <test/folder--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't14':{'casename':'MX-11085','receivers':['u1 <test/folder/folder1/folder2/folder3--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
	          }
#set  subAddressAllowedIPs=127.0.0.1
remote_operation('su - imail -c "imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=10.49.58.240\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=10.49.58.240\""','10.49.58.239','root','letmein',0)

# restart mta server
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.239','root','letmein',1,'imservctrl: done',1)

print ('Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 if exists
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)
    
print ('Create u1,u2,u3 ...                  ',end='') #creaet account u1,u2,u3
remote_operation('su - imail -c \
  "account-create u1@openwave.com p default;account-create u2@openwave.com p default;account-create u3@openwave.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',3)

print ('Clear mta.log firsltly ...           ',end='') #clear mta.log firstly
remote_operation('su - imail -c "> log/mta.log"','10.49.58.239','root','letmein',0)

#set quote for sender and recepients
#ssdsdsd

print ('###############Beginning testing...######################')
for tck ,tcv in sorted(testcases.items(),key=lambda testcases:testcases[0]):
    print ('\033[1;45mRunning testing testcase: '+tck+'---------->'+tcv['casename']+'\033[0m')
    sendnum = len(tcv['receivers'])
    #print ('recivers numbers are:'+str(sendnum))
    print ('Sending message in proper formats ...',end='')
    send_mail(mtahost,mtaport,sender,tcv['receivers'])
    print ('Checking mta.log ...                 ',end='')
    remote_operation(tcv['commands'],sshtarget,sshaccount,sshpasswd,1,tcv['check_flags'],sendnum)
print ('###############Endding testing...######################') 

print ('Delete u1,u2,u3 ...',end='') #delete u1,u2,u3 at last
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)