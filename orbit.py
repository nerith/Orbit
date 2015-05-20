#!/usr/bin/env python3
#
# orbit gives an overview of packages in the Debian Continuous
# Integration project (ci.debian.net).

import sys
import init

if len(sys.argv) < 2 or sys.argv[1] == 'help':
    print('usage: orbit <command>')
    print('''Commands:
    add <package>     Adds a package for data collection
    collect           Collects data from a debci instance
    init              Initializes orbit
    packages          Lists all packages that are being collected
    remove <package>  Removes a package from data collection
    ''')
    sys.exit(1)

option = sys.argv[1]

if option == 'add':
    pass
elif option == 'collect':
    pass
elif option == 'init':
    init.Initialization().create_configuration()
elif option == 'packages':
    pass
elif option == 'remove':
    pass
else:
    print('Unknown command. Run `orbit help` for available commands.')
