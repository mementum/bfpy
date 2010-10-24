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

from collections import namedtuple
from datetime import datetime
from socket import error as SocketError

import suds.client

import bferror
from bfservice import BfService, GlobalServiceDef, ExchangeServiceDef, GlobalObject, ExchangeObject
from bfpostproc import *
import bftransport
import bfwsdl

postProcess = True
rootEventId = -1

Global = 0
ExchangeUK = 1
ExchangeAus = 2


class BfApi(object):

    __metaclass__ = BfService

    Global = Global
    ExchangeUK = ExchangeUK
    ExchangeAus = ExchangeAus

    wsdlDefs = {
        Global: bfwsdl.BFGlobalService,
        ExchangeUK: bfwsdl.BFExchangeService,
        ExchangeAus: bfwsdl.BFExchangeServiceAus
        }


    def __init__(self, postProcess=postProcess, **kwargs):
        self.postProcess = postProcess

        self.transport = bftransport.BfTransport()
        self.clients = dict()
        for endPoint, wsdlDef in self.wsdlDefs.iteritems():
            self.clients[endPoint] = suds.client.Client(wsdlDef, transport=self.transport.clone())


    def getService(self, endPoint, serviceName):
        try:
            return getattr(self.clients[endPoint].service, serviceName)
        except AttributeError:
            raise bferror.BfPythonError(serviceName, self.clients[endPoint], 'Method not found')


    def getObject(self, endPoint, objectName):
        return self.clients[endPoint].factory.create('ns1:%s' % objectName)


    def getHeader(self, endPoint):
        header = self.getObject(endPoint, 'APIRequestHeader')

	header.clientStamp = 0
	header.sessionToken = self.sessionToken

        return header


    def getRequest(self, endPoint, requestName, apiHeader=True): 
        request = self.getObject(endPoint, requestName)

        if apiHeader:
            request.header = self.getHeader(endPoint)

        return request


    def invoke(self, methodName, service, request, skipErrorCodes):
        try:
            response = service(request)
        except suds.WebFault, e:
            raise bferror.BfHttpError(methodName, e, str(e), e.fault, e.document)
        except (SocketError, bftransport.TransportException), e:
            # Summarise (all potential) network errors into a generic notification
            raise bferror.BfNetworkError(methodName, e, str(e), e.args)
        except Exception, e:
            # Catch all - needed because suds doesn't have a root class Exception
            # and also produces some standard exceptions
            raise bferror.BfError(methodName, e, str(e), e.args)

        # Analyze API errorCodes
        if response.header.errorCode != 'OK':
            raise bferror.BfApiError(methodName, response, str(response), response.header.errorCode)

        # Analyze Service errorCodes - keepAlive (at least) has no "errorCode" field
        if hasattr(response, 'errorCode'):
            if response.errorCode != 'OK' and response.errorCode not in skipErrorCodes:
                raise bferror.BfServiceError(methodName, response, str(response), response.errorCode)

        # Save the latest session token
        self.sessionToken = response.header.sessionToken
        
        return response


    MinStakes = namedtuple('CurrencyMinStakes', ('minimumStake', 'minimumRangeStake', 'minimumBSPLayLiability'))
    # minimumStake, minimumRangeStake, minimumBSPLayLiability
    MinBets = {
        'AUD': MinStakes(5.0, 3.0, 30.0),
        'CAD': MinStakes(6.0, 3.0, 30.0),
        'DKK': MinStakes(30.0, 15.0, 150.0),
        'EUR': MinStakes(2.0, 2.0, 20.0),
        'HKD': MinStakes(25.0, 15.0, 125.0),
        'NOK': MinStakes(30.0, 15.0, 150.0),
        'SGD': MinStakes(6.0, 1.0, 30.0),
        'SEK': MinStakes(30.0, 15.0, 150.0),
        'GBP': MinStakes(2.0, 1.0, 10.0),
        'USD': MinStakes(4.0, 2.0, 20.0),
        }

    @staticmethod
    def GetMinStakes(currency):
        '''
        Returns the minimum stakes for standard bets, range and BSP liability

        @param currency: the currency for which the minimum stakes are sought
        @type currency: str (3 letter code)

        @returns: the minimum stakes (minimumStake, minimumRangeStake, minimumBSPLayLiability
        @rtype: namedtuple
        '''
        return self.MinBets[currency]

    serviceDefs = [
        # ######################
        # API Object Retrieval
        # ######################
        GlobalObject('Event', eventId=-1, eventName=''),
        ExchangeObject('Market'),
        ExchangeObject('Runner'),
        ExchangeObject('MarketPrices'),
        ExchangeObject('RunnerPrices'),
        ExchangeObject('Price'),
        ExchangeObject('PlaceBets'),
        ExchangeObject('CancelBets'),
        ExchangeObject('UpdateBets'),
        
        # ######################
        # General API Services
        # ######################
        GlobalServiceDef('login', apiHeader=False, postProc=[ProcLogin()],
                         productId=82, vendorSoftwareId=0, ipAddress='0', locationId=0),
        GlobalServiceDef('logout', postProc=[ProcLogout()]),
        GlobalServiceDef('keepAlive'),

        # ######################
        # Read-Only API Services
        # ######################
        GlobalServiceDef('convertCurrency'),
        GlobalServiceDef('getActiveEventTypes', requestName='GetEventTypesReq', skipErrorCodes=['NO_RESULTS'],
                         postProc=[ArrayFix('eventTypeItems', 'EventType')]),
        GlobalServiceDef('getAllCurrencies', requestName='GetCurrenciesReq', postProc=[ArrayFix('currencyItems', 'Currency')]),
        GlobalServiceDef('getAllCurrenciesV2', requestName='GetCurrenciesV2Req', postProc=[ArrayFix('currencyItems', 'CurrencyV2')]),
        GlobalServiceDef('getAllEventTypes', requestName='GetEventTypesReq', skipErrorCodes=['NO_RESULTS'],
                         postProc=[ArrayFix('eventTypeItems', 'EventType')]),
        ExchangeServiceDef('getAllMarkets', postProc=[ProcAllMarkets()]),
        # MISSING GetBet
        # MISSING GetBetHistory
        # MISSING GetBetLite
        # MISSING GetBetMatchesLite
        ExchangeServiceDef('getCompleteMarketPricesCompressed', postProc=[ProcMarketPricesCompressed(True)]),
        ExchangeServiceDef('getCurrentBets', skipErrorCodes=['NO_RESULTS'], postProc=[ArrayFix('bets', 'Bet'), ProcCurrentBets()],
                           detailed=False, orderBy='NONE', marketId=0, recordCount=0, startRecord=0, noTotalRecordCount=True),
        # MISSING GetCurrentBetsLite
        # MISSING GetDetailAvailableMarketDepth
        GlobalServiceDef('getEvents', skipErrorCodes=['NO_RESULTS'],
                         postProc=[ArrayFix('eventItems', 'BFEvent'), ArrayFix('marketItems', 'MarketSummary')]),
        ExchangeServiceDef('getInPlayMarkets', postProc=[ProcAllMarkets()]),
        # Documentation incorrectly says that includeCouponLinks is optional
        ExchangeServiceDef('getMarket', postProc=[ProcMarket()], includeCouponLinks=False),
        ExchangeServiceDef('getMarketInfo'),
        # MISSING GetMarketPrices
        ExchangeServiceDef('getMarketPricesCompressed', postProc=[ProcMarketPricesCompressed()]),
        # XXX MISSING GetMUBets
        ExchangeServiceDef('getMUBets', postProc=[ArrayFix('bets', 'MUBet')],
                           excludeLastSecond=False, matchedSince=datetime(2000, 01, 01, 00, 00, 00),
                           orderBy='BET_ID', recordCount=200, sortOrder='ASC', startRecord=0),
        # MISSING GetMUBetsLite
        ExchangeServiceDef('getMarketProfitAndLoss',
                           skipErrorCodes=['MARKET_CLOSED', 'INVALID_MARKET'],
                           postProc=[ArrayFix('annotations', 'ProfitAndLoss'), ProcMarketProfitAndLoss],
                           includeSettledBets=False, netOfComission=False),
        # MISSING GetMarketTradedVolume
        # MISSING GetMarketTradedVolumeCompressed
        # MISSING GetPrivateMarkets
        # MISSING GetSilks
        # MISSING GetSilkV2

        # ######################,
        # Bet Placement API Services
        # ######################
        ExchangeServiceDef('cancelBets', postProc=[ArrayFix('betResults', 'CancelBetsResult')]),
        ExchangeServiceDef('cancelBetsByMarket', postProc=[ArrayFix('results', 'CancelBetsByMarketResults')]),
        ExchangeServiceDef('placeBets', postProc=[ArrayFix('betResults', 'PlaceBetsResult')]),
        ExchangeServiceDef('updateBets', postProc=[ArrayFix('betResults', 'UpdateBetsResult')]),

        # ######################
        # Acount Management API Services
        # ######################
        ExchangeServiceDef('getAccountFunds'),
        GlobalServiceDef('transferFunds'),

        # MISSING All other Account Management Services
        ]
