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
't1':{'casename':'MX-11350','receivers':['u1 <u1+INBOX@openwave.com>','u3 <u3+INBOX>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to INBOX folder'},
't2':{'casename':'MX-11351','receivers':['u1 <u1+Trash@openwave.com>','u3 <u3+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't3':{'casename':'MX-11352','receivers':['u1 <u1+Trash/folder@openwave.com>','u3 <u3+Trash/folder>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder folder'},
't4':{'casename':'MX-11353','receivers':['u1 <u1+Trash/folder/folder1/folder2/folder3@openwave.com>','u3 <u3+Trash/folder/folder1/folder2/folder3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder/folder1/folder2/folder3 folder'},
't5':{'casename':'MX-11354','receivers':['u1 <INBOX--u1@openwave.com>','u3 <INBOX--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to INBOX folder'},
't6':{'casename':'MX-11355','receivers':['u1 <Trash--u1@openwave.com>','u3 <Trash--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't7':{'casename':'MX-11356','receivers':['u1 <Trash/folder--u1@openwave.com>','u3 <Trash/folder--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder folder'},
't8':{'casename':'MX-11357','receivers':['u1 <Trash/folder/folder1/folder2/folder3--u1@openwave.com>','u3 <Trash/folder/folder1/folder2/folder3--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash/folder/folder1/folder2/folder3 folder'},
't9':{'casename':'MX-11358','receivers':['u1 <u1+test@openwave.com>','u3 <u3+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't10':{'casename':'MX-11359','receivers':['u1 <u1+test/folder@openwave.com>','u3 <u3+test/folder>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder folder'},
't11':{'casename':'MX-11360','receivers':['u1 <u1+test/folder/folder1/folder2/folder3@openwave.com>','u3 <u3+test/folder/folder1/folder2/folder3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder/folder1/folder2/folder3 folder'},
't12':{'casename':'MX-11361','receivers':['u1 <test--u1@openwave.com>','u3 <test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't13':{'casename':'MX-11362','receivers':['u1 <test/folder--u1@openwave.com>','u3 <test/folder--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder folder'},
't14':{'casename':'MX-11363','receivers':['u1 <test/folder/folder1/folder2/folder3--u1@openwave.com>','u3 <test/folder/folder1/folder2/folder3--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test/folder/folder1/folder2/folder3 folder'},
't15':{'casename':'MX-11364','receivers':['<u1+Trash@openwave.com>','<u3+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't16':{'casename':'MX-11365','receivers':['<u1+test@openwave.com>','<u3+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't17':{'casename':'MX-11366','receivers':['u1 <u1+++test@openwave.com>','u3 <u3+++test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to ++test folder'},
't18':{'casename':'MX-11367','receivers':['u1 <u1+++Trash@openwave.com>','u3 <u3+++Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to ++Trash folder'},
't19':{'casename':'MX-11368','receivers':['u1 <u1+--Trash@openwave.com>','u3 <u3+--Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to --Trash folder'},
't20':{'casename':'MX-11369','receivers':['u1 <u1+--test@openwave.com>','u3 <u3+--test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to --test folder'},
't21':{'casename':'MX-11370','receivers':['u1 <u1+!test@openwave.com>','u3 <u3+!test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !test folder'},
't22':{'casename':'MX-11371','receivers':['u1 <u1+test\'@openwave.com>','u3 <u3+test\'>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to test' folder"},
't23':{'casename':'MX-11372','receivers':['u1 <"u1+te st@openwave.com">','u3 <"u3+te st">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to te st folder'},
't24':{'casename':'MX-11373','receivers':[r'u1 <"u1+te\"st@openwave.com">',r'u3 <"u3+te\"st">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to te"st folder'},
't25':{'casename':'MX-11374','receivers':['u1 <Trash--u1@openwave.com>','u3 <Trash--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to Trash folder'},
't26':{'casename':'MX-11375','receivers':['u1 <test--u1@openwave.com>','u3 <test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to test folder'},
't27':{'casename':'MX-11376','receivers':['u1 <test----u1@openwave.com>','u3 <test----u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't28':{'casename':'MX-11377','receivers':['u1 <Trash----u1@openwave.com>','u3 <Trash----u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't29':{'casename':'MX-11378','receivers':['u1 <!test--u1@openwave.com>','u3 <!test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered to !test folder'},
't30':{'casename':'MX-11379','receivers':['u1 <test\'---u1@openwave.com>','u3 <test\'---u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't31':{'casename':'MX-11380','receivers':[r'u1 <"te st---u1@openwave.com">',r'u3 <"te st---u3">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't32':{'casename':'MX-11381','receivers':[r'u1 <"te\"st---u1@openwave.com">',r'u3 <"te\"st---u3">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't33':{'casename':'MX-11382','receivers':['u1 <u1--+test@openwave.com>','u3 <u3--+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't34':{'casename':'MX-11383','receivers':['u1 <u1--+Trash@openwave.com>','u3 <u3--+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't35':{'casename':'MX-11384','receivers':['u1 <test--!u1@openwave.com>','u3 <test--!u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't36':{'casename':'MX-11385','receivers':['u1 <Trash--!u1@openwave.com>','u3 <Trash--!u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't37':{'casename':'MX-11386','receivers':['u1--- <u1++test\'@openwave.com>','u3--- <u3++test\'>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':"delivered to +test' folder"},
't38':{'casename':'MX-11387','receivers':['u1+++ <test\'---u1@openwave.com>','u3+++ <test\'---u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
            }
#set  subAddressAllowedIPs=10.49.58.240/30
print ("---->Set subAddressAllowedIPs=10.49.58.240/30 ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=10.49.58.240/30\n8.8.8.8\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=10.49.58.240/30\n8.8.8.8\"\'','10.49.58.239','root','letmein',0)

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