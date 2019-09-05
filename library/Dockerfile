#
#     Copyright (c) 2019 World Wide Technology, LLC
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  4 September 2019
#
FROM ubuntu:16.04

MAINTAINER @joelwking

LABEL version=".99" description="Code for Catalyst"

#
# Install software
#
RUN apt-get update && apt-get install -y python-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install snort
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python
RUN pip install requests
RUN pip install pyyaml
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install vim

#
# Add the Snort local.rules and the configuration file
#
COPY ./snort.conf /etc/snort/snort.conf
COPY ./local.rules /etc/snort/rules/local.rules

#
# Add Python code and configuration file
#
RUN mkdir -p /app
COPY parse_alerts.* /app/
ADD https://raw.githubusercontent.com/joelwking/Phantom-Cyber/master/REST_ingest/PhantomIngest.py /app/PhantomIngest.py
WORKDIR /app

#
# Environment variables
#
ENV INTERFACE eth0

#
# Execution
#
CMD ["/bin/bash", "parse_alerts.sh"]