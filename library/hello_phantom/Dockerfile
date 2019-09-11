#
#     Copyright (c) 2019 World Wide Technology, LLC
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  11 September 2019
#
#     usage:
#
#       from directory `cat9k-soar/library`
#       docker build -f ./hello_phantom/Dockerfile -t  joelwking/hello:0.9 .
#
FROM ubuntu:16.04

MAINTAINER @joelwking

LABEL version=".99" description="Code for Catalyst, hello Phantom"

#
# Install software
#
RUN apt-get update && apt-get install -y python-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python
RUN pip install requests
RUN pip install pyyaml
#
# Remove vim once debugging is complete
#
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install vim
#
# Add Python code and configuration file
#
RUN mkdir -p /app
COPY ./hello_phantom/* /app/
COPY ./connector/*.py /app/
ADD https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/REST_ingest/PhantomIngest.py /app/PhantomIngest.py
WORKDIR /app
#
# Execution
#
CMD ["python2.7", "hello.py"]