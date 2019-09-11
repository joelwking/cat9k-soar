#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  11 September 2019
#
#     description: Hello World skeleton program to demonstrate creating a container on Phantom Cyber
#
#
# Import the SOAR class from the base_connector.py file
#
from base_connector import SOAR
#
# Optionally import user defined constants from hello_constants.py
#
try:
    from hello_constants import *
except ImportError:
    pass


class Hello(SOAR):

    BANNER = "HELLO"

    def __init__(self):
        """
            Instance variables
        """

        super(Hello, self).__init__()                      # Call the SOAR init first


    def handle_action(self):
        """
            This method calls the 'msg' method from class SOAR in the base_connector. During initialization, the SOAR class 
            has read the YAML configuration file to obtain the Phantom IP and token for authentication. 
            We create and tage a container in Phantom, and exit.
        """
        self.msg('INFO: entering handle_action')
        phantom = self.create_phantom_object(self.args.get('phantom').get('public_ip'), self.args.get('phantom').get('ph_auth_token'))

        container = dict(name='Hello_World', description='Code-for-Catalyst challenge', tags=['hello', 'demo'])
        self.create_phantom_container(phantom, container)


if __name__ == '__main__':

    import sys

    connector = Hello()
    connector.msg('INFO: {}'.format(connector.BANNER))
    connector.handle_action()

    exit(0)
