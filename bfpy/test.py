#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010  Daniel Rodriguez (aka Daniel Rodriksson)
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfpy/
#
# BfPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BfPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
Base test script that imports modules (given in the command line argument)
from the test directory
'''

import sys

class flushfile(object):
    '''
    Class to flush stdout and stderr instantly
    '''
    def __init__(self, f):
        self.f = f

    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stdout = flushfile(sys.stdout)
sys.stderr = flushfile(sys.stderr)

# The credentials file "testInfo" has only 1 line
# The same information can be put directly into loginInfo variable
# dict(username=yourusername, password=yourpassword, productId=yourProductId, vendorSoftwareId=yourVendorSoftwareId)

print 'Reading Credentials'
testInfoFile = open('../../testInfo')
loginInfo = eval(testInfoFile.readline().rstrip())
testInfoFile.close()
print 'Read Credentials'

print 'Testing Modules'
for arg in sys.argv[1:]:
    print '---------- Testing module: %s ------------' % arg
    modName = 'tests.' + arg
    __import__(modName)
    del sys.modules[modName]
    print '---------- Tested module: %s ------------' % arg
print 'Tested Modules'
