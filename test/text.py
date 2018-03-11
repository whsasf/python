#!/usr/bin/env python3

from modules.remote_operations import remote_operation

remote_operation('su - imail -c "imconfcontrol -install -key \"/*/mta/subAddressAllowedIPs=127.0.0.1\";imconfcontrol -install -key \"/site1-inbound-standardmta-direct/mta/subAddressAllowedIPs=127.0.0.1\""','10.49.58.239','root','letmein',0)
remote_operation('su - imail -c "~/lib/imservctrl killStart mta"', '10.49.58.239','root','letmein',1,'imservctrl: done',1)