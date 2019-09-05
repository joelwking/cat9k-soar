#!/bin/bash
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  4 September 2019
#
#  Start Snort in the background
#
snort -q -i echo ${INTERFACE}  -c /etc/snort/snort.conf -K ascii > /dev/null 2>&1 &
#
#  Start monitoring the alert file
#
python2.7 parse_alerts.py ./parse_alerts.yml
