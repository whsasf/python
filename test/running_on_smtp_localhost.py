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
't1':{'casename':'MX-11124-1','receivers':['u1 <u1+Trash@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash'},
't1':{'casename':'MX-11124-2','receivers':['u1 <u1++++Trash@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to +++Trash'},
't1':{'casename':'MX-11124-3','receivers':['u1 <u1+--Trash@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to --Trash'},
't1':{'casename':'MX-11124-4','receivers':['u1 <u1+----Trash@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to ----Trash'},
't1':{'casename':'MX-11124-5','receivers':['u1 <u1+!Trash@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !Trash'},
't1':{'casename':'MX-11124-6','receivers':['u1 <"u1+Trash'@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to Trash'"},
't1':{'casename':'MX-11124-7','receivers':['u1 <"u1+Tras h@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to Tras h"},
't1':{'casename':'MX-11124-8','receivers':['u1 <Trash--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash'},
't1':{'casename':'MX-11124-9','receivers':['u1 <Trash-----u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash---'},
't1':{'casename':'MX-11124-10','receivers':['u1 <!Trash--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !Trash'},
't1':{'casename':'MX-11124-11','receivers':['u1 <"Trash'--u1@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to Trash'"},
't1':{'casename':'MX-11124-12','receivers':['u1 <"Tras h--u1@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to Tras h"},
't1':{'casename':'MX-11124-13','receivers':['u1 <u1+test@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test'},
't1':{'casename':'MX-11124-14','receivers':['u1 <u1++++test@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to +++test'},
't1':{'casename':'MX-11124-15','receivers':['u1 <u1+--test@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to --test'},
't1':{'casename':'MX-11124-16','receivers':['u1 <u1+----test@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to ----test'},
't1':{'casename':'MX-11124-17','receivers':['u1 <u1+!test@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !test'},
't1':{'casename':'MX-11124-18','receivers':['u1 <"u1+test'@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to test'"},
't1':{'casename':'MX-11124-19','receivers':['u1 <"u1+tes t@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to tes t"},
't1':{'casename':'MX-11124-20','receivers':['u1 <test--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test'},
't1':{'casename':'MX-11124-21','receivers':['u1 <test-----u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test---'},
't1':{'casename':'MX-11124-22','receivers':['u1 <!test--u1@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !test'},
't1':{'casename':'MX-11124-23','receivers':["u1 <test'--u1@openwave.com>"],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to test'"},
't1':{'casename':'MX-11124-24','receivers':['u1 <"tes t--u1@openwave.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to tes t"},
            }
#set  subAddressAllowedIPs=127.0.0.1
remote_operation('su - imail -c "imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=127.0.0.1\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=127.0.0.1\""','10.49.58.239','root','letmein',0)

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

print ('Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 at last
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)