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
Test the following services

  - getMarket
  - getMarketInfo
  - getSilks
  - getSilksV2
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

response = bf.getMarket(bfpy.ExchangeUK, marketId=101426972)
print response

response = bf.getMarketInfo(bfpy.ExchangeUK, marketId=101426972)
print response

response = bf.getSilks(bfpy.ExchangeUK, markets=[102021854, 102021856])
print response

response = bf.getSilksV2(bfpy.ExchangeUK, markets=[102021854, 102021856])
print response

