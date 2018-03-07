#!/usr/bin/env python3

import smtplib
import base64

#create a attachment file
filename = 'attach.txt'
attdata = str(base64.b64encode('world peace.are u OK?'.encode('utf-8')),'utf-8')
with open(filename, 'w') as file_object:
    file_object.write(attdata)

smtphost = '10.49.58.239'
smtpport = 20025
sender = 'xx2@openwave.com'
recievers = ['xx1 <xx1+xyz@openwave.com>','xx3 <xx3+xyz@openwave.com>']

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: %s
To: %s
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (sender,','.join(recievers),marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: text/plain; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=\"%s\"

%s
--%s--
""" %(filename, filename, attdata, marker)
message = part1 + part2 + part3

#print (message)


try:
   smtpObj = smtplib.SMTP(smtphost,smtpport)
   smtpObj.sendmail(sender, recievers, message)         
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
smtpObj.quit()