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

  - placeBets
  - updateBets
  - cancelBets
'''
import sys
import time

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
# Man City
placeBet.selectionId = 47999

placeBet.price = 500.0
placeBet.size = 2.0
placeBet.bspLiability = 0.0

placeBet.betType = 'B'
placeBet.betCategoryType = 'E'

placeBet.betPersistenceType = 'NONE'

# English Premier League Winner 2010/2011
placeBet.marketId = 101426972

response = bf.placeBets(bfpy.ExchangeUK, bets=[placeBet])
print response


print 'sleeping 5 seconds'
time.sleep(5)

bet = response.betResults[0]

updateBet = bf.createUpdateBets()

updateBet.betId = bet.betId
updateBet.newBetPersistenceType = 'NONE'
updateBet.newPrice = 1000.0
updateBet.newSize = 2.0

updateBet.oldBetPersistenceType = 'NONE'
updateBet.oldPrice = 500.0
updateBet.oldSize = 2.0

response = bf.updateBets(bfpy.ExchangeUK, bets=[updateBet])
print response

print 'sleeping 5 seconds'
time.sleep(5)

bet = response.betResults[0]

cancelBet = bf.createCancelBets()
cancelBet.betId = bet.newBetId

response = bf.cancelBets(bfpy.ExchangeUK, bets=[cancelBet])
print response


