#!/usr/bin/python3
import smtplib

smtphost='10.49.58.239'
smtpport=20025
sender = 'xx2@openwave.com'
receivers = ['xx1+what@openwave.com','xx3+what@openwave.com']

#From: From Person <sender>
#To: To Person <receivers>

message = """
Subject: SMTP e-mail test

This is a test e-mail message3.
"""

try:
   smtpObj = smtplib.SMTP(smtphost,smtpport)
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
smtpObj.quit()