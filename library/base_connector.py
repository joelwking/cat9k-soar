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
# Application imports
#
import PhantomIngest as ingest
#
# programatially import
#
import importlib
agent = importlib.import_module('time')
# agent
# agent.asctime()

# System imports
#
import yaml
import time
import sys
import signal


class SOAR(object):

    __version__ = '.99'
    ERROR = 'ERROR'

    def __init__(self):
        """
        """
        self.version = SOAR.__version__


    def msg(self, text):
        """
            Generate status messages, exit if the message begins with ERROR
        """
        print('{} | {}'.format(time.asctime(), text))
        if SOAR.ERROR in text[0:len(SOAR.ERROR)]:
            sys.exit()

        return


    def sig_handler(self, signum, frame):
        """
            Handle signal interrupts.
        """
        self.msg('INFO: interrupt {} caught, exiting.'.format(signum))
        sys.exit()

