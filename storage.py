import init
import json

class Storage:
    def __init__(self):
        self.configuration = init.Initialization().load_configuration()
        self.CONFIG_PATH = init.Initialization().CONFIG_PATH
        self.packages = self.configuration['packages'].split()

    def add_package(self, package):
        """Adds a package to the configuration. This will cause data to
        be collected for the package.

        Parameters:
          package: The package to be added

        Returns: nothing
        """
        if package not in self.packages:
            self.packages.append(package)
            self.write_packages(self.packages)

    def remove_package(self, package):
        """Removes a package from the configuration. This will cause data
        to stop being collected for the package.

        Parameters:
          package: The package to be removed

        Returns: nothing
        """
        if package in self.packages:
            self.packages.remove(package)
            self.write_packages(self.packages)

    def write_packages(self, packages):
        """Edits the configuration to include or exclude a package
        from data collection.

        write_package is a common 'back-end' function for use by add_package
        and remove_package. It writes an updated list of packages to the
        configuration file in a JSON format.

        Parameters:
          packages: The new package list

        Returns: nothing
        """
        self.configuration['packages'] = ' '.join(packages)
        json.dump(self.configuration, open(self.CONFIG_PATH, 'w'))
