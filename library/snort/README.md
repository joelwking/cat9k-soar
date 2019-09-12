README
------


```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker run -it --name snort joelwking/snort:1.0
Thu Sep 12 13:05:09 2019 | INFO: snort.py 1.0
Thu Sep 12 13:05:09 2019 | INFO: use CTRL + c to exit!
Thu Sep 12 13:05:09 2019 | INFO: entering handle_action
Thu Sep 12 13:05:15 2019 | INFO: Created container 61
Thu Sep 12 13:05:15 2019 | INFO: Added artifact: 1162 to container: 61
Thu Sep 12 13:05:19 2019 | INFO: Added artifact: 1163 to container: 61
Thu Sep 12 13:05:36 2019 | INFO: Added artifact: 1164 to container: 61
Thu Sep 12 13:05:36 2019 | INFO: Added artifact: 1165 to container: 61
Thu Sep 12 13:05:37 2019 | INFO: Added artifact: 1166 to container: 61
Thu Sep 12 13:05:37 2019 | INFO: Added artifact: 1167 to container: 61
Thu Sep 12 13:05:38 2019 | INFO: Added artifact: 1168 to container: 61
Thu Sep 12 13:05:38 2019 | INFO: Added artifact: 1169 to container: 61
administrator@olive-iron:~/docker/cat9k-soar/library$
administrator@olive-iron:~/docker/cat9k-soar/library$
administrator@olive-iron:~/docker/cat9k-soar/library$ docker attach snort
Thu Sep 12 13:09:00 2019 | INFO: Added artifact: 1178 to container: 62
Thu Sep 12 13:09:00 2019 | INFO: Added artifact: 1179 to container: 62
Thu Sep 12 13:09:01 2019 | INFO: Added artifact: 1180 to container: 62
Thu Sep 12 13:09:01 2019 | INFO: Added artifact: 1181 to container: 62
Thu Sep 12 13:09:02 2019 | INFO: Added artifact: 1182 to container: 62
Thu Sep 12 13:09:02 2019 | INFO: Added artifact: 1183 to container: 62
read escape sequence
```

```
administrator@olive-iron:~$ docker stop snort
snort
administrator@olive-iron:~$ docker start snort
snort
administrator@olive-iron:~$ ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.052 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.055 ms
64 bytes from 172.17.0.2: icmp_seq=3 ttl=64 time=0.058 ms
^C
--- 172.17.0.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 1999ms
rtt min/avg/max/mdev = 0.052/0.055/0.058/0.002 ms
```