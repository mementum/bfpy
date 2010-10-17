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

###############################################################################
# Standard Python Library imports
###############################################################################
from copy import copy
from collections import namedtuple
from datetime import datetime
from socket import error as SocketError
from threading import Lock

###############################################################################
# suds import
###############################################################################
import suds
    
###############################################################################
# suds logging configuration
###############################################################################
import logging

class NullHandler(logging.Handler):
    def emit(self, record):
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


###############################################################################
# Internal package imports
###############################################################################
import bferror
import bftransport
import bfwsdl

###############################################################################
# Variables and Classes
###############################################################################

RootEventId = -1

GlobalService = 0
ExchangeUk = 1
ExchangeAus = 2

freeApi = 82

MarketTuple = namedtuple('MarketTuple', ('exchangeId', 'marketId'))

class BfApi(object):
    # default send receive timeout
    classTimeout = 14

    # socket.setdefaulttimeout(classTimeout)

    WsdlFiles = {
        GlobalService: bfwsdl.BFGlobalService,
        ExchangeUk: bfwsdl.BFExchangeService,
        ExchangeAus: bfwsdl.BFExchangeServiceAus
        }

    def __init__(self, **kwargs):
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
        return self.Clone()


    def Clone(self):
        clone = copy(self)

        clone.bfClient = dict()
        for key, bfClient in self.bfClient.iteritems():
            clone.bfClient[key] = bfClient.clone()
                
        clone.sessionToken = ''
        return clone


    def GetAPIRequestHeader(self, reqObjName, bfServiceId):
        # Check if we are logged in
        if(self.sessionToken == ''):
            raise bfapi.BfApiError(reqObjName[:-3], None, 'No Session Token available', 'NO_SESSION')

	# Create the keepaliverequest and associated data objects
        header = self.GetObject('APIRequestHeader', bfServiceId)

	header.clientStamp = 0
	header.sessionToken = self.sessionToken

        return header


    def GetObject(self, objectName, bfServiceId):
        return self.bfClient[bfServiceId].factory.create('ns1:%s' % objectName)


    def GetObjectExchange(self, objectName, exchangeId=ExchangeUk):
        return self.GetObject(objectName, exchangeId)


    def GetObjectGlobal(self, objectName):
        return self.GetObject(objectName, GlobalService)


    def GetRequestObject(self, reqObjectName, bfServiceId, addHeader=True):
        reqObject =  self.GetObject(reqObjectName, bfServiceId)

        if addHeader == True:
            reqObject.header = self.GetAPIRequestHeader(reqObjectName, bfServiceId)

        return reqObject


    def GetRequestObjectGlobal(self, requestObjectName, addHeader=True):
        return self.GetRequestObject(requestObjectName, GlobalService, addHeader)


    def GetRequestObjectExchange(self, requestObjectName, exchangeId=ExchangeUk):
        return self.GetRequestObject(requestObjectName, exchangeId, addHeader=True)


    def InvokeRequest(self, bfServiceId, requestName, requestArg, goodErrorCodes=None):
        if hasattr(self.bfClient[bfServiceId].service, requestName) == True:
            method = getattr(self.bfClient[bfServiceId].service, requestName)
        else:
            raise bferror.BfPythonError(requestName, self.bfClient[bfServiceId], 'Method Not found')

        try:
            response = method(requestArg)
        except suds.WebFault, e:
            raise bferror.BfHttpError(requestName, e, str(e), e.fault, e.document)
        except (SocketError, bftransport.TransportException), e:
            raise bferror.BfNetworkError(requestName, e, str(e), e.args)
        except Exception, e:
            raise bferror.BfError(requestName, e, str(e), e.args)

        if response.header.errorCode != 'OK':
            raise bferror.BfApiError(requestName, response, str(response), response.header.errorCode)

        if hasattr(response, 'errorCode'):
            if not (response.errorCode == 'OK' or (goodErrorCodes and response.errorCode in goodErrorCodes)):
                raise bferror.BfServiceError(requestName, response, str(response), response.errorCode)

        self.sessionToken = response.header.sessionToken
        return response


    def InvokeRequestGlobal(self, requestName, requestArg, goodErrorCodes=None):
        return self.InvokeRequest(GlobalService, requestName, requestArg, goodErrorCodes)


    def InvokeRequestExchange(self, exchangeId, requestName, requestParam, goodErrorCodes=None):
        return self.InvokeRequest(exchangeId, requestName, requestParam, goodErrorCodes)


    ############################################################
    # Services
    ############################################################

    ############################################################
    # General API Services
    ############################################################

    def Login(self, username, password, productId=82, vendorSoftwareId=0):
        request = self.GetRequestObjectGlobal('LoginReq', addHeader=False)

	request.username = username
	request.password = password
	request.productId = productId
	request.vendorSoftwareId = vendorSoftwareId

	request.ipAddress = '0'
	request.locationId = 0

        return self.InvokeRequestGlobal('login', request);


    def Logout(self):
        request = self.GetRequestObjectGlobal('LogoutReq')
        return self.InvokeRequestGlobal('logout', request);

	
    def KeepAlive(self):
        request = self.GetRequestObjectGlobal('KeepAliveReq')
        return self.InvokeRequestGlobal('keepAlive', request);


    ############################################################
    # Bet Placement API Services
    ############################################################

    def PlaceBets(self, exchangeId, placeBets):
	# Create a request and fill the data
        request = self.GetRequestObjectExchange('PlaceBetsReq')

        request.bets.PlaceBets = placeBets
        response = self.InvokeRequestExchange(exchangeId, 'placeBets', request)

        return response


    def CancelBets(self, exchangeId, cancelBets):
	# Create a request and fill the data
        request = self.GetRequestObjectExchange('CancelBetsReq')

        request.bets.CancelBets = cancelBets
        response = self.InvokeRequestExchange(exchangeId, 'cancelBets', request)

        return response


    def CancelBetsByMarket(self, exchangeId, markets):
        # NOT AVAILABLE IN FREE API

	# Create a request and fill the data
        request = self.GetRequestObjectExchange('CancelBetsByMarketReq')
        request.markets = markets

        response = self.InvokeRequestExchange(exchangeId, 'cancelBetsByMarket', request)
        return response


    def UpdateBets(self, exchangeId, updateBets):

	# Create a request and fill the data
        request = self.GetRequestObjectExchange('UpdateBetsReq')
        request.bets.UpdateBets = updateBets

        response = self.InvokeRequestExchange(exchangeId, 'updateBets', request)
        return response


    ############################################################
    # Read-Only Betting API Services
    ############################################################

    def GetActiveEventTypes(self):
	# Create a request and fill the data
        request = self.GetRequestObjectGlobal('GetEventTypesReq')
        return self.InvokeRequestGlobal('getActiveEventTypes', request,
                                        ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH', 'NO_RESULTS'])


    def GetAllEventTypes(self):
	# Create a request and fill the data
        request = self.GetRequestObjectGlobal('GetEventTypesReq')

        return self.InvokeRequestGlobal('getAllEventTypes', request,
                                        ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH', 'NO_RESULTS'])


    def GetAllMarkets(self, exchangeId):
        request = self.GetRequestObjectExchange('GetAllMarketsReq')
        return self.InvokeRequestExchange(exchangeId, 'getAllMarkets', request)


    def GetCompleteMarketPricesCompressed(self, exchangeId, marketId):
        request = self.GetRequestObjectExchange('GetCompleteMarketPricesCompressedReq')
        return self.InvokeRequestExchange(exchangeId, 'getCompleteMarketPricesCompressed', request)


    def GetCurrentBets(self, exchangeId, betStatus, orderBy='NONE', marketId=0):
        request = self.GetRequestObjectExchange('GetCurrentBetsReq')

        request.betStatus = betStatus
        request.detailed = False
        request.orderBy = orderBy
        # Documentation says it is optional
        # But the WSDL says "nillable=False" and indicates that a 0 has to be passed
        # to get all bets in the exchange
        request.marketId = marketId
        request.recordCount = 0
        request.startRecord = 0
        request.noTotalRecordCount = True

        return self.InvokeRequestExchange(exchangeId, 'getCurrentBets', request,
                                          ['NO_RESULTS'])


    def GetEvents(self, parentEventId):
	# Create a request and fill the data
        request = self.GetRequestObjectGlobal('GetEventsReq')

        request.eventParentId = parentEventId

        return self.InvokeRequestGlobal('getEvents', request,
                                        ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH', 'NO_RESULTS'])


    def GetMarket(self, exchangeId, marketId):
        request = self.GetRequestObjectExchange('GetMarketReq')
        request.marketId = marketId

        # 'includeCouponLinks' is optional according to the docs
        # but the server responds with an INTERNAL_ERROR if not set
        request.includeCouponLinks = False


        return self.InvokeRequestExchange(exchangeId,
                                          'getMarket', request,
                                          ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH'])


    def GetMarketInfo(self, exchangeId, marketId):
        request = self.GetRequestObjectExchange('GetMarketInfoReq')
        request.marketId = marketId

        return self.InvokeRequestExchange(exchangeId,
                                          'getMarketInfo', request,
                                          ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH'])


    def GetMarketPrices(self, exchangeId, marketId):
        return self.GetMarketPricesCompressed(exchangeId, marketId)


    def GetMarketPricesCompressed(self, exchangeId, marketId):
        request = self.GetRequestObjectExchange('GetMarketPricesCompressedReq')
        request.marketId = marketId

        return self.InvokeRequestExchange(exchangeId, 'getMarketPricesCompressed', request)


    # Long name in Betfair's documentation for GetMUBets
    def GetMatchedAndUnmatchedBets(self, exchangeId, marketId):
        return self.GetMUBets(exchangeId, marketId)


    def GetMUBets(self, exchangeId, marketId):
        request = self.GetRequestObjectExchange('GetMUBetsReq')

        request.betStatus = 'MU'
        request.marketId = marketId
        request.orderBy = 'BET_ID'
        # Seems to be the limit according to GetMUBets (the non-lite version)
        request.recordCount = 200
        request.sortOrder = 'DESC'
        request.startRecord = 0

        # In theory this is an optional field
        request.excludeLastSecond = False

        # They seem to be really optional
        # request.betIds = list()
        # In theory, specifying matchedSince eliminates 'recordCount' restrictions
        request.matchedSince = datetime(2001, 01, 01, 00, 00, 01)

        return self.InvokeRequestExchange(exchangeId, 'getMUBets', request, ['NO_RESULTS'])


    def GetMarketProfitAndLoss(self, exchangeId, marketId):
        request = self.GetRequestObjectExchange('GetMarketProfitAndLossReq')

        # it is marketID unlike in the rest of the API calls, where it is marketId
        # request.marketID = marketId
        request.marketID = marketId
        request.includeBspBets = False
        request.includeSettledBets = False
        request.netOfCommission = False

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
        request = self.GetRequestObjectExchange('GetAccountFundsReq')

        return self.InvokeRequestExchange(exchangeId, 'getAccountFunds', request)


    def TransferFunds(self, sourceWalletId, destWalletId, amount):
        request = self.GetRequestObjectGlobal('TransferFundsReq')

        request.sourceWalletId = sourceWalletId
        request.targetWalletId = destWalletId
        request.amount = amount

        return self.InvokeRequestGlobal('transferFunds', request);
