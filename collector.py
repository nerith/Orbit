import init
import urllib.request
import os
import json
import re

class Collector:
    def __init__(self):
        self.url = init.Initialization().load_configuration()['instance']

    def load_packages(self):
        """Loads package names from the configuration file.

        After running, the package names will be loaded and will be usable
        for checking the status of a package.

        Parameters: none
        Returns: nothing
        """
        packages = []

        try:
            with open(os.path.dirname(os.path.realpath(__file__)) +
                      "/config.json", 'r') as conf:
                data = json.load(conf)
                packages = [ package for package in data['packages'].split() ]
        except IOError:
            print('Error:   Configuration file does not exist.')
            print('\tCreate it by running orbit init.')
        except ValueError:
            print('Configuration JSON is invalid.')
            sys.exit(1)

        return packages

    def get_status(self, suite, architecture, package):
        """Returns the status of a package in the testing system

        Parameters:
          suite:        The suite
          architecture: The architecture
          package:      The name of the package

        Returns: nothing
        """
        url = '/'.join([self.url, 'data/packages'])
        url = '/'.join([url, suite, architecture, self.get_prefix(package),
                    package, 'latest.json'])

        form = "%-20s %-7s"

        try:
            data = urllib.request.urlopen(url)
        except urllib.request.HTTPError:
            print(form % (package, 'No data'))
            return 'No data'
        except urllib.error.URLError:
            print('URL not available')
            sys.exit(1)

        jsn = ''.join([ line.decode('utf-8') for line in data])
        status = json.loads(jsn)['status']

        print(form % (package, status))

    def get_prefix(self, package):
        """Returns the prefix for a package name

        Parameters:
          package: The package name

        Returns: the prefix for a package name
        """
        return re.match(r'lib[a-z]|[0-9a-z]{1,1}', package).group()
