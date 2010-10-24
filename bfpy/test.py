#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-

import sys

class flushfile(object):

    def __init__(self, f):
        self.f = f

    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stdout = flushfile(sys.stdout)
sys.stderr = flushfile(sys.stderr)

# Place a file with the following content:
# dict(username=yourusername, password=yourpassword, productId=yourProductId, vendorSoftwareId=yourVendorSoftwareId)

print 'Reading Credentials'
testInfoFile = open('../../testInfo')
loginInfo = eval(testInfoFile.readline().rstrip())
testInfoFile.close()
print 'Read Credentials'

print 'Testing Modules'
for arg in sys.argv[1:]:
    print '---------- Testing module: %s ------------' % arg
    __import__('tests.' + arg)
    print '---------- Tested module: %s ------------' % arg
print 'Tested Modules'
