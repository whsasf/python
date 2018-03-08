def send_mail (mtahost,mtaport,fromuser,tousers,\
    marker = 'AUNIQUEMARKER',\
    mimeinfo = 'This is a multi-part message in MIME format.',\
    body = 'This is a test email to send an attachement,haha,enjoy.'\
    ):
    """ this function is used to send email"""
    #import basic libs
    import smtplib
    import base64
    
    #define variables
    smtphost = mtahost
    smtpport = mtaport
    sender = fromuser
    recievers = tousers
       
    #create a attachment file
    filename = 'attach.txt'
    attdata = str(base64.b64encode('world peace.are u OK?'.encode('utf-8')),'utf-8')
    #with open(filename, 'rw') as file_object:
    #    file_object.write(attdata)
    
    # Define the main headers.
    part1 = """From: %s
    To: %s
    Subject: Sending Attachement
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=%s
    %s
    --%s
    """.replace('\n    ','\n') %(sender,','.join(recievers),marker,mimeinfo,marker)
    
    # Define the message action
    part2 = """Content-Type: text/plain
    Content-Transfer-Encoding:8bit

    %s
    --%s
    """.replace('\n    ','\n') %(body,marker)
    
    # Define the attachment section
    part3 = """Content-Type: text/plain; name=\"%s\"
    Content-Transfer-Encoding:base64
    Content-Disposition: attachment; filename=\"%s\"

    %s
    --%s--
    """.replace('\n    ','\n') %(filename, filename, attdata, marker)
    message = part1 + part2 + part3
    
    #print (message)
    
    
    try:
       smtpObj = smtplib.SMTP(smtphost,smtpport)
       smtpObj.sendmail(sender, recievers, message)         
       print ("Successfully sent email")
    except smtplib.SMTPException:
       print ("Error: unable to send email")
    smtpObj.quit()