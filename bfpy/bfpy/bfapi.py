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
BfApi object implemenation.

It does initialize suds logging to a L{NullHandler} to avoid any logging output
'''

from copy import copy
from collections import namedtuple
from datetime import datetime
import logging
from socket import error as SocketError
from threading import Lock

import suds
    
class NullHandler(logging.Handler):
    '''
    Definition of a Null logging class to avoid any output
    from suds
    '''
    def emit(self, record):
        '''
        Simply discard the incoming with the incoming logging record

        @param record: logging record
        @type record: str
        '''
        pass

sudsLogger = logging.getLogger('suds')
sudsLogger.setLevel(logging.ERROR)

if True:
    handler = NullHandler()
else:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -\n%(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.ERROR)

sudsLogger.addHandler(handler)


import bferror
import bftransport
import bfwsdl

RootEventId = -1

GlobalService = 0
ExchangeUk = 1
ExchangeAus = 2

freeApi = 82

MarketTuple = namedtuple('MarketTuple', ('exchangeId', 'marketId'))

class BfApi(object):
    '''
    The BfApi is a mere "objectization" of the betfair API. It creates the needed
    suds clients to communicate with the Betfair API and provides the framework to
    easily create request objects and invoke methods, whilst also providing error
    management.

    No processing of the answers received from the API is done
    '''

    # default send receive timeout
    classTimeout = 14

    # socket.setdefaulttimeout(classTimeout)

    WsdlFiles = {
        GlobalService: bfwsdl.BFGlobalService,
        ExchangeUk: bfwsdl.BFExchangeService,
        ExchangeAus: bfwsdl.BFExchangeServiceAus
        }

    def __init__(self, **kwargs):
        '''
        Constructor. Create the transport and the suds clients needed to talk
        to the Betfair API.

        @param kwargs: standard Python keywords arguments
        @type kwargs: dict

        @returns: a constructed object
        @rtype: BfApi
        '''
        self.timeout = kwargs.get('timeout', self.classTimeout)
        self.sessionToken = ''

	# Initialize the Betfair communication objects
        self.transport = bftransport.BfTransport()
        # The proxy may be needed if the WSDLs are to be downloaded from the net
        if 'proxydict' in kwargs:
            self.transport.setproxy(kwargs['proxydict'])
        self.bfClient = dict()
        for key, val in self.WsdlFiles.iteritems():
            self.bfClient[key] = suds.client.Client(val, transport=self.transport.clone(), timeout=self.timeout)


    def __deepcopy__(self, memo):
        '''
        Clones the L{BfApi} object

        @param memo: standard Python deepcopy param
        @type memo: dict

        @returns: cloned self
        @rtype: BfApi
        '''
        return self.Clone()


    def Clone(self):
        '''
        Clones the L{BfApi} object, taking clare of cloning the suds clients

        @returns: cloned self
        @rtype: BfApi
        '''
        clone = copy(self)

        clone.bfClient = dict()
        for key, bfClient in self.bfClient.iteritems():
            clone.bfClient[key] = bfClient.clone()
                
        clone.sessionToken = ''
        return clone


    def GetAPIRequestHeader(self, reqObjName, bfServiceId):
        '''
        Returns a new API Request Header, checking if a session logging exists and
        raising an L{BfApiError} if no session is alive. Else, it fills the session
        field

        @param reqObjName: Name of the request object that will hold the request header
        @type reqObjName: str
        @param bfServiceId: id of the WSDL object to use (Exchange or Global)
        @type bfServiceId: int

        @returns: APIRequestHeader
        @rtype: suds object

        @raise BfApiError: on no session available
        '''
        # Check if we are logged in
        if(self.sessionToken == ''):
            raise bfapi.BfApiError(reqObjName[:-3], None, 'No Session Token available', 'NO_SESSION')

	# Create the keepaliverequest and associated data objects
        header = self.GetObject('APIRequestHeader', bfServiceId)

	header.clientStamp = 0
	header.sessionToken = self.sessionToken

        return header


    def GetObject(self, objectName, bfServiceId):
        '''
        Proxy function to obtain an object from a suds wsdl client

        @param objectName: Name of the object
        @type objectName: str
        @param bfServiceId: id of the suds wsdl client to use
        @type bfServiceId: int

        @returns: requested suds object
        @rtype: suds object
        '''
        return self.bfClient[bfServiceId].factory.create('ns1:%s' % objectName)


    def GetObjectExchange(self, objectName, exchangeId=ExchangeUk):
        '''
        Proxy function to obtain an object from a suds "exchange" wsdl client

        Since both exchanges (UK and Aus) support the same set of objects, ExchangeUK
        is provided as the default value to ease calling

        @param objectName: Name of the object
        @type objectName: str
        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int

        @returns: requested suds "exchange" object
        @rtype: suds object
        '''
        return self.GetObject(objectName, exchangeId)


    def GetObjectGlobal(self, objectName):
        '''
        Proxy function to obtain an object from the suds "global" wsdl client

        @param objectName: Name of the object
        @type objectName: str

        @returns: requested suds "global" object
        @rtype: suds object
        '''
        return self.GetObject(objectName, GlobalService)


    def GetRequestObject(self, reqObjectName, bfServiceId, addHeader=True):
        '''
        Proxy function to obtain a request object from a suds wsdl client, adding
        an APIRequestHeader if needed

        Some services (like Login) do not require a header and that is the reason
        for the addHeader param

        @param reqObjectName: Name of the request object
        @type reqObjectName: str
        @param bfServiceId: id of the suds wsdl client to use
        @type bfServiceId: int
        @param addHeader: whether a APIRequestHeader should be returned in the object
        @type addHeader: bool

        @returns: requested suds object
        @rtype: suds object
        '''
        reqObject = self.GetObject(reqObjectName, bfServiceId)

        if addHeader:
            reqObject.header = self.GetAPIRequestHeader(reqObjectName, bfServiceId)

        return reqObject


    def GetRequestObjectGlobal(self, requestObjectName, addHeader=True):
        '''
        Helper Proxy function to obtain a request object from the suds "global" wsdl client

        Some services (like Login) do not require a header and that is the reason
        for the addHeader param

        @param requestObjectName: Name of the request object
        @type requestObjectName: str
        @param addHeader: whether a APIRequestHeader should be returned in the object
        @type addHeader: bool

        @returns: requested suds "global" object
        @rtype: suds object
        '''
        return self.GetRequestObject(requestObjectName, GlobalService, addHeader)


    def GetRequestObjectExchange(self, requestObjectName, exchangeId=ExchangeUk):
        '''
        Helper Proxy function to obtain a request object from suds "exchange" wsdl client

        Since both exchanges (UK and Aus) support the same set of objects, ExchangeUK
        is provided as the default value to ease calling

        So far all seen Exchange objects require a header. See L{GetRequestObjectGlobal}

        @param requestObjectName: Name of the request object
        @type requestObjectName: str
        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int

        @returns: requested suds "exchange" object
        @rtype: suds object
        '''
        return self.GetRequestObject(requestObjectName, exchangeId, addHeader=True)


    def InvokeRequest(self, bfServiceId, requestName, requestArg, goodErrorCodes=None):
        '''
        Invokes a method by name, passing the supplied request argument by using specific
        suds wsdl client (specified by bfServiceId)

        The method checks for the existence of the method before invocation and raises
        different exceptions in case errors happen.

        If the call to the Betfair API succeeds but a high level errorCode is returned,
        a list of goodErrorCodes is checked before raising the exception. This is so,
        because the Betfair API may have errors (returning INVALID_MARKET instead of
        MARKET_CLOSED in getProfitAndLoss) or because an error like
        INVALID_LOCALE_DEFAULTING_TO_ENGLISH may be returned, which still provides the
        requested info even if in a different language.

        Suds raises some plain exceptions and its exceptions do not have a base
        "SudsError" class. Therefore a catch-all "Exception" is implemented to try a
        good error reporting to the calling application

        @param bfServiceId: id of the suds wsdl client to use
        @type bfServiceId: int
        @param requestName: service to invoke
        @type requestName: str
        @param requestArg: object to be passed as param of the request
        @type requestArg: suds object
        @param goodErrorCodes: list of errorCodes to skip
        @type goodErrorCodes: list

        @returns: Betfair API answer
        @rtype: suds object

        @raise BfPythonError: if the method is not found in the suds client
        @raise BfHttpError: if suds raises a WebFault
        @raise BfNetworkError: on potential network errors
        @raise BfError: on generic Exceptions
        @raise BfApiError: if the API replies with a ApiHeader error
        @raise BfServiceError: if the API replies with a Service error and
                               the error is not overseen by goodErrorCodes
        '''
        if hasattr(self.bfClient[bfServiceId].service, requestName):
            method = getattr(self.bfClient[bfServiceId].service, requestName)
        else:
            raise bferror.BfPythonError(requestName, self.bfClient[bfServiceId], 'Method Not found')

        try:
            response = method(requestArg)
        except suds.WebFault, e:
            raise bferror.BfHttpError(requestName, e, str(e), e.fault, e.document)
        except (SocketError, bftransport.TransportException), e:
            # Summarise network errors into a generic notification
            raise bferror.BfNetworkError(requestName, e, str(e), e.args)
        except Exception, e:
            # Catch all - needed because suds is inconsistent with error handling
            raise bferror.BfError(requestName, e, str(e), e.args)

        # Response is returned

        # First check API errors
        if response.header.errorCode != 'OK':
            raise bferror.BfApiError(requestName, response, str(response), response.header.errorCode)

        # Some services don't return errorCode, check before error checking
        if hasattr(response, 'errorCode'):
            # if errorCode is present check it is ok or an accepted errorCode
            if not (response.errorCode == 'OK' or (goodErrorCodes and response.errorCode in goodErrorCodes)):
                raise bferror.BfServiceError(requestName, response, str(response), response.errorCode)

        # Save the "new" session token
        self.sessionToken = response.header.sessionToken
        return response


    def InvokeRequestGlobal(self, requestName, requestArg, goodErrorCodes=None):
        '''
        Helper Proxy function to invoke "global" methods

        @param requestName: service to invoke
        @type requestName: str
        @param requestArg: object to be passed as param of the request
        @type requestArg: suds object
        @param goodErrorCodes: list of errorCodes to skip
        @type goodErrorCodes: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
        return self.InvokeRequest(GlobalService, requestName, requestArg, goodErrorCodes)


    def InvokeRequestExchange(self, exchangeId, requestName, requestParam, goodErrorCodes=None):
        '''
        Helper Proxy function to invoke "exchange" methods

        @param exchangeId: id of the suds wsdl client to use
        @type exchangeId: int
        @param requestName: service to invoke
        @type requestName: str
        @param requestParam: object to be passed as param of the request
        @type requestParam: suds object
        @param goodErrorCodes: list of errorCodes to skip
        @type goodErrorCodes: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
        return self.InvokeRequest(exchangeId, requestName, requestParam, goodErrorCodes)


    ############################################################
    # Services
    ############################################################

    ############################################################
    # General API Services
    ############################################################

    def Login(self, username, password, productId=82, vendorSoftwareId=0):
        '''
        Login onto the Betfair API

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
        request = self.GetRequestObjectGlobal('LoginReq', addHeader=False)

	request.username = username
	request.password = password
	request.productId = productId
	request.vendorSoftwareId = vendorSoftwareId

	request.ipAddress = '0'
	request.locationId = 0

        return self.InvokeRequestGlobal('login', request);


    def Logout(self):
        '''
        Logout

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectGlobal('LogoutReq')
        return self.InvokeRequestGlobal('logout', request);

	
    def KeepAlive(self):
        '''
        Keepalive

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectGlobal('KeepAliveReq')
        return self.InvokeRequestGlobal('keepAlive', request);


    ############################################################
    # Bet Placement API Services
    ############################################################

    def PlaceBets(self, exchangeId, placeBets):
        '''
        Place a list of bets in an exchange

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param placeBets: list of bets to be placed
        @type placeBets: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectExchange('PlaceBetsReq')

        request.bets.PlaceBets = placeBets
        response = self.InvokeRequestExchange(exchangeId, 'placeBets', request)

        return response


    def CancelBets(self, exchangeId, cancelBets):
        '''
        Cancel a list of bets in an exchange

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param cancelBets: list of bets to be canceled
        @type cancelBets: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectExchange('CancelBetsReq')

        request.bets.CancelBets = cancelBets
        response = self.InvokeRequestExchange(exchangeId, 'cancelBets', request)

        return response


    def CancelBetsByMarket(self, exchangeId, markets):
        '''
        Cancel all bets on given markets

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param markets: list of market ids where to cancel bets
        @type markets: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectExchange('CancelBetsByMarketReq')
        request.markets = markets

        response = self.InvokeRequestExchange(exchangeId, 'cancelBetsByMarket', request)
        return response


    def UpdateBets(self, exchangeId, updateBets):
        '''
        Update a list of bets

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param updateBets: list of bets to be canceled
        @type updateBets: list

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectExchange('UpdateBetsReq')
        request.bets.UpdateBets = updateBets

        response = self.InvokeRequestExchange(exchangeId, 'updateBets', request)
        return response


    ############################################################
    # Read-Only Betting API Services
    ############################################################

    def GetActiveEventTypes(self):
        '''
        Retrieve the list of Active Event Types (top level events)

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectGlobal('GetEventTypesReq')
        return self.InvokeRequestGlobal('getActiveEventTypes', request,
                                        ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH', 'NO_RESULTS'])


    def GetAllEventTypes(self):
        '''
        Retrieve the list of all Event Types (top level events)

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectGlobal('GetEventTypesReq')

        return self.InvokeRequestGlobal('getAllEventTypes', request,
                                        ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH', 'NO_RESULTS'])


    def GetAllMarkets(self, exchangeId):
        '''
        Retrieve a list of objects with all available markets in an exchange

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetAllMarketsReq')
        return self.InvokeRequestExchange(exchangeId, 'getAllMarkets', request)


    def GetCompleteMarketPricesCompressed(self, exchangeId, marketId):
        '''
        Retrieve the complete market prices (compressed)

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetCompleteMarketPricesCompressedReq')
        return self.InvokeRequestExchange(exchangeId, 'getCompleteMarketPricesCompressed', request)


    def GetEvents(self, parentEventId):
        '''
        Retrieve a list of eventItems/marketItems for a given Active Event
        or eventItem

        @param parentEventId: id of the parent event
        @type parentEventId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
	# Create a request and fill the data
        request = self.GetRequestObjectGlobal('GetEventsReq')

        request.eventParentId = parentEventId

        return self.InvokeRequestGlobal('getEvents', request,
                                        ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH', 'NO_RESULTS'])


    def GetMarket(self, exchangeId, marketId):
        '''
        Retrieve a market object

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetMarketReq')
        request.marketId = marketId

        # 'includeCouponLinks' is optional according to the docs
        # but the server responds with an INTERNAL_ERROR if not set
        request.includeCouponLinks = False


        return self.InvokeRequestExchange(exchangeId,
                                          'getMarket', request,
                                          ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH'])


    def GetMarketInfo(self, exchangeId, marketId):
        '''
        Retrieve market information

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetMarketInfoReq')
        request.marketId = marketId

        return self.InvokeRequestExchange(exchangeId,
                                          'getMarketInfo', request,
                                          ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH'])


    def GetMarketPrices(self, exchangeId, marketId):
        '''
        Retrieve the market prices

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        return self.GetMarketPricesCompressed(exchangeId, marketId)


    def GetMarketPricesCompressed(self, exchangeId, marketId):
        '''
        Retrieve the market prices (compressed)

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param marketId: id of the market
        @type marketId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetMarketPricesCompressedReq')
        request.marketId = marketId

        return self.InvokeRequestExchange(exchangeId, 'getMarketPricesCompressed', request)


    def GetCurrentBets(self, exchangeId, betStatus, orderBy='NONE', marketId=0,
                       startRecord=0, recordCount=0, noTotalRecordCount=True):
        '''
        Retrieve a list of current bets on an exchange, according to betStatus
        marketId and ordered according to orderBy

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int
        @param betStatus: status of bets to be returned (matched, unmatched)
        @type betStatus: string (Betfair enum)
        @param orderBy: ordering criterion
        @type orderBy: string (Betfair enum)
        @param marketId: id of market to get current bets for. With 0, all bets
                         in the selected exchange will be returned
        @type marketId: int
        @param startRecord: to enable paging through long lists
        @type startRecord: int
        @param recordCount: maximum number of records to retrieve (see matchedSince)
        @type recordCount: int
        @param noTotalRecordCount: whether the total record count should be returned
        @type noTotalRecordCount: bool

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetCurrentBetsReq')

        request.betStatus = betStatus
        request.detailed = False
        request.orderBy = orderBy
        # Documentation says it is optional
        # But the WSDL says "nillable=False" and indicates that a 0 has to be passed
        # to get all bets in the exchange
        request.marketId = marketId
        request.recordCount = recordCount
        request.startRecord = startRecord
        request.noTotalRecordCount = noTotalRecordCount

        return self.InvokeRequestExchange(exchangeId, 'getCurrentBets', request,
                                          ['NO_RESULTS'])


    # Long name in Betfair's documentation for GetMUBets
    def GetMatchedAndUnmatchedBets(self, exchangeId, marketId=None,
                                   betStatus='MU', orderBy='BET_ID', sortOrder='DESC',
                                   startRecord=0, recordCount=200, excludeLastSecond=False,
                                   useMatchedSince=False, matchedSince=None):
        '''
        Alias for GetMUBets

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
        return self.GetMUBets(exchangeId, marketId=marketId,
                              betStatus=betStatus, orderBy=orderBy, sortOrder=sortOrder,
                              startRecord=startRecord, recordCount=recordCount,
                              excludeLastSecond=excludeLastSecond,
                              useMatchedSince=useMatchedSince, matchedSince=matchedSince)
            

    def GetMUBets(self, exchangeId, marketId=None, betIds=None,
                  betStatus='MU', orderBy='BET_ID', sortOrder='DESC',
                  startRecord=0, recordCount=200, excludeLastSecond=False,
                  useMatchedSince=False, matchedSince=None):
        '''
        Get Matched and Unmatched bets for a given marketId

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
        request = self.GetRequestObjectExchange('GetMUBetsReq')

        request.betStatus = betStatus
        if marketId is not None:
            request.marketId = marketId
        request.orderBy = orderBy
        # Seems to be the limit according to GetMUBets (the non-lite version)
        request.recordCount = recordCount
        request.sortOrder = sortOrder
        request.startRecord = startRecord

        # In theory this is an optional field
        request.excludeLastSecond = excludeLastSecond

        # They seem to be really optional
        if betIds is not None:
            request.betIds = betIds

        # In theory, specifying matchedSince eliminates 'recordCount' restrictions
        if useMatchedSince:
            if matchedSince is None:
                # Use a sensible default
                matchedSince = datetime(2001, 01, 01, 00, 00, 01)

            request.matchedSince = matchedSince

        return self.InvokeRequestExchange(exchangeId, 'getMUBets', request, ['NO_RESULTS'])


    def GetMarketProfitAndLoss(self, exchangeId, marketId,
                               includeBspBets=False,
                               includeSettledBets=False,
                               netOfCommission=False):
        '''
        Get Matched and Unmatched bets for a given marketId

        The param netOfCommission is optional according to the docs

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
        request = self.GetRequestObjectExchange('GetMarketProfitAndLossReq')

        # it is marketID unlike in the rest of the API calls, where it is marketId
        # request.marketID = marketId
        request.marketID = marketId
        request.includeBspBets = includeBspBets
        # Compulsory - Supposed to be optional according to the docs
        request.includeSettledBets = includeSettledBets

        # Compulsory - Supposed to be optional according to the docs
        request.netOfCommission = netOfCommission

        # For a closed market, the Api is returning 'INVALID_MARKET' instead of
        # 'MARKET_CLOSED' as stated and as returned by calls that are usually executed
        # together with this one like: GetMarketPricesCompressed/GetMarket/GetMUBets
        return self.InvokeRequestExchange(exchangeId,
                                          'getMarketProfitAndLoss', request,
                                          ['MARKET_CLOSED', 'INVALID_MARKET'])


    ############################################################
    # Account Management Betting API Services
    ############################################################

    def GetAccountFunds(self, exchangeId):
        '''
        Get Account Funds from an exchange

        @param exchangeId: id of the suds "exchange" wsdl client to use
        @type exchangeId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectExchange('GetAccountFundsReq')

        return self.InvokeRequestExchange(exchangeId, 'getAccountFunds', request)


    def TransferFunds(self, sourceWalletId, destWalletId, amount):
        '''
        Transfer funds amongst exchanges

        @param sourceWalletId: id of the suds "exchange" to use as source
        @type sourceWalletId: int
        @param destWalletId: id of the suds "exchange" to use as destination
        @type destWalletId: int
        @param amount: amount to transfer
        @type amount: float

        @returns: Betfair API answer
        @rtype: suds object
        '''
        request = self.GetRequestObjectGlobal('TransferFundsReq')

        request.sourceWalletId = sourceWalletId
        request.targetWalletId = destWalletId
        request.amount = amount

        return self.InvokeRequestGlobal('transferFunds', request);
