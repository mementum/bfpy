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
Test the services used by bfplusplus for the directApi
'''

import time
import sys

import bfpy
import bfpy.bfclient as bfclient

print 'Creating a Betfair Client'
bf = bfclient.BfClient(fullDirect=True)
print 'Created a Betfair Client'

loginInfo = sys.modules['__main__'].loginInfo

response = bf.login(**loginInfo)
print response

if True:

    response = bf.keepAlive()
    print response

    # Re-Login with the same details
    response = bf.login()
    print response

    response = bf.logout()
    print response

    # Re-Login after logout
    response = bf.login()
    print response

    response = bf.getActiveEventTypes()
    print response

    # Barclays PremierShip - includes eventItems and marketSummaryItems
    response = bf.getEvents(eventParentId=2022802)
    print response

    response = bf.getAllMarkets(bfpy.ExchangeUK, eventTypeIds=[136332, 998919])
    print response

    response = bf.getAccountFunds(bfpy.ExchangeUK)
    print response

    response = bf.transferFunds(sourceWalletId=bfpy.ExchangeUK,
                                targetWalletId=bfpy.ExchangeAus,
                                amount=0.50)
    print response

    response = bf.transferFunds(sourceWalletId=bfpy.ExchangeAus,
                                targetWalletId=bfpy.ExchangeUK,
                                amount=0.50)
    print response

    response = bf.getCurrentBets(bfpy.ExchangeUK, betStatus='M')
    print response

    longTermId = 102817643 # Barclays Premiership 2011/2012
    longTermRunnerId = 55190 # Chelsea
    response = bf.getMarket(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getMarketPricesCompressed(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getCompleteMarketPricesCompressed(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getMarketTradedVolumeCompressed(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getMarketProfitAndLoss(bfpy.ExchangeUK, marketId=longTermId)
    print response

    placeBet = bf.createPlaceBets()
    placeBet.asianLineId = 0
    placeBet.betType = 'B'
    placeBet.betCategoryType = 'E'
    placeBet.betPersistenceType = 'NONE'
    placeBet.marketId = longTermId
    placeBet.price = 500.0
    placeBet.selectionId = longTermRunnerId
    placeBet.size = 2.0

    response = bf.placeBets(bfpy.ExchangeUK, bets=[placeBet])
    print response

    time.sleep(5.0)
    updateBet = bf.createUpdateBets()
    updateBet.betId = response.betResults[0].betId
    updateBet.newPrice = 1000.0
    updateBet.newSize = 2.0
    updateBet.oldPrice = 500.0
    updateBet.oldSize = 2.0
    updateBet.newBetPersistenceType = 'NONE'
    updateBet.oldBetPersistenceType = 'NONE'
    response = bf.updateBets(bfpy.ExchangeUK, bets=[updateBet])
    print response

    newBetId = response.betResults[0].newBetId

    response = bf.getMUBets(bfpy.ExchangeUK, marketId=longTermId, betStatus='MU')
    print response

    time.sleep(5.0)
    cancelBet = bf.createCancelBets()
    cancelBet.betId = newBetId
    response = bf.cancelBets(bfpy.ExchangeUK, bets=[cancelBet])
    print response

sys.exit(0)
