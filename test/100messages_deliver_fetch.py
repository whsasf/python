#!/usr/bin/env python3

from modules.readmessages import imap_fetch
from modules.sendmails import send_mail
from modules.remote_operations import remote_operation
import time

mtahost = '10.49.58.239'
imaphost = '10.49.58.239'
mtaport = 20025
imapport = 20143
sshtarget = '10.49.58.239'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'm2 <m2@openwave.com>'
mailboxname = 'INBOX'
loginuser = 'm1'
loginpass = 'p'

print ('---->Delete m1,m2,xx3 if already existed...',end='') #delete m1,m2,xx3 if exists
remote_operation('su - imail -c \
  "account-delete m1@openwave.com;account-delete m2@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',2)
    
print ('---->Create m1,m2,xx3 ...                  ',end='') #creaet account m1,m2,xx3
remote_operation('su - imail -c \
  "account-create m1@openwave.com p default;account-create m2@openwave.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',2)
  
#set  account quota 
print ("---->Set  mailquotamaxmsgkb(mailquotatotkb) 0  ...",end='')
remote_operation('su - imail -c "imdbcontrol sac m1 openwave.com mailquotamaxmsgkb 0;imdbcontrol sac m1 openwave.com mailquotatotkb 0"','10.49.58.239','root','letmein',0)


#deliver 100 messages:
for c in range(1,101):
    print ("Delivering message"+str(c))
    send_mail(mtahost,mtaport,sender,['m1 <m1@openwave.com>'],c)

time.sleep(10)
# fetch 101 message body and firstlinedata

imap_fetch(imaphost,imapport,mailboxname,loginuser,loginpass)

