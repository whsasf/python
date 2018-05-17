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
sshtarget = '10.49.58.239'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@openwave.com>'

#define all the variables needed
testcases = {
't1':{'casename':'MX-11236','receivers':['u1 <u1+INBOX@openwave.com>','u3 <u3+INBOX@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't2':{'casename':'MX-11237','receivers':['u1 <u1+Trash@openwave.com>','u3 <u3+Trash@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't3':{'casename':'MX-11238','receivers':['u1 <u1+Trash/folder@openwave.com>','u3 <u3+Trash/folder@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't4':{'casename':'MX-11239','receivers':['u1 <u1+Trash/folder/folder1/folder2/folder3@openwave.com>','u3 <u3+Trash/folder/folder1/folder2/folder3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't5':{'casename':'MX-11240','receivers':['u1 <INBOX--u1@openwave.com>','u3 <INBOX--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't6':{'casename':'MX-11241','receivers':['u1 <Trash--u1@openwave.com>','u3 <Trash--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't7':{'casename':'MX-11242','receivers':['u1 <Trash/folder--u1@openwave.com>','u3 <Trash/folder--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't8':{'casename':'MX-11243','receivers':['u1 <Trash/folder/folder1/folder2/folder3--u1@openwave.com>','u3 <Trash/folder/folder1/folder2/folder3--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't9':{'casename':'MX-11244','receivers':['u1 <u1+test@openwave.com>','u3 <u3+test@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't10':{'casename':'MX-11245','receivers':['u1 <u1+test/folder@openwave.com>','u3 <u3+test/folder@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't11':{'casename':'MX-11246','receivers':['u1 <u1+test/folder/folder1/folder2/folder3@openwave.com>','u3 <u3+test/folder/folder1/folder2/folder3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't12':{'casename':'MX-11247','receivers':['u1 <test--u1@openwave.com>','u3 <test--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't13':{'casename':'MX-11248','receivers':['u1 <test/folder--u1@openwave.com>','u3 <test/folder--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't14':{'casename':'MX-11249','receivers':['u1 <test/folder/folder1/folder2/folder3--u1@openwave.com>','u3 <test/folder/folder1/folder2/folder3--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't15':{'casename':'MX-11250','receivers':['<u1+Trash@openwave.com>','<u3+Trash@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't16':{'casename':'MX-11251','receivers':['<u1+test@openwave.com>','<u3+test@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't17':{'casename':'MX-11252','receivers':['u1 <u1+++test@openwave.com>','u3 <u3+++test@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't18':{'casename':'MX-11253','receivers':['u1 <u1+++Trash@openwave.com>','u3 <u3+++Trash@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't19':{'casename':'MX-11254','receivers':['u1 <u1+--Trash@openwave.com>','u3 <u3+--Trash@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't20':{'casename':'MX-11255','receivers':['u1 <u1+--test@openwave.com>','u3 <u3+--test@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't21':{'casename':'MX-11256','receivers':['u1 <u1+!test@openwave.com>','u3 <u3+!test@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't22':{'casename':'MX-11257','receivers':['u1 <u1+test\'@openwave.com>','u3 <u3+test\'@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't23':{'casename':'MX-11258','receivers':['u1 <"u1+te st@openwave.com">','u3 <"u3+te st@bigchina.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't24':{'casename':'MX-11259','receivers':[r'u1 <"u1+te\"st@openwave.com">',r'u3 <"u3+te\"st@bigchina.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't25':{'casename':'MX-11260','receivers':['u1 <Trash--u1@openwave.com>','u3 <Trash--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't26':{'casename':'MX-11261','receivers':['u1 <test--u1@openwave.com>','u3 <test--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't27':{'casename':'MX-11262','receivers':['u1 <test----u1@openwave.com>','u3 <test----u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't28':{'casename':'MX-11263','receivers':['u1 <Trash----u1@openwave.com>','u3 <Trash----u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't29':{'casename':'MX-11264','receivers':['u1 <!test--u1@openwave.com>','u3 <!test--u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't30':{'casename':'MX-11265','receivers':['u1 <test\'---u1@openwave.com>','u3 <test\'---u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't31':{'casename':'MX-11266','receivers':[r'u1 <"te st---u1@openwave.com">',r'u3 <"te st---u3@bigchina.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't32':{'casename':'MX-11267','receivers':[r'u1 <"te\"st---u1@openwave.com">',r'u3 <"te\"st---u3@bigchina.com">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't33':{'casename':'MX-11268','receivers':['u1 <u1--+test@openwave.com>','u3 <u3--+test@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't34':{'casename':'MX-11269','receivers':['u1 <u1--+Trash@openwave.com>','u3 <u3--+Trash@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't35':{'casename':'MX-11270','receivers':['u1 <test--!u1@openwave.com>','u3 <test--!u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't36':{'casename':'MX-11271','receivers':['u1 <Trash--!u1@openwave.com>','u3 <Trash--!u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't37':{'casename':'MX-11272','receivers':['u1--- <u1++test\'@openwave.com>','u3--- <u3++test\'@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't38':{'casename':'MX-11273','receivers':['u1+++ <test\'---u1@openwave.com>','u3+++ <test\'---u3@bigchina.com>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
	          }
#set  subAddressAllowedIPs=127.0.0.1
print ("---->Set subAddressAllowedIPs=127.0.0.1 ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=127.0.0.1\n8.8.8.8\";imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=127.0.0.1\n8.8.8.8\"\'','10.49.58.239','root','letmein',0)

#set relaySourcePolicy
print ("---->Set  relaySourcePolicy=allowALL ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/relaySourcePolicy=allowAll";imconfcontrol -install -key \"/inbound-standardmta-direct/mta/relaySourcePolicy=allowAll\"\'','10.49.58.239','root','letmein',0)

#set smtprelaytabl
#print ("---->Set  smtprelay...",end='')
#remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/mailRoutingTable=bigchina.com:10.49.58.239#20025";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/mailRoutingTable=bigchina.com:10.49.58.239#20025\"\'','10.49.58.239','root','letmein',0)

# restart mta server
print ("---->Restarting mta server ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.239','root','letmein',1,'imservctrl: done',1)

time.sleep(5)

print ('---->Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 if exists
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@bigchina.com;imdbcontrol dd bigchina.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)
    
print ('---->Create u1,u2,u3 ...                  ',end='') #creaet account u1,u2,u3
remote_operation('su - imail -c \
  "imdbcontrol cd bigchina.com local;account-create u1@openwave.com p default;account-create u2@openwave.com p default;account-create u3@bigchina.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',3)

print ('Clear mta.log firsltly ...           ',end='') #clear mta.log firstly
remote_operation('su - imail -c "> log/mta.log"','10.49.58.239','root','letmein',0)

#set quote for sender and recepients
#ssdsdsd

print ('###############Beginning testing...######################')
for tck ,tcv in sorted(testcases.items(),key=lambda testcases:testcases[0]):
    print ('---->run imrecalcmboxstats for u1 ...           ',end='')
    remote_operation("su - imail -c \"msgid=\$(imboxstats u1@openwave.com|grep Statistics|awk '{print \$5}');echo \$msgid >xx.txt;imrecalcmboxstats mx1 repair \$msgid ''\"",'10.49.58.239','root','letmein',0)
    print ('---->run imrecalcmboxstats for u3 ...           ',end='')
    remote_operation("su - imail -c \"msgid=\$(imboxstats u3@bigworld.com|grep Statistics|awk '{print \$5}');echo \$msgid >xx.txt;imrecalcmboxstats mx1 repair \$msgid ''\"",'10.49.58.239','root','letmein',0)

    print ('\033[1;45mRunning testing testcase: '+tck+'---------->'+tcv['casename']+'\033[0m')
    sendnum = len(tcv['receivers'])
    #print ('recivers numbers are:'+str(sendnum))
    print ('Sending message in proper formats ...',end='')
    send_mail(mtahost,mtaport,sender,tcv['receivers'])
    time.sleep(7)
    print ('Checking mta.log ...                 ',end='')
    remote_operation(tcv['commands'],sshtarget,sshaccount,sshpasswd,1,tcv['check_flags'],sendnum)
print ('###############Endding testing...######################') 

print ('---->Delete u1,u2,u3 ...',end='') #delete u1,u2,u3 at last
remote_operation('su - imail -c \
  "account-delete u1@openwave.com;account-delete u2@openwave.com;account-delete u3@bigchina.com;imdbcontrol dd bigchina.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)