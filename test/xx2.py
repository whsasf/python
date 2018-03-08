#!/usr/bin/env python3

from modules.remote_operations import remote_operation

remote_operation('su - imail -c "cat  log/mta.log;> log/mta.log"','10.49.58.239','root','letmein','delivered to b')