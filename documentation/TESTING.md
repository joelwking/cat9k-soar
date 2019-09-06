TESTING
-------

## Testing parse_alerts.py

When testing outside the container, you can execute the program and simply manually add CSV records to the file
```bash
root@olive-iron:/var/log/snort# sudo echo '09/03-15:20:34.587699 ,1,1000001,3,"__S_ICMP_cat9Ktest",ICMP,172.17.0.1,,172.17.0.2,,02:42:38:29:34:94,02:42:AC:11:00:02,0x62,,,,,,64,0,65339,84,86016,8,0,10379,1' >>alert.csv
```

## Running Snort interactively from the container

```bash
root@785b77eabd12:/app# snort  -q -i eth0 -c /etc/snort/snort.conf -K ascii &
```

## Manually running parse_alerts.py

```
root@785b77eabd12:/app# wget https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/REST_ingest/PhantomIngest.py
root@785b77eabd12:/app# python2.7 parse_alerts.py

```
The output may look like the following:
```
root@785b77eabd12:/app# python2.7 parse_alerts.py
Wed Sep  4 18:07:11 2019 | INFO: parse_alerts.py .99
Wed Sep  4 18:07:11 2019 | INFO: use CTRL + c to exit!
Wed Sep  4 18:07:12 2019 | INFO: Created container 18
Wed Sep  4 18:07:24 2019 | INFO: Added artifact: 15 to container: 18
Wed Sep  4 18:07:24 2019 | INFO: Added artifact: 16 to container: 18
Wed Sep  4 18:07:25 2019 | INFO: Added artifact: 17 to container: 18
Wed Sep  4 18:07:25 2019 | INFO: Added artifact: 18 to container: 18
Wed Sep  4 18:07:26 2019 | INFO: Added artifact: 19 to container: 18
Wed Sep  4 18:07:26 2019 | INFO: Added artifact: 20 to container: 18
Wed Sep  4 18:07:27 2019 | INFO: Added artifact: 21 to container: 18
Wed Sep  4 18:07:27 2019 | INFO: Added artifact: 22 to container: 18
Wed Sep  4 18:07:28 2019 | INFO: Added artifact: 23 to container: 18
Wed Sep  4 18:07:28 2019 | INFO: Added artifact: 24 to container: 18
Wed Sep  4 18:07:29 2019 | INFO: Added artifact: 25 to container: 18
Wed Sep  4 18:07:29 2019 | INFO: Added artifact: 26 to container: 18
Wed Sep  4 18:07:30 2019 | INFO: Added artifact: 27 to container: 18
Wed Sep  4 18:07:30 2019 | INFO: Added artifact: 28 to container: 18
^CWed Sep  4 18:10:56 2019 | INFO: interrupt 2 caught, exiting.
```
### Running the image

`docker run -it --name snort --env INTERFACE=eth0  joelwking/snort`


### Issuing commands in the container

administrator@olive-iron:~/docker/cat9k-soar/library$  docker exec -it snort /bin/bash

root@c1893265e8dd:/app#
root@b1c4c10aa23c:/app# ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 17:09 pts/0    00:00:00 /bin/bash parse_alerts.sh
root         7     1 98 17:09 pts/0    00:07:22 python2.7 parse_alerts.py ./parse_alerts.yml
root         8     0  0 17:09 pts/1    00:00:00 /bin/bash
root        23     8  0 17:11 pts/1    00:00:01 snort -q -i eth0 -c /etc/snort/snort.conf -K ascii
root        26     8  0 17:16 pts/1    00:00:00 ps -ef

### Saving the image for deployment on the Cat9K

```
$ docker save -o cat9k.tar  b8b2a96ebf80
```

### executing on Cat9K


https://developer.cisco.com/docs/app-hosting/#!getting-started-with-docker-applications-deployment/install-activate-and-start-app

`app-hosting install appid SOAR package usbflash:cat9k.tar`

https://success.docker.com/article/multiple-docker-networks
```
interface AppGigabitEthernet 1/0/1
   switchport mode trunk

 app-hosting appid SOAR
    app-vnic AppGigabitEthernet trunk
       guest-interface eth1
```       

```
app-hosting activate appid SOAR
```

```
app-hosting start appid SOAR
```
