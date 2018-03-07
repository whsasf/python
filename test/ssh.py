#!/usr/bin/env python3
import paramiko
#paramiko.util.log_to_file('ssh.log') # sets up logging ,disbale by default

command1 = 'su - imail -c "cat log/mta.log"'
hostname = '10.49.58.239'
port = 22
username = 'root'
password = 'letmein'


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname, port=port, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command(command1)
result = stdout.read()

if len(result) == 0:  
    print(str(stderr.read(),'utf-8'))
else:
    print(str(result,'utf-8'))

ssh.close()

