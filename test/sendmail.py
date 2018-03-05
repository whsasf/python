#!/usr/bin/python3

import smtplib

sender = 'xx2@openwave.com'
receivers = ['xx1+Trash@openwave.com']

message = """From: From Person <xx2@openwave.com>
To: To Person <xx1+Trash@openwave.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('10.49.58.239',20025)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")