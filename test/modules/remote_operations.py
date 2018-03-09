####################func1 ,remote  operation#######################################
def remote_operation(cmds,sshhost,user,passwd,checkyns,\
    check_flag = '',\
    check_target = 1 ,\
    sshport = 22,\
    outlog = 'sshout.log',\
    errorlog = 'ssherror.log',\
    check_flag_double_check = 'Unable to delete the mailbox' ,\
    ):
    '''function to run commands via ssh'''
     # "check_flag_double_check" currently only for account-delete
    import paramiko
    #paramiko.util.log_to_file('ssh.log') # sets up logging ,disbale by default
    
    commands = cmds
    hostname = sshhost
    username = user
    password = passwd   
    checkyn = checkyns
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=sshport, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(commands)
    okout = stdout.read()
    errout = stderr.read()
    #print ('err:'+str(errout,'utf-8'))
    #print ('ok:'+str(okout,'utf-8'))
    if checkyn == 1:
        if len(okout) == 0:  
            out=str(errout,'utf-8')
            #print(out,end='')
            #write error log to file
            with open(errorlog,'a') as file_object_err:
                file_object_err.write(out)
            if out.count(check_flag_double_check) == check_target:
                print('\033[1;32m  Operation success\033[0m')
            else:
                print ('\033[1;31m  Operation failed,no need to continue,please check'+errorlog+'!\033[0m')
        else:
            out=str(okout,'utf-8')
            #print(out,end='')
            #write out log to file
            with open(outlog,'a') as file_object_ok:
                file_object_ok.write(out)
            if out.count(check_flag) == check_target or out.count(check_flag_double_check) == check_target:
                print('\033[1;32m  Operation success\033[0m')
            else:
                print('\033[1;31m  Operation failed\033[0m')
    else:
        print ('\033[1;32m  Operation success\033[0m')
    ssh.close()
        
