#!/usr/bin/python3
#coding:utf-8

from email import encoders  
from email.header import Header  
from email.mime.text import MIMEMultipart
from email.utils import parseaddr, formataddr  


import smtplib  
#字符集转换  
def __format_addr(s):  
    name, addr = parseaddr(s)  
    return formataddr((Header(name, 'utf-8').decode(), addr))  
#基本信息初始化  
from_addr = 'xx2@openwave.com'
to_addr = 'xx1@openwave.com'
#使用MIMEMultipart定义Message  
msg = MIMEMultipart()  
#初始化头  
msg['From'] = __format_addr('Your Dady: <%s>' % from_addr)  
msg['To'] = __format_addr('Son: <%s>' % to_addr)  
msg['Subject'] = Header('A how are you from......').encode()  
#将文本内容添加入邮件  
msg.attach(MIMEText('Send with file......', 'plain', 'utf-8'))  
#打开一个图片文件，将其添加到邮件中  
with open('format.png', 'rb') as f:  
    mime = MIMEBase('image', 'png', filename = 'format.png')  
    #添加头部信息  
    mime.add_header('Content-Disposition', 'attachment', filename = 'format.png')  
    mime.add_header('Content-ID', '<0>')  
    mime.add_header('X-Attachment-Id', '0')  
    #读取信息，默认字符集为空，这里是图片就不用设置了  
    mime.set_payload(f.read())  
    #使用Base64对图片编码  
    encoders.encode_base64(mime)  
    msg.attach(mime)  