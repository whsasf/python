#!/usr/bin/python3
from modules.sendmails import send_mail
from modules.remote_operations import remote_operation
mtahost = '10.49.58.239'
mtaport = 20025
sshtarget = '10.49.58.239'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@openwave.com>'

#define all the variables needed
testcases = {
't37':{'casename':'MX-11234','receivers':['u1 <u1++test\'@openwave.com','u3 <u3++test\'@openwave.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"+test'"},
           }
#set  subAddressAllowedIPs=10.37.2.214
remote_operation('su - imail -c "imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=10.37.2.214\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=10.37.2.214\""','10.49.58.239','root','letmein',0)

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

#print ('Delete u1,u2,u3 ...',end='') #delete u1,u2,u3 at last
#remote_operation('su - imail -c \
#  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@openwave.com"',\
#  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)