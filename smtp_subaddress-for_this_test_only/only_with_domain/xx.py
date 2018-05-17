#!/usr/bin/python3
from modules.sendmails import send_mail
from modules.remote_operations import remote_operation
mtahost = '10.49.58.239'
mtaport = 20025
sshtarget = '10.49.58.239'
sshaccount = 'root'
sshpasswd = 'letmein'
sender = 'u2 <u2@openwave.com>'

remote_operation('su - imail -c "imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=127.0.0.1\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=127.0.0.1\""','10.49.58.239','root','letmein',0)
