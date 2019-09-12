#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     Copyright (c) 2019 World Wide Technology, Inc.
#     All rights reserved.
#
#     author: joel.king@wwt.com (@joelwking)
#     written:  3 September 2019
#
#     description: TODO
#
# Application imports
#
import PhantomIngest as ingest

# System imports
#
import yaml
import time
import sys
import signal


class SOAR(object):

    __version__ = '1.0'
    ERROR = 'ERROR'

    def __init__(self):
        """
        """
        self.version = SOAR.__version__
        self.enable_interrupts()
        self.args = self.load_configuration()


    def msg(self, text):
        """
            Generate status messages, exit if the message begins with ERROR
        """
        print('{} | {}'.format(time.asctime(), text))
        if SOAR.ERROR in text[0:len(SOAR.ERROR)]:
            sys.exit()

        return


    def enable_interrupts(self):
        """
        #
        #  Interrupts
        #
        """
        self.msg("INFO: {} {}".format(sys.argv[0], SOAR.__version__))
        signal.signal(signal.SIGINT, self.sig_handler)              # Enable Interrupt handler
        signal.signal(signal.SIGTERM, self.sig_handler)             # Enable TERM handler
        self.msg('INFO: use CTRL + c to exit!')


    def sig_handler(self, signum, frame):
        """
            Handle signal interrupts.
        """
        self.msg('INFO: interrupt {} caught, exiting.'.format(signum))
        sys.exit()

    
    def load_configuration(self, configuration='{}.yml'.format(sys.argv[0].split('.')[0])):
        """
            The configuration file is stored in a .yml file in the same directory as this program
            Include the configuration file, either user specified or use the default
        """
        
        try:
            configuration = sys.argv[1]
        except IndexError:
            pass

        with open(configuration, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as e:
                self.msg('{}: error {} loading YAML file: {}'.format(SOAR.ERROR, e, configuration))

        return config

    def test_connectivity(self):
        """
        Test connecitivity to the Phantom instance
        """
        self.msg('INFO: entering test_connectivity')
        return None


    def create_phantom_object(self, server='192.0.2.1', token=None):
        """
            Instanciate an instance of the object, returning the object.
        """
        return ingest.PhantomIngest(server, token)


    def create_phantom_artifact(self, phantom, artifact=dict(), cef=dict(), meta_data=dict()):
        """
            Add the Snort alert as an artifact to the Phantom container, CEF is Common Event Format.
            Refer to https://<phantom>/docs/rest/cef for the valid fields.
        """
        artifact_id = None

        try:
            artifact_id = phantom.add_artifact(phantom.container_id, cef, meta_data, **artifact)
            self.msg('INFO: Added artifact: {} to container: {}'.format(artifact_id, phantom.container_id))
        except Exception as e:
            self.msg('WARN: exception while adding artifact {} {}'.format(e, phantom.content))

        return artifact_id

    def create_phantom_container(self, phantom, container=dict()):
        """
            Input is a dictionary with input to create the container
        """

        if phantom.container_id:
            # a container already exists, simply return the existing container_id
            return phantom.container_id

        try:
            phantom.add_container(**container)
            self.msg('INFO: Created container {}'.format(phantom.container_id))
        except AssertionError as e:
            self.msg('{}: Any HTTP return code other than OK {}'.format(ERROR, e))            
        except Exception as e:
            self.msg('{}: Phantom host did not respond, a connection error {}'.format(ERROR, e))

        return phantom.container_id