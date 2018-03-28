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
sender = 'x2 <x2@openwave.com>'
mailboxname = 'INBOX'
loginuser = 'x1'
loginpass = 'p'

print ('---->Delete x1,x2,xx3 if already existed...',end='') #delete x1,x2,xx3 if exists
remote_operation('su - imail -c \
  "account-delete x1@openwave.com;account-delete x2@openwave.com;account-delete xx3@openwave.com"',\
  '10.49.58.239','root','letmein',1,'Mailbox Deleted Successfully',3)
    
print ('---->Create x1,x2,xx3 ...                  ',end='') #creaet account x1,x2,xx3
remote_operation('su - imail -c \
  "account-create x1@openwave.com p default;account-create x2@openwave.com p default;account-create xx3@openwave.com p default"',\
  '10.49.58.239','root','letmein',1,'MailboxId',3)
  
#set  account quota 
print ("---->Set  mailquotamaxmsgkb(mailquotatotkb) 0  ...",end='')
remote_operation('su - imail -c "imdbcontrol sac x1 openwave.com mailquotamaxmsgkb 0;imdbcontrol sac x1 openwave.com mailquotatotkb 0"','10.49.58.239','root','letmein',0)


#deliver 100 messages:
for c in range(1,101):
    print ("Delivering message"+str(c))
    send_mail(mtahost,mtaport,sender,['x1 <x1@openwave.com>'])

time.sleep(10)
# fetch 101 message body and firstlinedata

imap_fetch(imaphost,imapport,mailboxname,loginuser,loginpass)

