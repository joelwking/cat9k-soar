README
------

```
administrator@olive-iron:~/docker$ git clone https://github.com/joelwking/cat9k-soar.git

```
```
administrator@olive-iron:~/docker$ cd cat9k-soar/library
```
```
administrator@olive-iron:~/docker/cat9k-soar/library$ cat snort/snort.yml
---
#
#  configuration file for parse_alerts.py
#
alert_csv: /var/log/snort/alert.csv
msg_tag: '__cat9K_'

phantom:
    short_name: ec2
    ph_auth_token: "p9d+65AW77775erAW3MlXTSOAROa4gIaCIi081Rx7Lg="
    public_ip: "192.0.2.1"
    public_dns: "ec2-192-0-2-1.compute-1.amazonaws.com"
    container_id: FUTURE
```
```

```
administrator@olive-iron:~/docker/cat9k-soar/library$ cat snort/local.rules
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
# ----------------
# LOCAL RULES
# ----------------
# This file intentionally does not come with signatures.  Put your local
# additions here.
#
alert icmp any any -> any any (msg:"__cat9K_ICMP test"; sid:1000001; rev:1; classtype:icmp-event;)
alert tcp any any -> any 23 (msg:”__cat9K_TCP Port Scanning”; sid:1000006; rev:1;)administrator@olive-iron:~/docker/cat9k-soar/library$
```
```
```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker build -f ./snort/Dockerfile -t joelwking/snort:1.0 .
```

```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker run -it --name snort joelwking/snort:1.0
Fri Sep 13 01:26:53 2019 | INFO: snort.py 1.0
Fri Sep 13 01:26:53 2019 | INFO: use CTRL + c to exit!
Fri Sep 13 01:26:53 2019 | INFO: entering handle_action
Fri Sep 13 01:26:58 2019 | INFO: Created container 64
Fri Sep 13 01:26:59 2019 | INFO: Added artifact: 1184 to container: 64
Fri Sep 13 01:27:02 2019 | INFO: Added artifact: 1185 to container: 64
Fri Sep 13 01:27:07 2019 | INFO: Added artifact: 1186 to container: 64
Fri Sep 13 01:27:08 2019 | INFO: Added artifact: 1187 to container: 64
Fri Sep 13 01:27:08 2019 | INFO: Added artifact: 1188 to container: 64
Fri Sep 13 01:27:09 2019 | INFO: Added artifact: 1189 to container: 64
```
```
administrator@olive-iron:~$ ping -c 2 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.053 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.028 ms

```

```
Fri Sep 13 01:34:39 2019 | WARN: exception while adding artifact Failure to communicate: 401 {"failed": true, "message": "invalid token from 65.116.106.4"}
Fri Sep 13 01:34:40 2019 | WARN: exception while adding artifact Failure to communicate: 401 {"failed": true, "message": "invalid token from 65.116.106.4"}
Fri Sep 13 01:34:40 2019 | WARN: exception while adding artifact Failure to communicate: 401 {"failed": true, "message": "invalid token from 65.116.106.4"}
Fri Sep 13 01:34:41 2019 | WARN: exception while adding artifact Failure to communicate: 401 {"failed": true, "message": "invalid token from 65.116.106.4"}


```
```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker save -o /tmp/snort.tar joelwking/snort:1.0
```