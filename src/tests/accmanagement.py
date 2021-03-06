#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
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
Test the following services

  - viewReferAndEarn
'''
import sys

import bfpy
import bfpy.bfclient as bfclient

print 'Creating a Betfair Client'
bf = bfclient.BfClient()
print 'Created a Betfair Client'

loginInfo = sys.modules['__main__'].loginInfo

response = bf.login(**loginInfo)
print response

response = bf.getAccountStatement(bfpy.ExchangeUK)
print response

# Possibly a full set of fields is needed and not just one field
# response = bf.modifyProfile(password='yourPass', homeTelephone='aTelephone')
# print response

response = bf.modifyPassword(password=loginInfo['password'], newPassword='newPass123456', newPasswordRepeat='newPass123456')
print response

response = bf.modifyPassword(password='newPass123456', newPassword=loginInfo['password'], newPasswordRepeat=loginInfo['password'])
print response

response = bf.getSubscriptionInfo()
print response

response = bf.viewProfile()
print response

response = bf.viewReferAndEarn()
print response
