#!/usr/bin/env python3

from modules.sendmails import send_mail
from modules.remote_operations import remote_operation

#reate summary file and debug files:
#sumfile = 'sumary.log'
#dbgfile = 'debug.log'
#with open(sumfile, 'a') as file_object:
#    file_object.write(attdata)

mtahost = '10.49.58.147'
mtaport = 25
sshtarget = '10.49.58.147'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@qacopernicus.synchronoss.net>'

#define all the variables needed
testcases = {
't1':{'casename':'MX-11312','receivers':['u1 <u1+INBOX@qacopernicus.synchronoss.net>','u3 <u3+INBOX>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't2':{'casename':'MX-11313','receivers':['u1 <u1+Trash@qacopernicus.synchronoss.net>','u3 <u3+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't3':{'casename':'MX-11314','receivers':['u1 <u1+Trash/folder@qacopernicus.synchronoss.net>','u3 <u3+Trash/folder>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't4':{'casename':'MX-11315','receivers':['u1 <u1+Trash/folder/folder1/folder2/folder3@qacopernicus.synchronoss.net>','u3 <u3+Trash/folder/folder1/folder2/folder3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't5':{'casename':'MX-11316','receivers':['u1 <INBOX--u1@qacopernicus.synchronoss.net>','u3 <INBOX--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't6':{'casename':'MX-11317','receivers':['u1 <Trash--u1@qacopernicus.synchronoss.net>','u3 <Trash--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't7':{'casename':'MX-11318','receivers':['u1 <Trash/folder--u1@qacopernicus.synchronoss.net>','u3 <Trash/folder--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't8':{'casename':'MX-11319','receivers':['u1 <Trash/folder/folder1/folder2/folder3--u1@qacopernicus.synchronoss.net>','u3 <Trash/folder/folder1/folder2/folder3--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't9':{'casename':'MX-11320','receivers':['u1 <u1+test@qacopernicus.synchronoss.net>','u3 <u3+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't10':{'casename':'MX-11321','receivers':['u1 <u1+test/folder@qacopernicus.synchronoss.net>','u3 <u3+test/folder>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't11':{'casename':'MX-11322','receivers':['u1 <u1+test/folder/folder1/folder2/folder3@qacopernicus.synchronoss.net>','u3 <u3+test/folder/folder1/folder2/folder3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't12':{'casename':'MX-11323','receivers':['u1 <test--u1@qacopernicus.synchronoss.net>','u3 <test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't13':{'casename':'MX-11324','receivers':['u1 <test/folder--u1@qacopernicus.synchronoss.net>','u3 <test/folder--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't14':{'casename':'MX-11325','receivers':['u1 <test/folder/folder1/folder2/folder3--u1@qacopernicus.synchronoss.net>','u3 <test/folder/folder1/folder2/folder3--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't15':{'casename':'MX-11326','receivers':['<u1+Trash@qacopernicus.synchronoss.net>','<u3+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't16':{'casename':'MX-11327','receivers':['<u1+test@qacopernicus.synchronoss.net>','<u3+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't17':{'casename':'MX-11328','receivers':['u1 <u1+++test@qacopernicus.synchronoss.net>','u3 <u3+++test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't18':{'casename':'MX-11329','receivers':['u1 <u1+++Trash@qacopernicus.synchronoss.net>','u3 <u3+++Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't19':{'casename':'MX-11330','receivers':['u1 <u1+--Trash@qacopernicus.synchronoss.net>','u3 <u3+--Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't20':{'casename':'MX-11331','receivers':['u1 <u1+--test@qacopernicus.synchronoss.net>','u3 <u3+--test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't21':{'casename':'MX-11332','receivers':['u1 <u1+!test@qacopernicus.synchronoss.net>','u3 <u3+!test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't22':{'casename':'MX-11333','receivers':['u1 <u1+test\'@qacopernicus.synchronoss.net>','u3 <u3+test\'>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't23':{'casename':'MX-11334','receivers':['u1 <"u1+te st@qacopernicus.synchronoss.net">','u3 <"u3+te st">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't24':{'casename':'MX-11335','receivers':[r'u1 <"u1+te\"st@qacopernicus.synchronoss.net">',r'u3 <"u3+te\"st">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't25':{'casename':'MX-11336','receivers':['u1 <Trash--u1@qacopernicus.synchronoss.net>','u3 <Trash--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't26':{'casename':'MX-11337','receivers':['u1 <test--u1@qacopernicus.synchronoss.net>','u3 <test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't27':{'casename':'MX-11338','receivers':['u1 <test----u1@qacopernicus.synchronoss.net>','u3 <test----u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't28':{'casename':'MX-11339','receivers':['u1 <Trash----u1@qacopernicus.synchronoss.net>','u3 <Trash----u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't29':{'casename':'MX-11340','receivers':['u1 <!test--u1@qacopernicus.synchronoss.net>','u3 <!test--u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't30':{'casename':'MX-11341','receivers':['u1 <test\'---u1@qacopernicus.synchronoss.net>','u3 <test\'---u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't31':{'casename':'MX-11342','receivers':[r'u1 <"te st---u1@qacopernicus.synchronoss.net">',r'u3 <"te st---u3">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't32':{'casename':'MX-11343','receivers':[r'u1 <"te\"st---u1@qacopernicus.synchronoss.net">',r'u3 <"te\"st---u3">'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
't33':{'casename':'MX-11344','receivers':['u1 <u1--+test@qacopernicus.synchronoss.net>','u3 <u3--+test>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't34':{'casename':'MX-11345','receivers':['u1 <u1--+Trash@qacopernicus.synchronoss.net>','u3 <u3--+Trash>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't35':{'casename':'MX-11346','receivers':['u1 <test--!u1@qacopernicus.synchronoss.net>','u3 <test--!u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't36':{'casename':'MX-11347','receivers':['u1 <Trash--!u1@qacopernicus.synchronoss.net>','u3 <Trash--!u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'AcctUnknownUser'},
't37':{'casename':'MX-11348','receivers':['u1--- <u1++test\'@qacopernicus.synchronoss.net>','u3--- <u3++test\'>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'delivered:'},
't38':{'casename':'MX-11349','receivers':['u1+++ <test\'---u1@qacopernicus.synchronoss.net>','u3+++ <test\'---u3>'],'commands':'su - imail -c "cat log/mta.log;> log/mta.log"','check_flags':'UserDataException'},
	          }
#set  subAddressAllowedIPs=10.49.58.240
print ("---->Set subAddressAllowedIPs=10.49.58.240 ...",end='')
remote_operation('su - imail -c \'imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=10.49.58.149\n8.8.8.8\";imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=10.49.58.149\n8.8.8.8\"\'','10.49.58.147','root','letmein',0)

# restart mta server
print ("---->Restarting mta server ...",end='')
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.147','root','letmein',1,'imservctrl: done',1)

print ('---->Delete u1,u2,u3 if already existed...',end='') #delete u1,u2,u3 if exists
remote_operation('su - imail -c \
  "account-delete u1@qacopernicus.synchronoss.net;account-delete u2@qacopernicus.synchronoss.net;account-delete u3@qacopernicus.synchronoss.net"',\
  '10.49.58.147','root','letmein',1,'Mailbox Deleted Successfully',3)
    
print ('---->Create u1,u2,u3 ...                  ',end='') #creaet account u1,u2,u3
remote_operation('su - imail -c \
  "account-create u1@qacopernicus.synchronoss.net p default;account-create u2@qacopernicus.synchronoss.net p default;account-create u3@qacopernicus.synchronoss.net p default"',\
  '10.49.58.147','root','letmein',1,'MailboxId',3)

print ('---->Clear mta.log firsltly ...           ',end='') #clear mta.log firstly
remote_operation('su - imail -c "> log/mta.log"','10.49.58.147','root','letmein',0)

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

print ('---->Delete u1,u2,u3 ...',end='') #delete u1,u2,u3 at last
remote_operation('su - imail -c \
  "account-delete u1@qacopernicus.synchronoss.net;account-delete u2@qacopernicus.synchronoss.net;account-delete u3@qacopernicus.synchronoss.net"',\
  '10.49.58.147','root','letmein',1,'Mailbox Deleted Successfully',3)