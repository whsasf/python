#!/usr/bin/env python3
import paramiko

command1 = 'ls -al'
command2 = 'imservping'
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.49.58.239', port=22, username='root', password='letmein')

stdin, stdout, stderr = ssh.exec_command(command1)
#stdin, stdout, stderr = ssh.exec_command(command2)
#stdin, stdout, stderr = ssh.exec_command('imservping')

result2 = stdout.read()
result3 = stderr.read()

print (result2.decode('utf-8'))
print (result3.decode('utf-8'))


ssh.close()

