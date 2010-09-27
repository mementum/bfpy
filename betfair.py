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

from timezone import GMT, LocalTimezone


class EmptyObject(object):
    pass

import bfapi
import bferror

MinBet = 2.00

class Betfair(bfapi.BfApi):

    def __init__(self, **kwargs):

        bfapi.BfApi.__init__(self, **kwargs)

        self.username = None
        self.password = None


    ############################################################
    # API Object Creation
    ############################################################
    def CreateMarket(self):
        return self.GetObjectExchange('Market')

    def CreateRunner(self):
        return self.GetObjectExchange('Runner')

    def CreateMarketPrices(self):
        return self.GetObjectExchange('MarketPrices')

    def CreateRunnerPrices(self):
        return self.GetObjectExchange('RunnerPrices')

    def CreatePrice(self):
        return self.GetObjectExchange('Price')

    def CreateEvent(self, eventId=-1, eventName=''):
        # event = self.GetObjectGlobal('BFEvent')
        event = EmptyObject()
        event.eventId = eventId
        event.eventName = eventName
        return event


    def CreatePlaceBet(self):
        return self.GetObjectExchange('PlaceBets')


    def CreateCancelBet(self):
        return self.GetObjectExchange('CancelBets')


    def CreateUpdateBet(self):
        return self.GetObjectExchange('UpdateBets')


    ############################################################
    # General Services API Services
    ############################################################

    def Login(self, username, password, productId=82, vendorSoftwareId=0):
        # Invalidate previous credentials
        self.username = None
        self.password = None

        response = bfapi.BfApi.Login(self, username, password, productId, vendorSoftwareId)

        # If not exception was thrown, then login succeeded, store the credentials
        self.username = username
        self.password = password

        return response


    def Logout(self):
        # Invalidate credentials before calling the service, since this might fail
        # with an Exception, preventing us from clearing the credentials 
        self.username = None
        self.password = None

        return bfapi.BfApi.Logout(self)


    def ReLogin(self):
        '''
        Attempts to execute Login if the credentials have already been proven right

        Raises a BfApiError_t with NO_SESSION otherwise
        '''
        if self.username:
            return self.Login(self.username, self.password)
        else:
            raise bferror.BfApiError('ReLogin', 'NO_SESSION', 'No credentials available to relogin')


    ############################################################
    # Read-Only Betting API Services
    ############################################################

    def GetActiveEventTypes(self):
        '''
        Return the list of EventTypes aliased as Events.
        The reasoning behind this is to let the UI manage only two types of objects:
        -- Events
        -- Markets

        EventTypes have an exchangeId field for Greyhound races and Events have fields
        like menuLevel and orderIndex, but the main fields are actually the same:

        -- id vs eventId
        -- name vs eventName
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
        response = bfapi.BfApi.GetAllEventTypes(self)

        # Remove indirection
        if response.eventTypeItems != None:
            response.eventTypeItems = response.eventTypeItems.EventType
        else:
            response.eventTypeItems = list()

        return response


    def GetAllMarkets(self, exchangeId):
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
        response = bfapi.BfApi.GetCompleteMarketPricesCompressed(self, exchangeId, marketId)

        response.completeMarketPrices = self.ParseMarketPricesCompressed(response.completemarketPrices, completeCompressed=True)
        response.completeMarketPrices.runnerPrices = response.completeMarketPrices.runnerPrices.RunnerPrices

        return response


    def GetCurrentBets(self, exchangeId):
        responseMatched = bfapi.BfApi.GetCurrentBets(self, exchangeId, 'M')

        # Remove one indirection level if possible
        if responseMatched.bets:
            responseMatched.bets = responseMatched.bets.Bet
        else:
            responseMatched.bets = list()

        responseUnmatched = bfapi.BfApi.GetCurrentBets(self, exchangeId, 'U')
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
        Return the list of events and markets for the given parentEventId

        The id -1 indicates that the top active EventTypes shall be returned.

        The EventTypes will be aliased to eventItems

        @type parentEventId: int
        @param parentEventId: Id of parent event for the returned objects

        @rtype: object
        @return: the response contains two lists: eventItems and marketItems
                 eventItems can be identified by the eventId and eventName fields
                 marketItems can be identified by teh marketId and marketName fields
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

        response.market.marketTime = marketTime.astimezone(LocalTimezone())

        # Return the adjusted market response
        return response


    def GetMarketInfo(self, exchangeId, marketId):
        response = bfapi.BfApi.GetMarketInfo(self, exchangeId, marketId)

        response.marketLite.exchangeId = exchangeId

        return response


    def GetMarketPricesCompressed(self, exchangeId, marketId):
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
        response = self.GetMarketPricesCompressed(market.exchangeId, market.marketId)

        response.market = market

        # Copy inside each runner in the market the corresponding price object
        for runner in response.market.runners:
            for runnerPrice in response.marketPrices.runnerPrices:
                if runner.selectionId == runnerPrice.selectionId:
                    runner.prices = runnerPrice
                    break

        return response


    def GetMUBets(self, exchangeId, marketId):
        response = bfapi.BfApi.GetMUBets(self, exchangeId, marketId)

        if response.bets:
            response.bets = response.bets.MUBet
        else:
            response.bets = list()

        return response


    def GetMarketProfitAndLoss(self, exchangeId, marketId):
        response = bfapi.BfApi.GetMarketProfitAndLoss(self, exchangeId, marketId)

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
        response = bfapi.BfApi.CancelBets(self, exchangeId, cancelBets)
        if response.betResults:
            response.betResults = response.betResults.CancelBetsResult
        else:
            response.betResults = list()

        return response


    def UpdateBets(self, exchangeId, updateBets):
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
        return self.GetAccountFunds(bfapi.ExchangeUk)


    def GetAccountFundsAus(self):
        return self.GetAccountFunds(bfapi.ExchangeAus)


    def TransferFundsFromUkToAus(self, amount):
        return self.TransferFunds(bfapi.ExchangeUk, bfapi.ExchangeAus, amount)


    def TransferFundsFromAusToUk(self, amount):
        return self.TransferFunds(bfapi.ExchangeAus, bfapi.ExchangeUk, amount)

    ############################################################
    # Utility Functions
    ############################################################

    def ParseMarketPricesCompressed(self, compressedPrices, completeCompressed=False):
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

        return float(strval) if len(strval) else 0.0


    def ParseMarketPricesCompressedRunnerPrice(self, compressedPriceParts):
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
