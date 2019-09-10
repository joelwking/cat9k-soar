#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  9 September 2019
#
#     description: snort.py
#
# from framework.base_connector import SOAR
from base_connector import SOAR

try:
    from snort_constants import *                          # file name would be ./framework_consts.py
except Importerror                                         # the constants are optional
    pass

class Snort(SOAR):

    BANNER = "SNORT"

    def __init__(self):
        """
        Instance variables
        """
        # Call the SOAR init first
        super(Snort, self).__init__()


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

        if args.get('msg_tag') in alert.get('msg'):                                    # searching for '__I_' in the alert file
            if len(keys) != len(value):
                msg('WARN: length of keys does not match CSV values provided, ignoring record: {}'.format(value))
                return
            else:
                self.create_phantom_container(phantom)

                artifact = dict(name=alert.get('msg'),
                                source_data_identifier='{}:{}'.format(alert.get('sig id'), alert.get('sig rev')),
                                description='Code-for-Catalyst challenge',
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
        """
        self.msg('INFO: entering handle_action')
        #
        # Tail the Snort Alert file (in CSV format) process only new records
        #
        phantom = create_phantom_object(args.get('phantom').get('public_ip'), args.get('phantom').get('ph_auth_token'))

        with open(args.get('alert_csv', '/var/log/snort/alert.csv'), 'r') as alert_file:
            for EOF, line in self.readlines_then_tail(alert_file):
                if EOF:
                    self.process_alert(phantom, line)
                else:
                    pass

        return


# =============================================================================================
# 
# =============================================================================================

if __name__ == '__main__':

    import sys

    connector = Snort()
    connector.msg(connector.BANNER)
    connector.handle_action()

    exit(0)    
