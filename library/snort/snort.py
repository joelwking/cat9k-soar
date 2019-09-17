#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, LLC
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  9 September 2019
#
#     description: Tails a Snort Alert file (CSV) and creates Phantom containers and artifacts
#
# 
# Import the SOAR class from the base_connector.py file
#
from base_connector import SOAR
#
# Optionally import user defined constants from hello_constants.py
#
try:
    from snort_constants import *
except ImportError:
    pass

class Snort(SOAR):

    BANNER = "SNORT"

    def __init__(self):
        """
            Call the SOAR init first
        """
        
        super(Snort, self).__init__()


    def tail(self, file_):
        """
            Listen for new lines added to file refer to: http://lethain.com/tailing-in-python/
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
                self.tail(file_)

    
    def process_alert(self, phantom, line):
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

        if self.args.get('msg_tag') in alert.get('msg'):
            if len(keys) != len(value):
                self.msg('WARN: length of keys does not match CSV values provided, ignoring record: {}'.format(value))
                return
            else:
                self.create_phantom_container(phantom, dict(name=self.args.get('msg_tag'), description='Code-for-Catalyst', tags=['snort']))

                artifact = dict(name=alert.get('msg'),
                                source_data_identifier='{}:{}'.format(alert.get('sig id'), alert.get('sig rev')),
                                description='DESCRIPTION',
                                tags=['snort', 'demo']
                                )

                cef = dict(sourceAddress=alert.get('src'),
                           sourcePort=alert.get('srcport'),
                           smac=alert.get('ethsrc'),
                           destinationAddress=alert.get('dst'),
                           destinationPort=alert.get('dstport'),
                           dmac=alert.get('ethdst'),
                           proto=alert.get('proto')
                           )

                return self.create_phantom_artifact(phantom, artifact=artifact, cef=cef, meta_data=dict(record=alert))
        return



    def handle_action(self):
        """
            Create a Phantom object loaded with the IP and credentials from the configuration file
            Open the Snort alert file (CSV format) 
            As lines are added to the file, process them
        """
        self.msg('INFO: entering handle_action')

        phantom = self.create_phantom_object(self.args.get('phantom').get('public_ip'), self.args.get('phantom').get('ph_auth_token'))

        with open(self.args.get('alert_csv', '/var/log/snort/alert.csv'), 'r') as alert_file:
            for EOF, line in self.readlines_then_tail(alert_file):
                if EOF:
                    self.process_alert(phantom, line)
                else:
                    pass

        return



if __name__ == '__main__':
    """
        Instanciate an instance of the Snort class and invoke the main logic
    """

    connector = Snort()
    connector.handle_action()

    exit(0)    
