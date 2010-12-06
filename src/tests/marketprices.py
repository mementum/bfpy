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

  - getMarketPrices
  - getMarketPricesCompressed
  - getMUBets
  - getMUBetsLite
  - getMarketProfitAndLoss
  - getCompleteMarketPricesCompressed
  - getMarketTradedVolume
  - getMarketTradedVolumeCompressed
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

# English Premier League Winner 2010/11
longTermId=101426972
# Chelsea = 55190

response = bf.getMarketPrices(bfpy.ExchangeUK, marketId=longTermId)
print response

response = bf.getMarketPricesCompressed(bfpy.ExchangeUK, marketId=longTermId)
print response

response = bf.getMUBets(bfpy.ExchangeUK, marketId=longTermId, betStatus='MU')
print response

response = bf.getMUBetsLite(bfpy.ExchangeUK, marketId=longTermId, betStatus='MU')
print response

response = bf.getMarketProfitAndLoss(bfpy.ExchangeUK, marketId=longTermId)
print response

response = bf.getCompleteMarketPricesCompressed(bfpy.ExchangeUK, marketId=longTermId)
print response

response = bf.getDetailAvailableMarketDepth(bfpy.ExchangeUK, marketId=longTermId, selectionId=55190)
print response

response = bf.getMarketTradedVolume(bfpy.ExchangeUK, marketId=longTermId, selectionId=55190)
print response

response = bf.getMarketTradedVolumeCompressed(bfpy.ExchangeUK, marketId=longTermId)
print response
