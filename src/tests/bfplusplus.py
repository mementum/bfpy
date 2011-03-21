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
Test the services used by bfplusplus for the directApi
'''

import sys

import bfpy
import bfpy.bfclient as bfclient

print 'Creating a Betfair Client'
bf = bfclient.BfClient(fullDirect=True)
print 'Created a Betfair Client'

loginInfo = sys.modules['__main__'].loginInfo

response = bf.login(**loginInfo)
print response

response = bf.keepAlive()
print response

if False:

    response = bf.keepAlive()
    print response
    
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

    response = bf.getMarket(bfpy.ExchangeUK, marketId=101426972)
    print response

    longTermId=101426972
    # Chelsea = 55190
    response = bf.getMarketPricesCompressed(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getCompleteMarketPricesCompressed(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getMarketTradedVolumeCompressed(bfpy.ExchangeUK, marketId=longTermId)
    print response

    response = bf.getMarketProfitAndLoss(bfpy.ExchangeUK, marketId=longTermId)
    print response

    longTermId=101426972
    response = bf.getMUBets(bfpy.ExchangeUK, marketId=0, betStatus='MU', betIds=[11607664129])
    print response


    placeBet = bf.createPlaceBets()
    placeBet.asianLineId = 0
    placeBet.betType = 'B'
    placeBet.betPersistenceType = 'IP'
    placeBet.marketId = 102401756
    placeBet.price = 20.0
    placeBet.selectionId = 2426
    placeBet.size = 4.0

    bf.placeBets(bfpy.ExchangeUK, bets=[placeBet])
    print response

    cancelBet = bf.createCancelBets()
    cancelBet.betId = 14068925024
    bf.cancelBets(bfpy.ExchangeUK, bets=[cancelBet])
    print response


    updateBet = bf.createUpdateBets()
    updateBet.betId = 14069265023
    updateBet.newPrice = 30.0
    updateBet.newSize = 4.0
    updateBet.oldPrice = 20.0
    updateBet.oldSize = 4.0
    updateBet.newBetPersistenceType = 'IP'
    updateBet.oldBetPersistenceType = 'IP'
    bf.updateBets(bfpy.ExchangeUK, bets=[updateBet])
    print response

sys.exit(0)
