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
Implementation of BfApi request and response processors
'''

from datetime import datetime, timedelta

import bferror
from timezone import LocalTimezone
from util import EmptyObject


class ArrayUnfix(object):
    '''
    Request processor

    Places an array a level lower than specified by the call
    to add the array indirections present in the Betfair
    WSDL definitions
    '''
    def __init__(self, attrName, subAttrName):
        self.attrName = attrName
        self.subAttrName = subAttrName

    def __call__(self, request, requestArgs, **kwargs):
        attr = getattr(request, self.attrName)
        try:
            value = requestArgs.pop(self.attrName)
            setattr(attr, self.subAttrName, value)
        except KeyError:
            # Do nothing if the param has not been specified
            pass


class ArrayFix(object):
    '''
    Response processor

    Remove one (or more) levels of indirection from the arrays
    defined in the Betfair WSDLs
    '''
    def __init__(self, attrName, subAttrName):
        self.attrNames = attrName.split('.')
        self.subAttrNames = subAttrName.split('.')

    def __call__(self, response, **kwargs):
        parentAttrs = response

        targetName = self.attrNames[-1]
        if len(self.attrNames) > 1:
            for attrName in self.attrNames[:-1]:
                parentAttrs = getattr(parentAttrs, attrName)

        if not isinstance(parentAttrs, list):
            parentAttrs = [parentAttrs]

        for parentAttr in parentAttrs:
            targetAttr = getattr(parentAttr, targetName)
            if targetAttr is not None:
                subAttr = targetAttr
                for subAttrName in self.subAttrNames:
                    subAttr = getattr(subAttr, subAttrName)
            else:
                subAttr = list()

            setattr(parentAttr, targetName, subAttr)


class ArrayFix2(object):
    '''
    Response processor

    Remove one (or more) levels of indirection from the arrays
    defined in the Betfair WSDLs
    '''
    def __init__(self, attrName, subAttrName):
        self.attrNames = attrName.split('.')
        self.subAttrNames = subAttrName.split('.')

    def __call__(self, response, **kwargs):
        parentAttr = response
        if len(self.attrNames) > 1:
            for attrName in self.attrNames[:-1]:
                parentAttr = getattr(parentAttr, attrName)

        targetName = self.attrNames[-1]
        targetAttr = getattr(parentAttr, targetName)

        if targetAttr is not None:
            subAttr = targetAttr
            for subAttrName in self.subAttrNames:
                subAttr = getattr(subAttr, subAttrName)
        else:
            subAttr = list()

        setattr(parentAttr, targetName, subAttr)


class PatchAttr(object):
    '''
    Response processor

    An attribute can be added to an attribute of the response
    one or several levels below the root, to have sensible
    information added to a response
    '''
    def __init__(self, attrName, subAttrName):
        self.attrNames = attrName.split('.')
        self.subAttrName = subAttrName


    def __call__(self, response, **kwargs):
        subAttr = kwargs.get(self.subAttrName)
        
        attr = response
        for attrName in self.attrNames:
            attr = getattr(attr, attrName)

        setattr(attr, subAttrName, subAttr)


class PatchAttrExId(PatchAttr):
    '''
    Response processor

    Specialization of PatchAttr that handles "exchangeId"
    patching specifically
    '''
    def __init__(self, attrName):
        PatchAttr.__init__(self, attrName, 'exchangeId')



class ProcAllMarkets(object):
    '''
    Response processor

    Parses and formats as objects the information returned by
    getAllMarketData
    '''
    def __call__(self, response, **kwargs):
        # Creat a placeholder for the marketItems to be parsed
        marketItems = list()

        # Parse the marketItems data string - separate major fields
        marketDataParts = response.marketData.split(':')

        # First element is always empty ... pop it out because Betfair places a delimiter at the beginning
        marketDataParts.pop(0)

        toSkip = 0
        for i in xrange(len(marketDataParts)):

            if toSkip > 0:
                toSkip -= 1
                continue

            # Break fields
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


class ProcCurrentBets(object):
    '''
    Response processor

    Does some patching and correction to the bet information of
    bets returned by getCurrentBets
    '''
    def __call__(self, response, **kwargs):
        exchangeId = kwargs.get('exchangeId')
        for bet in response.bets:
            bet.exchangeId = exchangeId

            # Fix the market name to make it "more normal"
            fullMarketNameParts = bet.fullMarketName.split(' / ')
            bet.fullMarketName = ''
            for part in fullMarketNameParts:
                bet.fullMarketName += '\\%s' % part.strip()


class PreProcLogin(object):
    '''
    Request processor

    Preprocesses a login request to enable re-login
    functionality
    '''
    def __call__(self, request, requestArgs, **kwargs):
        instance = kwargs.get('instance')
        methodArgs = kwargs.get('methodArgs')

        loginArgs = ['username', 'password', 'productId', 'vendorSoftwareId']

        for loginArg in loginArgs:
            if hasattr(instance, loginArg):
                if loginArg not in methodArgs:
                    loginArgValue = getattr(instance, loginArg)
                    requestArgs[loginArg] = loginArgValue


class ProcLogin(object):
    '''
    Response processor

    Enables information storage for re-login functionality
    '''
    def __call__(self, response, **kwargs):
        instance = kwargs.get('instance')
        request = kwargs.get('request')

        loginArgs = ['username', 'password', 'productId', 'vendorSoftwareId']

        for loginArg in loginArgs:
            attrValue = getattr(request, loginArg)
            setattr(instance, loginArg, attrValue)


class ProcMarket(object):
    '''
    Response processor

    Patches exchangeId in the market, removes some indirections
    and adjusts the marketTime to have a timezone (and therefore be
    manageable) and to match the daylight savings
    '''
    def __call__(self, response, **kwargs):
        exchangeId = kwargs.get('exchangeId')

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
        # The original object is naive and suds fails to identify DST settings
        localTimezone = LocalTimezone()
        daylight = localTimezone.dst(response.market.marketTime)
        response.market.marketTime += daylight

        # Return a non-naive datetime object (in case the calling app wanted to
        # move it to another timezone
        marketTime = datetime(response.market.marketTime.year,
                              response.market.marketTime.month,
                              response.market.marketTime.day,
                              response.market.marketTime.hour,
                              response.market.marketTime.minute,
                              response.market.marketTime.second,
                              tzinfo=localTimezone)


class ProcMarketPricesCompressed(object):
    '''
    Response processor

    Decompresses the answer and removes indirections in the decompressed answer
    '''
    def __init__(self, completeCompressed=False):
        self.completeCompressed = completeCompressed

    def __call__(self, response, **kwargs):
        if not self.completeCompressed:
            response.marketPrices = self.ParseMarketPricesCompressed(response.marketPrices, self.completeCompressed)
        else:
            response.completeMarketPrices = self.ParseMarketPricesCompressed(response.completeMarketPrices, self.completeCompressed)

        # Array Fixes of the "decompressed prices" string - Can't be done before
        if self.completeCompressed:
            response.completeMarketPrices.runnerPrices = response.completeMarketPrices.runnerPrices.RunnerPrices
        else:
            response.marketPrices.runnerPrices = response.marketPrices.runnerPrices.RunnerPrices
            for runner in response.marketPrices.runnerPrices:
                runner.bestPricesToBack = runner.bestPricesToBack.Price
                runner.bestPricesToLay = runner.bestPricesToLay.Price


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
            # For completecompressed, fill the available fields and (remove) the others
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
                price = self.ParseMarketPricesRunnerCompressedAvailabilityInfo(partsPrices[index:index + numFieldsPerPrice])

                runner.Prices.append(price)
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


class PreProcMarketProfitAndLoss(object):
    '''
    Request processor

    The WSDLs have a typo for this call: marketID instead of marketId
    like all other calls. This method corrects possible user mistakes
    '''
    def __call__(self, request, requestArgs, **kwargs):
        try:
            marketId = requestArgs.pop('marketId')
            requestArgs['marketID'] = marketId
        except KeyError:
            pass


class ProcMarketProfitAndLoss(object):
    '''
    Response processor

    On closed markets, the call returns INVALID_MARKET (unlike getMUBets and
    getMarketPricesXXXXX) and this call patches it if needed.

    If the condition is not met, the exception that would have been raised during
    invocation is raised
    '''
    def __call__(self, response, **kwargs):
        '''
        @raise BfServiceError: if INVALID_MARKET is received with a MARKET_CLOSED status
        '''
        if response.errorCode == 'INVALID_MARKET':
            if response.marketStatus == 'CLOSED':
                response.errorCode = 'MARKET_CLOSED' # OK could also be returned
            else:
                raise bferror.BfServiceError('getMarketProfitAndLoss', response, str(response), response.errorCode)


class ProcMarketPrices(object):
    '''
    Response processor

    Removes several possible array indirections from a GetMarketPricesResp
    '''
    def __call__(self, response, **kwargs):

        mktPrices = response.marketPrices

        if mktPrices.runnerPrices is not None:
            mktPrices.runnerPrices = mktPrices.runnerPrices.RunnerPrices
        else:
            mktPrices.runnerPrices = list()

        for runnerPrice in mktPrices.runnerPrices:
            if runnerPrice.bestPricesToBack is not None:
                runnerPrice.bestPricesToBack = runnerPrice.bestPricesToBack.Price
            else:
                runnerPrice.bestPricesToBack = list()

            if runnerPrice.bestPricesToLay is not None:
                runnerPrice.bestPricesToLay = runnerPrice.bestPricesToLay.Price
            else:
                runnerPrice.bestPricesToLay = list()


class ProcMarketTradedVolumeCompressed(object):
    '''
    Response processor

    Decompresses de Market Traded Volume response
    '''
    def __call__(self, response, **kwargs):
        tradedVolume = list()

        runnerInfosStr = response.tradedVolume.split(':')
        for runnerInfoStr in runnerInfosStr[1:]:
            runnerInfo = EmptyObject()

            runnerInfoParts = runnerInfoStr.split('|')

            runnerDetails = runnerInfoParts[0].split('~')
            runnerInfo.selectionId = int(runnerDetails[0])
            runnerInfo.asianLineId = int(runnerDetails[1])
            runnerInfo.actualBSP = float(runnerDetails[2])
            runnerInfo.totalBspBackMatchedAmmount = float(runnerDetails[3])
            runnerInfo.totalBspLiabilityMatchedAmount = float(runnerDetails[4])

            runnerInfo.priceItems = list()
            for priceItemStr in runnerInfoParts[1:]:
                priceItemParts = priceItemStr.split('~')

                priceItem = EmptyObject()
                priceItem.odds = float(priceItemParts[0])
                priceItem.totalMatchedAmount = float(priceItemParts[1])

                runnerInfo.priceItems.append(priceItem)

            tradedVolume.append(runnerInfo)

        response.tradedVolume = tradedVolume


class PreProcPrivateMarkets(object):
    '''
    Request processor

    The docs have a typo for this call: EventTypeID for a paramenter
    instead of the usual spelling eventTypeId (which is the name in
    the WSDL)
    This method corrects possible user mistakes
    '''
    def __call__(self, request, requestArgs, **kwargs):
        try:
            eventTypeId = requestArgs.pop('EventTypeID')
            requestArgs['eventTypeId'] = eventTypeId
        except KeyError:
            pass


class ProcSilks(object):
    '''
    Response processor

    Removes several possible array indirections from a GetSilksResp/GetSilksRespV2
    '''
    def __call__(self, response, **kwargs):

        if response.marketDisplayDetails is not None:
            response.marketDisplayDetails = response.marketDisplayDetails.MarketDisplayDetail
        else:
            response.marketDisplayDetails = list()

        for marketDisplayDetails in response.marketDisplayDetails:
            if marketDisplayDetails.racingSilks is not None:
                marketDisplayDetails.racingSilks = marketDisplayDetails.racingSilks.RacingSilk
            else:
                marketDisplayDetails.racingSilks = list()


class PreBetHistory(object):
    '''
    Request processor

    Provide a default 24 hour BetHistory request
    '''
    def __call__(self, request, requestArgs, **kwargs):
        if 'placedDateFrom' not in requestArgs:
            requestArgs['placedDateFrom'] = datetime.now() - timedelta(days=1)

        if 'placedDateTo' not in requestArgs:
            requestArgs['placedDateTo'] = datetime.now()


class PreAccountStatement(object):
    '''
    Request processor

    Provide a default 24 hour request
    '''
    def __call__(self, request, requestArgs, **kwargs):
        if 'startDate' not in requestArgs:
            requestArgs['startDate'] = datetime.now() - timedelta(days=1)

        if 'endDate' not in requestArgs:
            requestArgs['endDate'] = datetime.now()
