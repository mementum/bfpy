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
import sys

import bfpy
import bfpy.bfclient as bfclient
print "forceDirect = %s" % str(bfpy.forceDirect)

print 'Creating a Betfair Client'
bf = bfclient.BfClient(fullDirect=True)
print "fullDirect = %s" % str(bf.fullDirect)
print "directApi = %s" % str(bf.directApi)
print 'Created a Betfair Client'

loginInfo = sys.modules['__main__'].loginInfo

response = bf.login(**loginInfo)
print response

myVendorId=PUT_YOUR_VENDOR_ID_HERE

if False:
    response = bf.createVendorAccessRequest(vendorCustomField='test1', vendorSoftwareId=myVendorId)
    print response

    response = bf.cancelVendorAccessRequest(accessRequestToken=response.accessRequestToken, vendorSoftwareId=myVendorId)
    print response

    response = bf.getVendorAccessRequests(vendorSoftwareId=myVendorId)
    print response

    response = bf.getSubscriptionInfo(vendorSoftwareId=myVendorId, vendorClientId=PUT_CLIENT_ID_HERE)
    print response

    import datetime
    response = bf.updateVendorSubscription(vendorSoftwareId=myVendorId, vendorClientId=PUT_CLIENT_ID_HERE, expiryDate=datetime.datetime.now())
    print response

    response = bf.getSubscriptionInfo(vendorSoftwareId=myVendorId, vendorClientId=PUT_CLIENT_ID_HERE)
    print response

    response = bf.getVendorInfo()
    print response

    response = bf.getVendorUsers(vendorSoftwareId=myVendorId, status='ACTIVE')
    print response
    pass
