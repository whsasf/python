#!/usr/bin/env python3

from modules.sendmails import send_mail
from modules.remote_operations import remote_operation
import time
#reate summary file and debug files:
#sumfile = 'sumary.log'
#dbgfile = 'debug.log'
#with open(sumfile, 'a') as file_object:
#    file_object.write(attdata)

mtahost = '10.49.58.239'
mtaport = 20025
sshtarget = '10.49.58.121'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@whsasf.com>'

#define all the variables needed
testcases = {
't23':{'casename':'MX-11296','receivers':['u1 <"u1+te st@bigworld.com">','u3 <"u3+te st@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to te st folder'},
't24':{'casename':'MX-11297','receivers':[r'u1 <"u1+te\"st@bigworld.com">',r'u3 <"u3+te\"st@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to te"st folder'},
't32':{'casename':'MX-11305','receivers':[r'u1 <"te\"st---u1@bigworld.com">',r'u3 <"te\"st---u3@bigworld.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
           }
#set  subAddressAllowedIPs=10.49.58.239
print ("---->Set subAddressAllowedIPs=10.49.58.239 on dource mta ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=10.49.58.239\n8.8.8.8\";imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=10.49.58.239\n8.8.8.8\"\'','10.49.58.239','root','letmein',0)

print ("---->Set subAddressAllowedIPs=10.49.58.239 on dest mta ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=10.49.58.239\n8.8.8.8\";imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=10.49.58.239\n8.8.8.8\"\'','10.49.58.121','root','letmein',0)

#set relaySourcePolicy
print ("---->Set  relaySourcePolicy=allowALL ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/relaySourcePolicy=allowAll";imconfcontrol -install -key \"/inbound-standardmta-direct/mta/relaySourcePolicy=allowAll\"\'','10.49.58.239','root','letmein',0)

#set smtprelaytabl
print ("---->Set  smtprelay...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/mailRoutingTable=bigworld.com:10.49.58.121#20025";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/mailRoutingTable=bigworld.com:10.49.58.121#20025\"\'','10.49.58.239','root','letmein',0)



# restart mta server
print ("---->Restarting mta server on source ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.239','root','letmein',1,'imservctrl: done',1)
print ("---->Restarting mta server on dest ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.121','root','letmein',1,'imservctrl: done',1)
time.sleep(5)

print ('---->Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 if exists
remote_operation('su - imail -c \
  "account-delete u2@whsasf.com;imdbcontrol dd whsasf.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',1)
  
remote_operation('su - imail -c \
  "account-delete u1@bigworld.com;account-delete u3@bigworld.com;imdbcontrol dd bigworld.com"',\
  '10.49.58.121','root','letmein',1,'Mailbox Deleted Successfully',2)
  
    
print ('---->Create u1,u2,u3 ...                  ',end='') #creaet account u1,u2,u3
remote_operation('su - imail -c \
  "imdbcontrol cd whsasf.com local;account-create u2@whsasf.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',1)

remote_operation('su - imail -c \
  "imdbcontrol cd bigworld.com local;account-create u1@bigworld.com p default;account-create u3@bigworld.com p default"',\
  '10.49.58.121','root','letmein',1,'MailboxId',2)
  

print ('---->Clear mta.log firsltly ...           ',end='') #clear mta.log firstly
remote_operation('su - imail -c "> log/mta.log"','10.49.58.121','root','letmein',0)

#set quote for sender and recepients
#ssdsdsd
time.sleep(30)
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
  '10.49.58.121','root','letmein',1,'Mailbox Deleted Successfully',2)
remote_operation('su - imail -c \
  "account-delete u2@whsasf.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',1)