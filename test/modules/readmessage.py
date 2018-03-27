#!/usr/bin/env python3

from imaplib import IMAP4

conn = IMAP4(host='10.49.58.239', port=20143)
conn.login('xx1','p')
conn.select(mailbox='INBOX', readonly=False)
message="FROM: xx2\r\n\
to:xx1\r\n\
data\t\n\
\r\n\
helo world\r\n"

conn.append('INBOX','unseen',1522146813,message.encode("utf-8") )

conn.fetch("1001",'full')

conn.logout()