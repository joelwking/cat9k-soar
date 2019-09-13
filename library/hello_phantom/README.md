README
------

```
administrator@olive-iron:~/docker$ git clone https://github.com/joelwking/cat9k-soar.git

```
```
administrator@olive-iron:~/docker$ cd cat9k-soar/library
```

```
administrator@olive-iron:~/docker/cat9k-soar/library$ cat hello_phantom/hello.yml
---
phantom:
    ph_auth_token: "p9d+65AW77775erAW3MlXTSOAROa4gIaCIi081Rx7Lg="
    public_ip: "192.0.2.1"

```


administrator@olive-iron:~/docker/cat9k-soar/library$ docker build -f ./hello_phantom/Dockerfile -t  joelwking/hello:1.0 .
```

```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker images joelwking/hello:1.0
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
joelwking/hello     1.0                 778b15372b6f        22 seconds ago      465MB

```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker run -it --name hello joelwking/hello:1.0
Thu Sep 12 23:58:27 2019 | INFO: hello.py 1.0
Thu Sep 12 23:58:27 2019 | INFO: use CTRL + c to exit!
Thu Sep 12 23:58:27 2019 | INFO: HELLO
Thu Sep 12 23:58:27 2019 | INFO: entering handle_action
Thu Sep 12 23:58:27 2019 | INFO: Created container 63

```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker save -o /tmp/hello.tar joelwking/hello:1.0
```