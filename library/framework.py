#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  9 September 2019
#
#     description: framework.py
#
# from framework.base_connector import SOAR
from base_connector import SOAR

from framework_constants import *                  # file name would be ./framework_consts.py

class Snort(SOAR):

    BANNER = "SNORT"

    def __init__(self):
        """
        Instance variables
        """
        # Call the SOAR init first
        super(Snort, self).__init__()

    def _test_connectivity(self, arg):
        """
        Test connecitivity to the Phantom instance
        """
        self.msg('INFO: entering _test_connectivity')
        return None

    def handle_action(self, arg):
        """
        """
        self.msg('INFO: entering handle_action')
        return None


# =============================================================================================
# 
# =============================================================================================

if __name__ == '__main__':

    import sys

    connector = Snort()
    connector.msg('Hello world')
    connector.msg(connector.BANNER)
    ret_val = connector._test_connectivity(None)
    ret_val = connector.handle_action(None)

    exit(0)    