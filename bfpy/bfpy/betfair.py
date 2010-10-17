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

from copy import deepcopy
from datetime import datetime
from collections import defaultdict
from operator import attrgetter

import bfapi
import bferror
from timezone import GMT, LocalTimezone
from util import EmptyObject

MinBet = 2.00

class Betfair(bfapi.BfApi):
    '''
    The Betfair object processes Betfair API answers (if needed) and decompresses
    compressed answers into usable objects

    It does also save necessary information to performa relogin
    '''

    def __init__(self, **kwargs):
        '''
        Constructor. Call the parent BfApi constructor and initialize the variables
        that will allow session login management

        @param kwargs: standard Python keywords arguments
        @type kwargs: dict

        @returns: a constructed object
        @rtype: Betfair
        '''
        bfapi.BfApi.__init__(self, **kwargs)

        self.username = None
        self.password = None
        self.productId = 0
        self.vendorSoftwareId = 0

    ############################################################
    # API Object Creation
    ############################################################
    def CreateMarket(self):
        '''
        Helper to create a suds "Market" object

        @returns: a Market object
        @rtype: suds object
        '''
        return self.GetObjectExchange('Market')


    def CreateRunner(self):
        '''
        Helper to create a suds "Runner" object

        @returns: a Runner object
        @rtype: suds object
        '''
        return self.GetObjectExchange('Runner')


    def CreateMarketPrices(self):
        '''
        Helper to create a suds "Market Prices" object

        @returns: a Market Prices object
        @rtype: suds object
        '''
        return self.GetObjectExchange('MarketPrices')


    def CreateRunnerPrices(self):
        '''
        Helper to create a suds "Runner Prices" object

        @returns: a Runner Prices object
        @rtype: suds object
        '''
        return self.GetObjectExchange('RunnerPrices')


    def CreatePrice(self):
        '''
        Helper to create a suds "Price" object

        @returns: a Price object
        @rtype: suds object
        '''
        return self.GetObjectExchange('Price')


    def CreateEvent(self, eventId=-1, eventName=''):
        '''
        Helper to create a suds "Event" object

        @param eventId: id of the event
        @type eventId: int
        @param eventName: name of the event
        @type eventName: str

        @returns: a Event object
        @rtype: suds object
        '''
        # event = self.GetObjectGlobal('BFEvent')
        event = EmptyObject()
        event.eventId = eventId
        event.eventName = eventName
        return event


    def CreatePlaceBet(self):
        '''
        Helper to create a suds "PlaceBet" object

        @returns: a PlaceBet object
        @rtype: suds object
        '''
        return self.GetObjectExchange('PlaceBets')


    def CreateCancelBet(self):
        '''
        Helper to create a suds "CancelBet" object

        @returns: a CancelBet object
        @rtype: suds object
        '''
        return self.GetObjectExchange('CancelBets')


    def CreateUpdateBet(self):
        '''
        Helper to create a suds "UpdateBet" object

        @returns: a UpdateBet object
        @rtype: suds object
        '''
        return self.GetObjectExchange('UpdateBets')

    ############################################################
    # General Services API Services
    ############################################################

    def Login(self, username, password, productId=82, vendorSoftwareId=0):
        '''
        Login onto the Betfair API. Values are temporarily stored for
        login session management

        @param username: username
        @type username: str
        @param password: password
        @type password: str
        @param productId: type of API access to use
        @type productId: int
        @param vendorSoftwareId: id assigned to software vendors
        @type vendorSoftwareId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        # Invalidate previous credentials
        self.username = None
        self.password = None

        response = bfapi.BfApi.Login(self, username, password, productId, vendorSoftwareId)

        # If not exception was thrown, then login succeeded, store the credentials
        self.username = username
        self.password = password
        self.productId = productId
        self.vendorSoftwareId = vendorSoftwareId

        return response


    def Logout(self):
        '''
        Logout. Invalidates login management data

        @returns: Betfair API answer
        @rtype: suds object
        '''
        # Invalidate credentials before calling the service, since this might fail
        # with an Exception, preventing us from clearing the credentials 
        self.username = None
        self.password = None

        return bfapi.BfApi.Logout(self)


    def ReLogin(self):
        '''
        Attempts to execute Login if the credentials have already been proven right

        @returns: Betfair API answer
        @rtype: suds object

        @raise BfApiError: if no session was active (with NO_SESSION as errorCode)
        '''
        if self.username:
            return self.Login(self.username, self.password, self.productId, self.vendorSoftwareId)
        else:
            raise bferror.BfApiError('ReLogin', 'NO_SESSION', 'No credentials available to relogin')


    ############################################################
    # Read-Only Betting API Services
    ############################################################

    def GetAllCurrencies(self):
        '''
        Get a list of the currencies and the conversion rate to GBP

        Removes indirection of currencyItems

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = bfapi.BfApi.GetRequestObjectGlobal(self, 'GetCurrenciesReq')

        if hasattr(request, 'currencyItems'):
            request.currencyItems = request.currencyItems.Currency
        else:
            request.currencyItems = list()
            
        return self.InvokeRequestGlobal('getAllCurrencies', request);


    def GetAllCurrenciesV2(self):
        '''
        Get a list of the currencies and the conversion rate to GBP
        and the minimum bet for each currency

        Removes indirection of currencyItems

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = bfapi.BfApi.GetRequestObjectGlobal(self, 'GetCurrenciesV2Req')
        if hasattr(request, 'currencyItems'):
            request.currencyItems = request.currencyItems.CurrencyV2
        else:
            request.currencyItems = list()
        return self.InvokeRequestGlobal('getAllCurrenciesV2', request);


    def GetActiveEventTypes(self):
        '''
        Retrieve the list of Active Event Types (top level events)

        Removes one level of idirection for eventTypeItems

        It performs an "eventItemization" of the top level events.

        The reasoning behind this is to let the UI manage only two types of objects:
        -- Events (eventItems)
        -- Markets (marketItems)

        EventTypes have an exchangeId field for Greyhound races and Events have fields
        like menuLevel and orderIndex, but the main fields are actually the same:

        -- id vs eventId
        -- name vs eventName

        @returns: Betfair API answer
        @rtype: suds object
        '''
        # Invoke the plain Api method
        response = bfapi.BfApi.GetActiveEventTypes(self)

        # Remove one level of indirection in the array
        if response.eventTypeItems != None:
            response.eventTypeItems = response.eventTypeItems.EventType
        else:
            response.eventTypeItems = list()

        # Alias the .id and .name attributes to those of an event
        for event in response.eventTypeItems:
            event.eventId = event.id
            event.eventName = event.name

        # Create the eventItems and marketItems alias
        response.eventItems = response.eventTypeItems
        response.marketItems = list()

        # Return the value to the caller
        return response


    def GetAllEventTypes(self):
        '''
        Retrieve the list of all Event Types (top level events)

        Removes one level of idirection for eventTypeItems

        It performs an "eventItemization" of the top level events.

        The reasoning behind this is to let the UI manage only two types of objects:
        -- Events (eventItems)
        -- Markets (marketItems)

        EventTypes have an exchangeId field for Greyhound races and Events have fields
        like menuLevel and orderIndex, but the main fields are actually the same:
        -- id vs eventId
        -- name vs eventName


        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.GetAllEventTypes(self)

        # Remove indirection
        if response.eventTypeItems != None:
            response.eventTypeItems = response.eventTypeItems.EventType
        else:
            response.eventTypeItems = list()

        # Alias the .id and .name attributes to those of an event
        for event in response.eventTypeItems:
            event.eventId = event.id
            event.eventName = event.name

        # Create the eventItems and marketItems alias
        response.eventItems = response.eventTypeItems
        response.marketItems = list()

        return response


    def GetAllMarkets(self, exchangeId):
        '''
        Retrieve a list of objects with all available markets in an exchange.

        The response is compressed and is decompressed into a list of marketItems
        objects

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        # Call the plain Api service
        response = bfapi.BfApi.GetAllMarkets(self, exchangeId)

        # Creat a placeholder for the marketItems to be parsed
        marketItems = list()

        # Parse the marketItems data string
        
        marketDataParts = response.marketData.split(':')
        # First element is always empty ... pop it out because Betfair places a delimiter at the beginning
        marketDataParts.pop(0)

        toSkip = 0
        for i in xrange(len(marketDataParts)):

            if toSkip > 0:
                toSkip -= 1
                continue

            marketItemFields = marketDataParts[i].split('~')
            
            while len(marketItemFields) < 16:
                # 2010-04-04 ... 16 is the number of fields, but the documentation says
                # that there could be more in the future and to parse accordingly
                toSkip += 1

                # The last character of the last field should be a backslash
                # pop out, strip char
                lastField = marketItemFields.pop(len(marketItemFields) - 1).rstrip('\\')
                
                # Get the extra fields needed
                extraFields = marketDataParts[i + toSkip].split('~')

                # join the popped out with the first one, since they were separated by the colon
                # and join them with a colon
                rebuiltField = lastField + ':' + extraFields.pop(0)

                # Re-insert the rebuilt at the end and extend with the extra fields
                marketItemFields.append(rebuiltField)
                marketItemFields.extend(extraFields)

            # Create a generic object and populate it with the market fields
            marketItem = EmptyObject()
            # marketItem = self.GetObjectExchange('Market')

            marketItem.marketId = int(marketItemFields[0])
            marketItem.marketName = marketItemFields[1]
            marketItem.marketType = marketItemFields[2]
            marketItem.marketStatus = marketItemFields[3]
            marketItem.marketTime = datetime.fromtimestamp(long(marketItemFields[4]) / 1000)
            
            menuPathParts = list()
            menuParts = marketItemFields[5].split('\\')
            for menuPart in menuParts:
                menuPathParts.append(menuPart.rstrip())

            # Hack to remove unexistent 'Group X' menu path for the 4 events
            if menuPathParts[1] in ('Tennis', 'Golf', 'Cricket', 'Rugby Union'):
                if 'Group' in menuPathParts[2]:
                    menuPathParts.pop(2)

            marketItem.menuPathParts = menuPathParts
            marketItem.menuPath = '\\'.join(menuPathParts)
            # Save the broken down menupath parts
            marketItem.menuPathParts = menuPathParts
            # Pop the initial empty element from the list
            marketItem.menuPathParts.pop(0)
            
            eventHierarchyStrings = marketItemFields[6].split('/')
            if len(eventHierarchyStrings):
                # if the event hierarchy is not empty
                # skip the leading '/' by popping the empty token
                eventHierarchyStrings.pop(0)

            marketItem.eventHierarchy = list()
            for ident in eventHierarchyStrings:
                marketItem.eventHierarchy.append(long(ident))

            marketItem.delay = int(marketItemFields[7])
            marketItem.exchangeId = int(marketItemFields[8])
            marketItem.countryISO3 = marketItemFields[9]
            marketItem.lastRefresh = datetime.fromtimestamp(long(marketItemFields[10])/1000)
            marketItem.numberOfRunners = int(marketItemFields[11])
            marketItem.numberOfWinners = int(marketItemFields[12])
            marketItem.totalAmountMatched = float(marketItemFields[13])
            marketItem.bspMarket = (marketItemFields[14] == 'Y')
            marketItem.turningInPlay = (marketItemFields[15] == 'Y')
            
            marketItems.append(marketItem)

        response.marketData = marketItems
        return response


    def GetCompleteMarketPricesCompressed(self, exchangeId, marketId):
        '''
        Retrieve the complete market prices (compressed).

        Decompresses the answer into an object

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.GetCompleteMarketPricesCompressed(self, exchangeId, marketId)

        response.completeMarketPrices = self.ParseMarketPricesCompressed(response.completemarketPrices, completeCompressed=True)
        response.completeMarketPrices.runnerPrices = response.completeMarketPrices.runnerPrices.RunnerPrices

        return response


    def GetCurrentBets(self, exchangeId):
        '''
        Retrieve a list of current bets on an exchange, according to betStatus
        marketId and ordered according to orderBy

        Unfortunately passing "MU" fails, so 2 calls have to be made, one to
        get the matched bets and another to get the unmatched bets

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        responseMatched = bfapi.BfApi.GetCurrentBets(self, exchangeId, betStatus='M')

        # Remove one indirection level if possible
        if responseMatched.bets:
            responseMatched.bets = responseMatched.bets.Bet
        else:
            responseMatched.bets = list()

        responseUnmatched = bfapi.BfApi.GetCurrentBets(self, exchangeId, betStatus='U')
        if responseUnmatched.bets:
            responseMatched.bets.extend(responseUnmatched.bets.Bet)

        responseMatched.totalRecordCount += responseUnmatched.totalRecordCount

        # Alias to standard response
        response = responseMatched

        # Sort the bets
        response.bets.sort(key=attrgetter('betId', 'betStatus'), reverse=True)

        for bet in response.bets:
            # Needed to load a market directly from BetInformation
            bet.exchangeId = exchangeId

            # Fix the market name to make it "more normal"
            fullMarketNameParts = bet.fullMarketName.split(' / ')
            bet.fullMarketName = ''
            for part in fullMarketNameParts:
                bet.fullMarketName += '\\%s' % part.strip()

        return response


    def GetEvents(self, parentEventId):
        '''
        Retrieve a list of eventItems/marketItems for a given Active Event
        or eventItem

        parentEvenId -1 indicates that the top active EventTypes shall be returned,
        voiding the need to separately call GetActiveEventTypes

        Removes one level of idirection for eventItems and marketItems

        @param parentEventId: id of the parent event
        @type parentEventId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        # Return the EventTypes if requested to do so with a -1 parentEventId
        if parentEventId == bfapi.RootEventId:
            return self.GetActiveEventTypes()

        # Call the plain Api method
        response = bfapi.BfApi.GetEvents(self, parentEventId)

        # Remove one level of indirection or fill with an empty list if the field is not present
        if response.eventItems:
            response.eventItems = response.eventItems.BFEvent
        else:
            response.eventItems = list()

        if response.marketItems:
            response.marketItems = response.marketItems.MarketSummary
        else:
            response.marketItems = list()

        return response


    def GetMarket(self, exchangeId, marketId):
        '''
        Retrieve a market object.

        A "exchangeId" parameter is added to the object (to ease all management
        for the calling application)
        
        Removal of array indirection is performed on runners and eventHiearchy.

        marketTime is returned as naive (no timezone) by suds. Adjusted to local
        timezone before returning

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        # Call the original
        response = bfapi.BfApi.GetMarket(self, exchangeId, marketId);

        # Embed the exchangeId in the answer, since this is a must for betting
        response.market.exchangeId = exchangeId

        # Adjust (moving arrays one level up) the response
        # There may be no runners (closed market for example)
        if response.market.runners:
            response.market.runners = response.market.runners.Runner
        else:
            response.market.runners = list()

        # Australian Market does not return eventHierarchy and the field is 'None'
        if response.market.eventHierarchy:
            response.market.eventHierarchy = response.market.eventHierarchy.EventId
        else:
            response.market.eventHierarchy = list()

        # Adjust the marketTime to the system local time
        # The original object is naive and apparently in UK Time
        marketTime = datetime(response.market.marketTime.year,
                              response.market.marketTime.month,
                              response.market.marketTime.day,
                              response.market.marketTime.hour,
                              response.market.marketTime.minute,
                              response.market.marketTime.second,
                              tzinfo=GMT(0))

        # Return it in the local time zone
        response.market.marketTime = marketTime.astimezone(LocalTimezone())

        # Return the adjusted market response
        return response


    def GetMarketInfo(self, exchangeId, marketId):
        '''
        Retrieve market information

        A "exchangeId" parameter is added to the object (to ease all management
        for the calling application)

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.GetMarketInfo(self, exchangeId, marketId)

        response.marketLite.exchangeId = exchangeId

        return response


    def GetMarketPricesCompressed(self, exchangeId, marketId):
        '''
        Retrieve the market prices (compressed)

        The answer is decompressed into a MarketPrices object

        Removal of array indirection is done on runnerPrices and bestPricesToXXX

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.GetMarketPricesCompressed(self, exchangeId, marketId)

        # The 'compressed string' response has to be parsed, processed and returned in a structure, ready
        # to be consumed

        # Return a complete GetMarketPrices response object, because all the structures are replicated
        # and the returned object is manageable
        # Changing to the GetMarketPrices call would be automatic

        response.marketPrices = self.ParseMarketPricesCompressed(response.marketPrices)

        response.marketPrices.runnerPrices = response.marketPrices.runnerPrices.RunnerPrices

        for runner in response.marketPrices.runnerPrices:
            # back prices - Move list one level up
            runner.bestPricesToBack = runner.bestPricesToBack.Price

            # lay prices - Move list one level up
            runner.bestPricesToLay = runner.bestPricesToLay.Price

        return response


    def GetMarketPricesCompressedForMarket(self, market):
        '''
        Retrieve the market prices (compressed) for a given market object

        @param market: object as returned by L{GetMarket}
        @type market: suds object

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = self.GetMarketPricesCompressed(market.exchangeId, market.marketId)

        response.market = market

        # Copy inside each runner in the market the corresponding price object
        for runner in response.market.runners:
            for runnerPrice in response.marketPrices.runnerPrices:
                if runner.selectionId == runnerPrice.selectionId:
                    runner.prices = runnerPrice
                    break

        return response


    def GetMUBets(self, exchangeId, marketId=None,
                  betStatus='MU', orderBy='BET_ID', sortOrder='DESC',
                  startRecord=0, recordCount=200, excludeLastSecond=False,
                  useMatchedSince=False, matchedSince=None):
        '''
        Get Matched and Unmatched bets for a given marketId

        Removal of indirection for bets is performed

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int
        @param betStatus: status of bets to be returned (matched, unmatched)
        @type betStatus: string (Betfair enum)
        @param orderBy: ordering criterion
        @type orderBy: string (Betfair enum)
        @param sortOrder: ordering criterion (asc/desc)
        @type sortOrder: string (Betfair enum)
        @param startRecord: to enable paging through long lists
        @type startRecord: int
        @param recordCount: maximum number of records to retrieve (see matchedSince)
        @type recordCount: int
        @param excludeLastSecond: exclude changes in the last second
        @type excludeLastSecond: bool
        @param useMatchedSince: whether to use the matched since param
        @type useMatchedSince: bool
        @param matchedSince: date to return bets since. It should void recordCounts
        @type matchedSince: datetime

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.GetMUBets(self, exchangeId, marketId=marketId,
                                         betStatus=betStatus, orderBy=orderBy,
                                         sortOrder=sortOrder,
                                         startRecord=startRecord, recordCount=recordCount,
                                         excludeLastSecond=excludeLastSecond,
                                         useMatchedSince=useMatchedSince,
                                         matchedSince=matchedSince)
                                         

        if response.bets:
            response.bets = response.bets.MUBet
        else:
            response.bets = list()

        return response


    def GetMarketProfitAndLoss(self, exchangeId, marketId,
                               includeBspBets=False,
                               includeSettledBets=False, netOfCommission=False):
        '''
        Get Matched and Unmatched bets for a given marketId

        Removal of annotations indirection is performed.

        Correction of errorCode is performed on API mismatch

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int
        @param includeBspBets: whether to include BspBets
        @type includeBspBets: bool
        @param includeSettledBets: whether to include settled bets
        @type includeSettledBets: bool
        @param netOfCommission: whether to include commision in profit and loss
        @type netOfCommission: bool

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.GetMarketProfitAndLoss(self, exchangeId, marketId,
                                                      includeBspBets=includeBspBets,
                                                      includeSettledBets=includeSettledBets,
                                                      netOfCommission=netOfCommission)

        if response.annotations:
            response.annotations = response.annotations.ProfitAndLoss
        else:
            response.annotations = list()

        # Hack to have the right error code. See BfApi
        if response.marketStatus == 'CLOSED' and response.errorCode == 'INVALID_MARKET':
            response.errorCode = 'MARKET_CLOSED'

        return response


    ############################################################
    # Bet Management Betting API Services
    ############################################################

    def PlaceBets(self, exchangeId, placeBets, nonIPRePlace=False):
        '''
        Place a list of bets in an exchange

        Removal of betResults indirection is performed

        As the API is non-permissive and sometimes the correct persistenceType
        can not be fully inferred, the function can be asked to re-place
        the bet by changing the persistenceType

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param placeBets: list of bets to be placed
        @type placeBets: list
        @param nonIPRePlace: whether to re-place in-play bets if persistence
                             type was wrong
        @type nonIPRePlace: bool

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.PlaceBets(self, exchangeId, placeBets)
        if response.betResults:
            response.betResults = response.betResults.PlaceBetsResult
        else:
            response.betResults = list()

        if response.betResults and nonIPRePlace:
            toRePlaceBets = list()
            for i, betResult in enumerate(response.betResults):
                placeBet = placeBets[i]
                if betResult.resultCode == 'INVALID_PERSISTENCE' and placeBet.betPersistenceType == 'IP':
                    # This could be a simple copy because placeBet is made of Simple types
                    newPlaceBet = deepcopy(placeBet)
                    newPlaceBet.betPersistenceType = 'NONE'
                    toRePlaceBets.append(newPlaceBet)
                    response.betResults.pop(i)

            if toRePlaceBets:
                newResponse = bfapi.BfApi.PlaceBets(self, exchangeId, toRePlaceBets)

                if newResponse.betResults:
                    for betResult in newResponse.betResults.PlaceBetsResult:
                        response.betResults.append(betResult)

        return response


    def CancelBets(self, exchangeId, cancelBets):
        '''
        Cancel a list of bets in an exchange

        Removal of betResults indirection is performed

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param cancelBets: list of bets to be canceled
        @type cancelBets: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.CancelBets(self, exchangeId, cancelBets)
        if response.betResults:
            response.betResults = response.betResults.CancelBetsResult
        else:
            response.betResults = list()

        return response


    def UpdateBets(self, exchangeId, updateBets):
        '''
        Update a list of bets

        Removal of betResults indirection is performed

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param updateBets: list of bets to be canceled
        @type updateBets: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
        response = bfapi.BfApi.UpdateBets(self, exchangeId, updateBets)
        if response.betResults:
            response.betResults = response.betResults.UpdateBetsResult
        else:
            response.betResults = list()

        return response


    ############################################################
    # Account Management Betting API Services
    ############################################################

    def GetAccountFundsUk(self):
        '''
        Helper function to Get Account funds from the UK Exchange
        '''
        return self.GetAccountFunds(bfapi.ExchangeUk)


    def GetAccountFundsAus(self):
        '''
        Helper function to Get Account funds from the Aus Exchange
        '''
        return self.GetAccountFunds(bfapi.ExchangeAus)


    def TransferFundsFromUkToAus(self, amount):
        '''
        Helper function to Transfer Account funds from the UK to Aus
        '''
        return self.TransferFunds(bfapi.ExchangeUk, bfapi.ExchangeAus, amount)


    def TransferFundsFromAusToUk(self, amount):
        '''
        Helper function to Transfer Account funds from the Aus to UK
        '''
        return self.TransferFunds(bfapi.ExchangeAus, bfapi.ExchangeUk, amount)

    ############################################################
    # Utility Functions
    ############################################################

    def ParseMarketPricesCompressed(self, compressedPrices, completeCompressed=False):
        '''
        Decompress compressed (complete or standard 3 levels) into a

        @param compressedPrices: compressed prices string
        @type compressedPrices: str
        @param completeCompressed: whether the prices to decompress are the standard
                                   3 level or the complete market prices
        @type completeCompressed: bool

        @returns: a MarketPrices or CompleteMarketPrices formed object from the compressed string
        @rtype: suds MarketPrices/CompleteMarketPrices object
        '''
        # Split the string in main MarketPrices object + Runner Objects
        parts = compressedPrices.split(':')

        # join the first fields that were separated due
        # to an escape char holding a '\:' combination
        # In theory this should only happend in the market info field which is
        # part of the header
        while True:
            if parts[0][-1] != '\\':
                break

            part0 = parts.pop(0).rstrip('\\')
            part1 = parts.pop(0)
            newpart = part0 + ':' + part1
            parts.insert(0, newpart)

        # The '0' index contains the Market prices header
        marketPrices = self.ParseMarketPricesCompressedHeader(parts[0], completeCompressed);

        # Parse and append each individual runner
        for runnerPart in parts[1:]:

            # Parse the runner
            runner = self.ParseMarketPricesCompressedRunner(runnerPart, completeCompressed)

            # Append it to the array of runners
            marketPrices.runnerPrices.RunnerPrices.append(runner)

        #return the fully populated MarketPrices object
        return marketPrices


    def ParseMarketPricesCompressedHeader(self, marketPricesHeader, completeCompressed):
        '''
        Decompress the header of the compressed market prices

        @param marketPricesHeader: compressed prices header string
        @type marketPricesHeader: str
        @param completeCompressed: whether the prices to decompress are the standard
                                   3 level or the complete market prices
        @type completeCompressed: bool

        @returns: the prices header
        @rtype: suds MarketPrices header object
        '''
        # Generate the object to store the information
        # marketPrices = self.GetObjectExchange('MarketPrices')
        marketPrices = EmptyObject()
        marketPrices.runnerPrices = EmptyObject()
        marketPrices.runnerPrices.RunnerPrices = list()

        # Split it into its constituent parts
        parts = marketPricesHeader.split('~')

        # and assign it to the fields of the generated MarketPrices object
        if completeCompressed == False:
            marketPrices.marketId = int(parts[0])
            marketPrices.currencyCode = parts[1]
            marketPrices.marketStatus = parts[2]
            marketPrices.delay = int(parts[3])
            marketPrices.numberOfWinners = int(parts[4])
            marketPrices.marketInfo = parts[5]
            marketPrices.discountAllowed = bool(parts[6])
            marketPrices.marketBaseRate = float(parts[7])
            marketPrices.lastRefresh = datetime.fromtimestamp(long(parts[8])/1000)
            marketPrices.removedRunners = parts[9]
            marketPrices.bspMarket = (parts[10] == 'Y')
        else:
            # For completecompressed, fill the available fields and remove the others
            marketPrices.marketId = int(parts[0])

            # del marketPrices.currencyCode
            # del marketPrices.marketStatus

            marketPrices.delay = int(parts[1])

            # del marketPrices.numberOfWinners
            # del marketPrices.marketInfo
            # del marketPrices.discountAllowed
            # del marketPrices.marketBaseRate
            # del marketPrices.lastRefresh

            marketPrices.removedRunners = parts[2]

            # del marketPrices.bspMarket

        # return the object
        return marketPrices


    def ParseMarketPricesCompressedRunner(self, marketPricesRunner, completeCompressed):
        '''
        Decompress the the prices of a runner

        @param marketPricesRunner: compressed prices header string
        @type marketPricesRunner: str
        @param completeCompressed: whether the prices to decompress are the standard
                                   3 level or the complete market prices
        @type completeCompressed: bool

        @returns: the prices for a runner
        @rtype: suds RunnerPrices objects
        '''
        # Generate a RunnerPrices object
        # runner = self.GetObjectExchange('RunnerPrices')
        runner = EmptyObject()
        runner.bestPricesToBack = EmptyObject()
        runner.bestPricesToBack.Price = list()
        runner.bestPricesToLay = EmptyObject()
        runner.bestPricesToLay.Price = list()

        # Parse the runner main fields, header + 2xPrices
        partsRunner = marketPricesRunner.split('|')

        # Parse the header (part[0])
        # Split the header in its constituent parts
        partsHeader = partsRunner[0].split('~')

        # Assign the header fields
        runner.selectionId = int(partsHeader[0])
        runner.asianLineId = 0
        runner.sortOrder = int(partsHeader[1])
        runner.totalAmountMatched = float(partsHeader[2])

        # The following 3 fields may be empty, therefore raising a exception
        runner.lastPriceMatched = self.ToFloatIfNotNull(partsHeader[3])
        runner.handicap = self.ToFloatIfNotNull(partsHeader[4])
        runner.reductionFactor = self.ToFloatIfNotNull(partsHeader[5])

        runner.vacant = (partsHeader[6] == 'true')

        # There 'may' be 3 additional fields for SP prices
        # SP do only apply to horses, so even if they are present, we leave
        # them out of the equation for now
        # The latest experiments show the fields always in place
        # Protect with a sanity check (try or check for length of array and strings)
        runner.farBSP = self.ToFloatIfNotNull(partsHeader[7])
        runner.nearBSP = self.ToFloatIfNotNull(partsHeader[8])
        runner.actualBSP = self.ToFloatIfNotNull(partsHeader[9])

        if completeCompressed == True:

            numFieldsPerPrice = 5
            runner.Prices = list()

            # Delete the non-used 'bestpricesToXXXX' lists
            # del runner.bestPricesToBack
            # del runner.bestPricesToLay

            partsPrices = partsRunner[1].split('~')
            numPrices = len(partsPrices) / numFieldsPerPrice

            for i in xrange(numPrices):

                index = i * numFieldsPerPrice

                # numFieldsPerPrice has to be added to the index to include the last element.
                price = self.ParseMarketPricesCompressedRunnerAvailabilityInfo(partsPrices[index:index + numFieldsPerPrice])

                runner.Price.append(price)
        else:

            numFieldsPerPrice = 4
            
            partsPrices = partsRunner[1].split('~')
            numPrices = len(partsPrices) / numFieldsPerPrice
            # Back Prices
            for i in xrange(numPrices):

                index = i * numFieldsPerPrice

                # numFieldsPerPrice has to be added to the index to include the last element.
                price = self.ParseMarketPricesCompressedRunnerPrice(partsPrices[index:index + numFieldsPerPrice])

                runner.bestPricesToBack.Price.append(price)

            partsPrices = partsRunner[2].split('~')
            numPrices = len(partsPrices) / numFieldsPerPrice
            # Lay Prices
            for i in xrange(numPrices):

                index = i * numFieldsPerPrice

                # numFieldsPerPrice has to be added to the index to include the last element
                price = self.ParseMarketPricesCompressedRunnerPrice(partsPrices[index:index + numFieldsPerPrice])

                runner.bestPricesToLay.Price.append(price)
                    
        return runner


    @staticmethod
    def ToFloatIfNotNull(strval):
        '''
        Return a float if the string is not null or 0.0

        @param strval: string containing the float
        @type strval: str

        @returns: the float contained in the string or 0.0
        @rtype: float
        '''
        return float(strval) if strval else 0.0


    def ParseMarketPricesCompressedRunnerPrice(self, compressedPriceParts):
        '''
        Decompress individual price parts into Price objects

        @param compressedPriceParts: compressed prices
        @type compressedPriceParts: str

        @returns: the individual prices
        @rtype: suds Price objects
        '''
        # Generate a RunnerPrices object
        # price = self.GetObjectExchange('Price')
        price = EmptyObject()

        # Split the price in its constituent parts
        # parts = p_price.split('~')
        # Ideally the string is already a list
        parts = compressedPriceParts

        price.price = float(parts[0])
        price.amountAvailable = float(parts[1])
        price.betType = parts[2]
        price.depth = int(parts[3])

        return price


    def ParseMarketPricesRunnerCompressedAvailabilityInfo(self, compressedPriceParts):
        '''
        Decompress individual price availability (complete prices) parts into objects

        @param compressedPriceParts: compressed prices
        @type compressedPriceParts: str

        @returns: the individual prices
        @rtype: suds Price objects
        '''
        # Generate a RunnerPrices object
        # price = self.GetObjectExchange('AvailabilityInfo')
        price = EmptyObject()

        # Split the price in its constituent parts
        # parts = p_price.split('~')
        # Ideally the string is already a list
        parts = compressedPriceParts

        price.odds = float(parts[0])
        price.totalAvailableBackAmount = float(parts[1])
        price.totalAvailableLayAmount = float(parts[2])
        price.totalBspBackAmount = float(parts[3])
        price.totalBspLayAmount = float(parts[4])

        return price
