# we may find ourselves developing on one platform then running on another
# we can find out about the operating system, the hardware and the nevironment

import sys

print(sys.platform)
print(sys.version)
sys.path.append('d:') # we can add places for Python to look when importing
paths = sys.path # a list of places Python will look for imports

for path in paths:
    print(path)

# this tells us the size of float that Python can handle
print(sys.float_info)

import os
print(os.name)