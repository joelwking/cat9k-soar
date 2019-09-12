README
------


```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker build -f ./hello_phantom/Dockerfile -t  joelwking/hello:0.9 .
```
```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker run -it --name hello joelwking/hello:0.9
Wed Sep 11 20:16:47 2019 | INFO: hello.py .99
Wed Sep 11 20:16:47 2019 | INFO: use CTRL + c to exit!
Wed Sep 11 20:16:47 2019 | INFO: HELLO
Wed Sep 11 20:16:47 2019 | INFO: entering handle_action
Wed Sep 11 20:16:47 2019 | INFO: Created container 52
administrator@olive-iron:~/docker/cat9k-soar/library$
```

```
administrator@olive-iron:~/docker/cat9k-soar/library$ docker save -o hello.tar joelwking/hello:0.9
```