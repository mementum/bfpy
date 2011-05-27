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

  - getBet
  - getBetLite
  - getBetMatchesLite
  - getBetHistory
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

placeBet = bf.createPlaceBets()

placeBet.asianLineId = 0
# Man City = 47999
# Chelsea = 55190
placeBet.selectionId = 55190

placeBet.price = 500.0
placeBet.size = 2.0
placeBet.bspLiability = 0.0

placeBet.betType = 'B'
placeBet.betCategoryType = 'E'

placeBet.betPersistenceType = 'NONE'

# English Premier League Winner 2011/2012
placeBet.marketId = 102817643

response = bf.placeBets(bfpy.ExchangeUK, bets=[placeBet])
print response

betId=response.betResults[0].betId

response = bf.getBet(bfpy.ExchangeUK, betId=betId)
print response

response = bf.getBetLite(bfpy.ExchangeUK, betId=betId)
print response

response = bf.getBetMatchesLite(bfpy.ExchangeUK, betId=betId)
print response

response = bf.cancelBetsByMarket(bfpy.ExchangeUK, markets=[102817643])
print response

response = bf.getBetHistory(bfpy.ExchangeUK, betTypesIncluded='M')
print response

