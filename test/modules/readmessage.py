#!/usr/bin/env python3

from imaplib import IMAP4

conn = IMAP4(host='10.49.58.239', port=20143)
conn.login('u1','p')
conn.select(mailbox='INBOX', readonly=False)