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
$ docker save -o soar.tar  b8b2a96ebf80
```

### Verify the app will run

administrator@olive-iron:~/docker/cat9k-soar/library$ docker run -it --name soar --env INTERFACE=eth0  joelwking/soar:1.0
root@abcde6f1934e:/app#
root@abcde6f1934e:/app#
root@abcde6f1934e:/app# ls
Dockerfile          PhantomIngest.py   framework.py            local.rules      parse_alerts.sh   snort.conf
Dockerfile_woSnort  base_connector.py  framework_constants.py  parse_alerts.py  parse_alerts.yml  snort.py
root@abcde6f1934e:/app# python framework.py
Mon Sep  9 13:36:49 2019 | Hello world
Mon Sep  9 13:36:49 2019 | SNORT
Mon Sep  9 13:36:49 2019 | INFO: entering _test_connectivity
Mon Sep  9 13:36:49 2019 | INFO: entering handle_action
root@abcde6f1934e:/app# ENV




### Upload to the linux box in the sandbox
```
[developer@devbox tmp]$ ls -salt
total 468268
468260 -rw-r--r--   1 developer docker 479494656 Sep  9 07:19 soar.tar
```

### Prereqs
https://developer.cisco.com/docs/app-hosting/#!getting-cat9k-setup

Before Application Hosting can be enabled on Cat9K, a Cisco certified USB3.0 Flash Drive must be installed in the device back-panel USB3.0 port. Application hosting only works on the back-panel USB3.0.
```
cat9k#show hardware | include flash
System image file is "flash:packages.conf"
11264000K bytes of Flash at flash:.
117219783K bytes of USB Flash at usbflash1:.
```

cat9k#cd usbflash1:/
cat9k#pwd
usbflash1:/

The Switch must be running release version 16.12. Docker App is supported only on release 16.12, as this version supports native docker engine. 
```
cat9k#show ver | inc IOS XE
Cisco IOS XE Software, Version 16.12.01ah1
```

### Licensing

Technology Package License Information:

------------------------------------------------------------------------------
Technology-package                                     Technology-package
Current                        Type                       Next reboot
------------------------------------------------------------------------------
network-advantage       Smart License                    network-advantage
dna-advantage           Subscription Smart License       dna-advantage


### Verify services are running

cat9k#config t
Enter configuration commands, one per line.  End with CNTL/Z.
cat9k(config)#iox
cat9k(config)#end
cat9k#show iox-service

IOx Infrastructure Summary:
---------------------------
IOx service (CAF)    : Running
IOx service (HA)     : Running
IOx service (IOxman) : Running
Libvirtd             : Running
Dockerd              : Running


### Copy image

I uploaded the .tar file to the developer sandbox Linux host (from my laptop) as the linux to linux transfer is quicker over the Internet from the cat 9K

copy scp://developer@10.10.20.20://tmp/soar.tar usbflash1://soar.tar vrf Mgmt-vrf
...
479494656 bytes copied in 405.028 secs (1183856 bytes/sec)
cat9k#


### executing on Cat9K


https://developer.cisco.com/docs/app-hosting/#!getting-started-with-docker-applications-deployment/install-activate-and-start-app

`app-hosting install appid SOAR package usbflash1:soar.tar`

cat9k#app-hosting install appid SOAR package usbflash1:soar.tar
Installing package 'usbflash1:soar.tar' for 'SOAR'. Use 'show app-hosting list' for progress.

### show device
```
cat9k#show app-hosting device
USB port          Device name           Available
      1            Front_USB_1         true
```

### show app-hosting infra
cat9k#show app-hosting infra
App signature verification: disabled
Internal working directory: /vol/usb1/iox

### show app-hosting resource

cat9k#show app-hosting resource
CPU:
  Quota: 7400(Units)
  Available: 7400(Units)
Memory:
  Quota: 2048(MB)
  Available: 2048(MB)
Storage space:
  Total: 120000(MB)
  Available: 120000(MB)


### show app-hosting detail


### copy to flash
cat9k#dir flash:/soar.tar
Directory of flash:/soar.tar

262181  -rw-        479494656  Sep 10 2019 00:30:11 +00:00  soar.tar

cat9k#dir usbflash1:soar.tar
Directory of usbflash1:/soar.tar

   12  -rw-        479494656  Sep 10 2019 00:12:34 +00:00  soar.tar

118014062592 bytes total (111303131136 bytes free)


### Install app

cat9k#app-hosting install appid SOAR package flash:soar.tar
Installing package 'flash:soar.tar' for 'SOAR'. Use 'show app-hosting list' for progress.


cat9k#show app-hosting utilization  appid SOAR
% Error: The application: SOAR, does not exist




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
