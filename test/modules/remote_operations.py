def remote_operation(cmds,sshhost,user,passwd,check_flags,\
    sshport = 22,\
    outlog = 'sshout.log',\
    errorlog = 'ssherror.log'\
    ):
    
    import paramiko
    #paramiko.util.log_to_file('ssh.log') # sets up logging ,disbale by default
    
    commands = cmds
    hostname = sshhost
    username = user
    password = passwd   
    check_flag = check_flags #'delivered to xyz'  #if delivered to inbox,should be ":" ,will be a lists    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=sshport, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(commands)
    okout = stdout.read()
    errout = stderr.read()
    
    if len(okout) == 0:  
        out=str(errout,'utf-8')
        print(out)
        continue_flag = 0
        #write error log to file
        with open(errorlog,'w') as file_object_err:
            file_object_err.write(out)
    else:
        out=str(okout,'utf-8')
        print(out)
        continue_flag = 1
        #write out log to file
        with open(outlog,'w') as file_object_ok:
            file_object_ok.write(out)
    ssh.close()
    
    if continue_flag == 1:
        if out.count(check_flag) == 2:
            print('\033[4;32mtest case success\033[0m')
        else:
            print('\033[4;31mtest case failed\033[0m')
    else:
        print ('ssh operations failed,no need to continue,please check'+errorlog+'!') 