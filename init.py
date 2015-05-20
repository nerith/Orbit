#!/usr/bin/env python3

import os
import json

class Initialization:
    def __init__(self):
        self.CONFIG_PATH = '/'.join([os.path.dirname(__file__), 'config.json'])

    def create_configuration(self):
        """Creates the default configuration file.

        Parameters: none
        Returns:    nothing
        """
        configuration = {'instance' : 'http://ci.debian.net', 'packages' : ''}
        with open(self.CONFIG_PATH, 'w') as conf:
            json.dump(configuration, conf)

    def load_configuration(self):
        """Loads the configuration file.

        Parameters: none
        Returns:    the current configuration
        """
        with open(self.CONFIG_PATH, 'r') as conf:
            current_config = json.load(conf)

        return current_config
