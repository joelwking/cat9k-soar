#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  3 September 2019
#
#     description: create Phantom Cyber containers and artifacts from a Snort alert file
#
#     usage:
#
#        $ python2.7 parse_alerts.py <parse_alerts.yml>
#
#     The rule file for Snort has entries which look like the following:
#
#        alert tcp any any -> any 80 (tos:184; sid:1000985; msg: "__S_tcp80";)
#        alert tcp any any -> any 443 (tos:184; sid:1000986; msg: "__S_tcp443"
#        alert tcp 192.168.0.0/16 any -> any 25 (content: "hacking"; msg: "__S_tcp25_hacking"; sid:1000987;)
#
#     The configuration file is in YAML, and specifies what records to select from the Snort alert file
#     based on the message tag (msg_tag). These alerts are then loaded to Phantom Cyber using the REST API.
#
__version__ = '.99'
SLEEP_INTERVAL = .333                                      # a fraction of a second
ERROR = 'ERROR'


#
# System imports
#
import yaml
import time
import sys
import signal


class SOAR(object):

    def __init__(self):

    def tail(self, file_):
        """
            Listen for new lines added to file.
            http://lethain.com/tailing-in-python/
        """

        while True:
            where = file_.tell()
            line = file_.readline()
            if not line:
                time.sleep(SLEEP_INTERVAL)
                file_.seek(where)
            else:
                yield line


    def readlines_then_tail(self, file_):
        """
            Iterate through lines and then tail for further lines.
        """
        EOF = False
        while True:
            line = file_.readline()
            if line:
                yield (EOF, line)
            else:                                              # Only start pushing flows for the appended lines
                EOF = True                                     # We don't proccess entries in the file until we call tail
                tail(file_)


    def process_alert(self, line, phantom, args):
        """
            Input is a Snort alert record, in CSV format
            Credit to: https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
            sample input:

            line = '09/03-15:20:34.587699 ,1,1000001,1,"__S_ICMP_cat9Ktest",ICMP,172.17.0.1,,172.17.0.2,,02:42:38:29:34:91,02:42:AC:11:00:02,0x62,,,,,,64,0,65339,84,86016,8,0,10379,1'
        """
        value = line.split(',')
        keys = ('timestamp', 'sig generator', 'sig id', 'sig rev', 'msg', 'proto', 'src', 'srcport', 'dst', 'dstport', 'ethsrc', 'ethdst', 'ethlen',
                'tcpflags', 'tcpseq', 'tcpack', 'tcplen', 'tcpwindow', 'ttl', 'tos', 'id', 'dgmlen', 'iplen', 'icmptype', 'icmpcode', 'icmpid', 'icmpseq')

        alert = {keys[i]: value[i] for i in range(len(value))}

        if args.get('msg_tag') in alert.get('msg'):                                    # searching for '__I_' in the alert file
            if len(keys) == len(value):
                update_phantom(alert, phantom)
            else:
                msg('WARN: length of keys does not match CSV values provided, ignoring record: {}'.format(value))
        return


    def monitor():
        """
            Main program
        """

        #
        # Tail the Snort Alert file (in CSV format) process only new records
        #
        with open(args.get('alert_csv','/var/log/snort/alert.csv'), 'r') as alert_file:
            for EOF, line in readlines_then_tail(alert_file):
                if EOF:
                    process_alert(line, phantom, args)
                else:
                    pass

        return