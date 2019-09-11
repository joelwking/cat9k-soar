#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  11 September 2019
#
#     description: hello.py
#

from base_connector import SOAR

try:
    from hello_constants import *                          # file name would be ./hello_consts.py
except Importerror                                         # the constants are optional
    pass

class Hello(SOAR):

       BANNER = "HELLO"

    def __init__(self):
        """
        Instance variables
        """
        # Call the SOAR init first
        super(Hello, self).__init__()

    def handle_action(self):
        """
        """
        self.msg('INFO: entering handle_action')
        phantom = self.create_phantom_object(self.args.get('phantom').get('public_ip'), self.args.get('phantom').get('ph_auth_token'))

        container = dict(name='Cat9K', description='Code-for-Catalyst challenge', tags=['hello', 'demo'])
        self.create_phantom_container(phantom, **container)


# =============================================================================================
# 
# =============================================================================================

if __name__ == '__main__':

    import sys

    connector = Hello()
    connector.msg(connector.BANNER)
    connector.handle_action()

    exit(0)    
