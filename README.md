#Orbit
Orbit enables data collection of packages from
<a href='http://ci.debian.net'>ci.debian.net</a>.

## Getting Started
To get started, add the location of this directory to your PATH
and run `chmod +x orbit`.

Once that is done, install Python 3. On a Debian based system, run
`sudo apt-get install python3` to install Python 3. Once you have
Python 3 installed, run `orbit init` to generate a basic config file.

## Configuration
The basic config file contains the url to obtain data from
(default: ci.debian.net) and the packages that should have their data
requested from ci.debian.net.

By default, the configuration contains no packages for data collection.
To start getting data collected for your packages, run `orbit add <packages>`.

Likewise, if you want to remove a package from data collection, run
`orbit remove <packages>`.

Once you are done adding packages to Orbit, you can start
collecting the status of each package by running `orbit collect`.

## Checking for packages
To check which packages Orbit is collecting, run `orbit packages`.
