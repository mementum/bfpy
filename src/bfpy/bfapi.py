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
BfApi object implementation.

It does initialize suds logging to a L{NullHandler} to avoid any logging output
'''

from copy import copy
from datetime import datetime
from socket import error as SocketError

import bfglobals
import bfcounter
import bfdirect
import bferror
from bfservice import GlobalServiceDef, ExchangeServiceDef, VendorServiceDef, GlobalObject, ExchangeObject
from bfprocessors import *
import bftransport


class BfService(type):
    '''
    Metaclass for L{BfApi} to initialize the non-data descriptor based
    methods on instantiation
    '''

    def __new__(mcs, name, bases, clsdict):
        '''
        On L{BfApi} instantiation the service definitions present in
        the class variable I{serviceDefs} are added to the dictionary of the
        instance to generate non-data descriptor based methods
        that allow the invocation of the Betfair API Services
        '''
        for serviceDef in clsdict['serviceDefs']:
            clsdict[serviceDef.methodName] = serviceDef

        # support for pluggable external ApiServices
        try:
            import bfextern
        except Exception, e:
            pass
        else:
            try:
                for apiService in bfextern.ApiServices:
                    clsdict[apiService.methodName] = apiService
            except Exception, e:
                pass
    
        return type.__new__(mcs, name, bases, clsdict)
    

class BfApi(object):
    '''
    The class implements a unified communication interface with the Betfair API Services
    EndPoints (Global, ExchangeUK, ExchangeAus)

    This is done by defining the the services and object retrieval methods by means of
    non-data descriptors. The descriptors are added to the class by the metaclass {BfService}

    The class can be configured to avoid any pre/post-processing of the requests and answers
    by changing the module L{preProcess} and L{postProcess} variables or passing them as
    named arguments to the constructor

    @type preProcess: bool
    @ivar preProcess: whether service requests will undergo pre-processing
    @type preProcess: bool
    @ivar postProcess: whether service requests will undergo post-processing
    @type postProcess: bool
    @ivar maxRequests: maximum number of requests to issue to Bf in 1 second
                       (20 is maximum before data charges kick-in)
                       maxRequests = 0 to unlimit the number of requests
    @type maxRequests: int
    @ivar directApi: use the DirectAPI calls where possible
    @type directApi: bool
    @ivar fullDirect: use only the available DirectAPI calls and do not load suds
    @type fullDirect: bool
    @ivar transport: a reference to the L{BfTransport} used to communicate (HTTP)
                     with the Betfair servers
    @type transport: L{BfTransport}
    @ivar clients: the actual suds clients to generate, transport and proccess
                   the service communication
    @type clients: dict

    @ivar serviceDefs: service definitions with non-data descriptors
    @type clients: list

    The description below states if a service diverts from the standard
    behaviour and what default values have may be assigned to some variables
    to ease the usage of the services.

    The Betfair API Documentation has to be checked to call those services.

    To call a service, pass the name of the fields the service request object
    has in the Betfair docs, as named parameters. If a service request needs a
    "username" parameters, simply: service(username=myusername)

    For Exchange services, pass the exchangeId as the first parameter. It must
    be unnamed. The reason is "consistency". All Exchange services will always
    have the exchangeId as the first parameter

    The following services are defined:

        - login
          Default values:
          productId=82, vendorSoftwareId=0, ipAddress='0', locationId=0

          If a sucessfull login has been achieved, calling the function with no
          parameters will perform a re-login

        - logout
        - keepAlive

        - convertCurrency
        - getActiveEventTypes
        - getAllCurrencies
        - getAllCurrenciesV2
        - getAllEventTypes
        - getAllMarkets
        - getBet
        - getBetHistory
          Default values:
          detailed=False, orderBy='BET_ID', eventTypesId=None,
          marketId=0, marketTypesIncluded=['A', 'L', 'O', 'R'],
          startRecord=0, recordCount=0,
          placedDateFrom=now() - 1 day, placedDateTo=now(), 

        - getBetLite
        - getBetMatchesLite
        - getCompleteMarketPricesCompressed
        - getCurrentBets
          Default values:
          detailed=False, orderBy='NONE',
          marketId=0, recordCount=0,
          startRecord=0, noTotalRecordCount=True

        - getCurrentBetsLite
          Default values:
          detailed=False, orderBy='NONE',
          marketId=0, recordCount=1000,
          startRecord=0, noTotalRecordCount=True

          Unlike getCurrentBets recordCount=0 does not return all
          current bets

        - getDetailAvailableMarketDepth
          Default values:
          asianLineId=0
          
        - getEvents
        - getMarket:
          Default values: includeCouponLinks=False

        - getInPlayMarkets  
        - getMarketInfo
        - getMarketPrices
        - getMarketPricesCompressed

        - getMarketProfitAndLoss
          This function is preprocessed to try avoid an error if the user
          passes a "marketId" parameter, given the obvious typo made when
          the service was created at Betfair: it requires a marketID parameter.

          Default values:
          includeBspBets=False,
          includeSettledBets=False, netOfCommission=False,

        - getMarketTradedVolume
          Default values:
          asianLineId=0

        - getMarketTradedVolumeCompressed

        - getMUBets:
          Default values:
          betStatus='MU', excludeLastSecond=False,
          matchedSince=datetime(2000, 01, 01, 00, 00, 00),
          orderBy='BET_ID', recordCount=200,
          sortOrder='ASC', startRecord=0

        - getMUBetsLite:directApi
          Default values:
          betStatus='MU', excludeLastSecond=False,
          matchedSince=datetime(2000, 01, 01, 00, 00, 00),
          orderBy='BET_ID', recordCount=200,
          sortOrder='ASC', startRecord=0

        - getPrivateMarkets  
          Default values:
          marketType='O'

        - getSilks
        - getsilksV2

        - cancelBets
        - cancelBetsByMarket
        - placeBets
        - updateBets

        - addPaymentCard
          Default values:
          cardStatus='UNLOCKED'
          itemsIncluded='EXCHANGE', startRecord=0, recordCount=1000
          startDate=datetime.now() - timedelta(days=1), endDate=datetime.now()),
        - deletePaymentCard  
        - depositFromPaymentCard
        - forgotPassword,
        - getAccountFunds
        - getAccountStatement
          Default values:
          itemsIncluded='EXCHANGE',
          startRecord=0, recordCount=0,
          ignoreAutoTransfers=True,

        - getSubscriptionInfo
        - modifyPassword
        - modifyProfile
        - retrieveLIMBMessage
        - selfExclude
        - setChatName
        - submitLIMBMessage
        - transferFunds
        - updatePaymentCard
        - viewProfile
        - viewProfileV2
        - viewReferAndEarn
        - withdrawToPaymentCard

        - createVendorAccessRequest,
        - cancelVendorAccessRequest,
        - updateVendorSubscription,
          requestName='VendorSubscriptionReq' (non standard definition by Betfair)
          Default parameters:
            username = '' (internal Betfair use, but cannot be set to null)
        - getVendorUsers
          Default parameters:
            usernameSearchModifier='CONTAINS', customFieldSearchModifier='CONTAINS', status='ACTIVE'
        - getVendorAccessRequests
          Default parameters:
            status = ACTIVE
        - getSubscriptionInfo
          Default parameters:
            username = '' (internal Betfair use, but cannot be set to null)
        - getVendorInfo
    '''

    __metaclass__ = BfService

    def __init__(self, preProcess=bfglobals.preProcess,
                 postProcess=bfglobals.postProcess,
                 maxRequests=20,
                 directApi=True,
                 fullDirect=False,
                 **kwargs):
        '''
        Initializes the processing options, transport and service clients

        @param preProcess: whether service requests will undergo pre-processing
        @type preProcess: bool
        @param postProcess: whether service requests will undergo post-processing
        @type postProcess: bool
        @param maxRequests: maximum number of requests to issue to Bf in 1 second (20 is maximum before data charges)
                            maxRequests = 0 to unlimit the number of requests
        @type maxRequests: int
        @param directApi: use the DirectAPI calls where possible
        @type directApi: bool
        @param fullDirect: use only the available DirectAPI calls and do not load suds
        @type fullDirect: bool
        '''
        self.preProcess = preProcess
        self.postProcess = postProcess
        self.maxRequests = maxRequests
        self.fullDirect = fullDirect if not bfglobals.forceDirect else True
        self.directApi = directApi if not self.fullDirect else True
        self.dataCounter = dict()
        for endPoint in bfglobals.EndPoints:
            self.dataCounter[endPoint] = bfcounter.DataCounter(maxRequests)

        self.transport = bftransport.BfTransport()
        if 'proxydict' in kwargs:
            self.transport.setproxy(kwargs['proxydict'])

        self.transport.setuseragent(bfglobals.libstring)

        if not self.fullDirect:
            self.clients = dict()
            for endPoint, wsdlDef in bfglobals.wsdlDefs.iteritems():
                self.clients[endPoint] = bfglobals.sudsClient.Client(wsdlDef, transport=self.transport.clone())

        self.apiServices = dict()
        for endPoint in bfglobals.EndPoints:
            self.apiServices[endPoint] = bfdirect.ApiService(endPoint=endPoint, transport=self.transport.clone())


    def clone(self):
        '''
        Returns smartly cloned object.

        All objects are copied, then clients are also "cloned" themselves and
        the sessionToken is ended

        @return: a clone of itself
        @rtype: L{BfApi}
        '''
        obj = copy(self)

        if not self.fullDirect:
            for endPoint, client in self.clients.iteritems():
                obj.clients[endPoint] = client.clone()

        obj.sessionToken = ''

        return obj


    def getService(self, endPoint, serviceName):
        '''
        Returns a service from an endPoint

        @param endPoint: suds client to retrieve the service from
        @type endPoint: int
        @param serviceName: name of the service to be retrieved
        @type serviceName: str

        @return: a service to be invoked
        @rtype: directapi call or method generated by suds from the WSDL definition
        '''
        if self.directApi:
            try:
                return self.apiServices[endPoint].getService(serviceName)
            except AttributeError:
                pass

        # If not directApi or a Exception was raised, we end up here
        return getattr(self.clients[endPoint].service, serviceName)


    def getObject(self, endPoint, objectName, apiHeader=False):
        '''
        Returns an object from an endPoint

        @param endPoint: suds client to retrieve the service from
        @type endPoint: int
        @param objectName: name of the object to be retrieved
        @type objectName: str
        @param apiHeader: whether to append an APIRequestHeader to the object
        @type apiHeader: bool

        @return: the requested object and whether the object is fetched from the directApi
        @rtype: tuple (object generated by suds from the WSDL definitions or directApi boolean)
        '''
        if self.directApi:
            try:
                obj = self.apiServices[endPoint].getObject(objectName)
            except KeyError:
                pass
            else:
                if apiHeader:
                    obj.header = self.apiServices[endPoint].getObject('APIRequestHeader')
                    obj.header.clientStamp = 0
                    obj.header.sessionToken = self.sessionToken
                return obj

        # If not directApi or a Exception was raised, we end up here
        obj = self.clients[endPoint].factory.create('ns1:%s' % objectName)
        if apiHeader:
            obj.header = self.clients[endPoint].factory.create('ns1:APIRequestHeader')
            obj.header.clientStamp = 0
            obj.header.sessionToken = self.sessionToken
        return obj


    def getRequest(self, endPoint, requestName, apiHeader=True): 
        '''
        All methods pass a request object to services. Because login does
        not carry a header, we need to know if the header has to be added
        retrieves the header object

        @param endPoint: suds client to retrieve the service from
        @type endPoint: int
        @param requestName: name of the object to be retrieved
        @type requestName: str
        @param apiHeader: whether to append an APIRequestHeader to the object
        @type apiHeader: bool

        @return: the request object
        @rtype: object generated by suds from the WSDL definitions or DirectAPI type
        '''
        return self.getObject(endPoint, requestName, apiHeader)


    def addDataWeight(self, endPoint, weight):
        '''
        Adds the weight to the counter corresponding to the endPoint

        @param endPoint: which endPoint to add weight to
        @type endPoint: int
        @param weight: weight of the call to come
        @type weight: int
        '''
        self.dataCounter[endPoint].add(weight, self.maxRequests)


    def invoke(self, methodName, service, request, skipErrorCodes):
        '''
        Invokes a service with a given request and with a list of errors
        that do not generate exceptions if returned

        @param methodName: method name that has been used to invoke
        @type methodName: str
        @param service: name of the object to be retrieved
        @type service: method generated by suds from the WSDL definition
        @param skipErrorCodes: error codes that will not generate exceptions
        @type skipErrorCodes: list

        @return: the response object processed by suds
        @rtype: object generated by suds from the WSDL definitions or DirectAPI parsed type

        @raise BfHttpError: if the server does not answer with 200 OK
        @raise BfNetworkError: on (potential) network errors
        @raise Exception: on other errors, due to the fact that suds does not
                          generate all exceptions from a common base
        @raise BfApiError: on specific API errors
        @raise BfServiceError: on service errors (unless specified in skipErrorCodes)
        '''

        try:
            response = service(request)
        except bfglobals.sudsWebFault, e:
            raise bferror.BfHttpError(methodName, e, str(e), e.fault, e.document)
        except (SocketError, bftransport.TransportException), e:
            # Summarise (all potential) network errors into a generic notification
            raise bferror.BfNetworkError(methodName, e, str(e), e.args)
        except bferror.BfHttpError, e:
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


    # MinStakes = namedtuple('CurrencyMinStakes', ('minimumStake', 'minimumRangeStake', 'minimumBSPLayLiability'))
    # minimumStake, minimumRangeStake, minimumBSPLayLiability
    # MinStakes = namedtuple('CurrencyMinStakes', ('minimumStake', 'minimumRangeStake', 'minimumBSPLayLiability'))

    class MinStake(object):
        '''
        Placeholder class for minimum bets if the getAllCurrencies family cannot be used

        @ivar minimumStake: Minimum Stake for regular markets
        @type minimumstake: float
        @ivar minimumRangeStake: Minimum Stake for Range markets
        @type minimumRangestake: float
        @ivar minimumBSPLayLiability: Minimum lay stake for BSP markets
        @type minimumBSPLayLiability: float
        '''

        def __init__(self, minimumStake, minimumRangeStake, minimumBSPLayLiability):
            '''
            Init the object instance variables with the provided values
            '''
            self.minimumStake = minimumStake
            self.minimumRangeStake = minimumRangeStake
            self.minimumBSPLayLiability = minimumBSPLayLiability

    MinBets = {
        'AUD': MinStake(5.0, 3.0, 30.0),
        'CAD': MinStake(6.0, 3.0, 30.0),
        'DKK': MinStake(30.0, 15.0, 150.0),
        'EUR': MinStake(2.0, 2.0, 20.0),
        'HKD': MinStake(25.0, 15.0, 125.0),
        'NOK': MinStake(30.0, 15.0, 150.0),
        'SGD': MinStake(6.0, 1.0, 30.0),
        'SEK': MinStake(30.0, 15.0, 150.0),
        'GBP': MinStake(2.0, 1.0, 10.0),
        'USD': MinStake(4.0, 2.0, 20.0),
        }

    @staticmethod
    def getMinStakes(currency, which=None):
        '''
        Returns the minimum stakes for standard bets, range and BSP liability

        Useful for Free API applications that cannot call getAllCurrencies(V2)

        @param currency: the currency for which the minimum stakes are sought
        @type currency: str (3 letter code)
        @param which: indicates if a specific stake should be returned
        @type which: str

        @returns: the minimum stakes (minimumStake, minimumRangeStake, minimumBSPLayLiability
        @rtype: L{MinStake}
        '''
        minBets = BfApi.MinBets[currency]
        if not which:
            return minBets

        return getattr(minBets, which)


    serviceDefs = [
        # ######################
        # API Object Retrieval
        # ######################
        GlobalObject('BFEvent', eventId=-1, eventName=''),
        ExchangeObject('Market'),
        ExchangeObject('Runner'),
        ExchangeObject('MarketPrices'),
        ExchangeObject('RunnerPrices'),
        ExchangeObject('Price'),
        ExchangeObject('PlaceBets', betCategoryType='E', bspLiability=0.0),
        ExchangeObject('CancelBets'),
        ExchangeObject('UpdateBets'),
        
        # ######################
        # General API Services
        # ######################
        GlobalServiceDef('login', apiHeader=False,
                         preProc=[PreProcLogin()], postProc=[ProcLogin()],
                         productId=bfglobals.freeApiId, vendorSoftwareId=0, ipAddress='0', locationId=0),
        GlobalServiceDef('logout'),
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
        ExchangeServiceDef('getAllMarkets', preProc=[ArrayUnfix('eventTypeIds', 'int'), ArrayUnfix('countries', 'Country')],
                           postProc=[ProcAllMarkets()]),
        ExchangeServiceDef('getBet', skipErrorCodes=['NO_RESULTS'], postProc=[ArrayFix('bet.matches', 'Match')], weight=1),
        ExchangeServiceDef('getBetHistory', skipErrorCodes=['NO_RESULTS'],
                           preProc=[ArrayUnfix('marketTypesIncluded', 'MarketTypeEnum'),
                                    ArrayUnfix('eventTypeIds', 'int'),
                                    PreBetHistory()],
                           weight=-1,
                           marketId=0, detailed=False, marketTypesIncluded=['A', 'L', 'O', 'R'],
                           recordCount=100, sortBetsBy='BET_ID', startRecord=0),
        ExchangeServiceDef('getBetLite', skipErrorCodes=['NO_RESULTS'], weight=1),
        ExchangeServiceDef('getBetMatchesLite', skipErrorCodes=['NO_RESULTS'], postProc=[ArrayFix('matchLites', 'MatchLite')], weight=1),
        ExchangeServiceDef('getCompleteMarketPricesCompressed',
                           skipErrorCodes=['EVENT_CLOSED', 'EVENT_SUSPENDED', 'EVENT_INACTIVE'],
                           preProc=[PreCompleteMarketPricesCompressed()],
                           postProc=[ProcMarketPricesCompressed(True)], weight=1),
        ExchangeServiceDef('getCurrentBets', skipErrorCodes=['NO_RESULTS'], postProc=[ArrayFix('bets', 'Bet'), ProcCurrentBets()],
                           weight=-1,
                           detailed=False, orderBy='NONE', marketId=0, recordCount=0, startRecord=0, noTotalRecordCount=True),
        ExchangeServiceDef('getCurrentBetsLite', skipErrorCodes=['NO_RESULTS'], postProc=[ArrayFix('betLites', 'BetLite')],
                           weight=-1,
                           orderBy='NONE', marketId=0, recordCount=1000, startRecord=0, noTotalRecordCount=True),
        ExchangeServiceDef('getDetailAvailableMarketDepth', serviceName='getDetailAvailableMktDepth',
                           requestName='GetDetailedAvailableMktDepthReq',
                           skipErrorCodes=['NO_RESULTS', 'SUSPENDED_MARKET'],
                           postProc=[ArrayFix('priceItems', 'AvailabilityInfo')], weight=1,
                           asianLineId=0),
        GlobalServiceDef('getEvents', skipErrorCodes=['NO_RESULTS'],
                         postProc=[ArrayFix('eventItems', 'BFEvent'), ArrayFix('marketItems', 'MarketSummary')]),
        ExchangeServiceDef('getInPlayMarkets', postProc=[ProcAllMarkets()]),
        # Documentation incorrectly states that includeCouponLinks is optional
        ExchangeServiceDef('getMarket', postProc=[ArrayFix('market.runners', 'Runner'), ArrayFix('market.eventHierarchy', 'eventId'), ProcMarket()], includeCouponLinks=False),
        ExchangeServiceDef('getMarketInfo'),
        ExchangeServiceDef('getMarketPrices', postProc=[ProcMarketPrices()], weight=1),
        ExchangeServiceDef('getMarketPricesCompressed', postProc=[ProcMarketPricesCompressed()], weight=1),
        ExchangeServiceDef('getMarketTradedVolume', skipErrorCodes=['NO_RESULTS', 'MARKET_CLOSED'],
                           postProc=[ArrayFix('priceItems', 'VolumeInfo')], weight=1,
                           asianLineId=0),
        ExchangeServiceDef('getMarketTradedVolumeCompressed', skipErrorCodes=['EVENT_SUSPENDED', 'EVENT_CLOSED'],
                           preProc=[PreMarketTradedVolumeCompressed()],
                           postProc=[ProcMarketTradedVolumeCompressed()], weight=1),
        ExchangeServiceDef('getMUBets', preProc=[ArrayUnfix('betIds', 'betId')],
                           postProc=[ArrayFix('bets', 'MUBet')],
                           skipErrorCodes=['NO_RESULTS'], weight=-1,
                           betStatus='MU', excludeLastSecond=False,
                           matchedSince=datetime(2000, 01, 01, 00, 00, 00),
                           orderBy='BET_ID', recordCount=200, sortOrder='ASC', startRecord=0),
        ExchangeServiceDef('getMUBetsLite', preProc=[ArrayUnfix('betIds', 'betId')],
                           postProc=[ArrayFix('betLites', 'MUBetLite')],
                           skipErrorCodes=['NO_RESULTS'], weight=-1,
                           betStatus='MU', excludeLastSecond=False,
                           matchedSince=datetime(2000, 01, 01, 00, 00, 00),
                           orderBy='BET_ID', recordCount=200, sortOrder='ASC', startRecord=0),
        ExchangeServiceDef('getMarketProfitAndLoss',
                           skipErrorCodes=['MARKET_CLOSED', 'INVALID_MARKET'],
                           preProc=[PreProcMarketProfitAndLoss()],
                           postProc=[ArrayFix('annotations', 'ProfitAndLoss'), ProcMarketProfitAndLoss()], weight=1,
                           includeBspBets=False, includeSettledBets=False, netOfCommission=False),
        ExchangeServiceDef('getPrivateMarkets', skipErrorCodes=['NO_RESULTS'],
                           preProc=[PreProcPrivateMarkets()], postProc=[ArrayFix('privateMarkets', 'PrivateMarket')],
                           marketType='O'),
        ExchangeServiceDef('getSilks', preProc=[ArrayUnfix('markets', 'int')], postProc=[ProcSilks()]),
        ExchangeServiceDef('getSilksV2', preProc=[ArrayUnfix('markets', 'int')], postProc=[ProcSilks()]),

        # ######################,
        # Bet Placement API Services
        # ######################
        ExchangeServiceDef('cancelBets', preProc=[ArrayUnfix('bets', 'CancelBets')],
                           postProc=[ArrayFix('betResults', 'CancelBetsResult')]),
        ExchangeServiceDef('cancelBetsByMarket', preProc=[ArrayUnfix('markets', 'int')],
                           postProc=[ArrayFix('results', 'CancelBetsByMarketResult')]),
        ExchangeServiceDef('placeBets', preProc=[ArrayUnfix('bets', 'PlaceBets')],
                           postProc=[ArrayFix('betResults', 'PlaceBetsResult')]),
        ExchangeServiceDef('updateBets', preProc=[ArrayUnfix('bets', 'UpdateBets')],
                           postProc=[ArrayFix('betResults', 'UpdateBetsResult')]),

        # ######################
        # Acount Management API Services
        # ######################
        GlobalServiceDef('addPaymentCard', cardStatus='UNLOCKED'),
        GlobalServiceDef('deletePaymentCard'),
        GlobalServiceDef('depositFromPaymentCard'),
        GlobalServiceDef('forgotPassword'),
        ExchangeServiceDef('getAccountFunds'),
        ExchangeServiceDef('getAccountStatement', skipErrorCodes=['NO_RESULTS'],
                           preProc=[PreAccountStatement()],
                           postProc=[ArrayFix('items', 'AccountStatementItem')],
                           itemsIncluded='EXCHANGE', startRecord=0, recordCount=1, ignoreAutoTransfers=True),
        GlobalServiceDef('getPaymentCard', postProc=[ArrayFix('paymentCardItems', 'PaymentCard')]),
        GlobalServiceDef('getSubscriptionInfo', postProc=[ArrayFix('subscriptions', 'Subscription'),
                                                          ArrayFix('subscriptions.services', 'ServiceCall')]),
        GlobalServiceDef('modifyPassword'),
        GlobalServiceDef('modifyProfile'),
        GlobalServiceDef('retrieveLIMBMessage',
                         postProc=[ArrayFix('retrieveCardBillingAddressCheckItems', 'retrieveCardBillingAddressCheckLIMBMessage')]),
        GlobalServiceDef('selfExclude'),
        GlobalServiceDef('setChatName'),
        GlobalServiceDef('submitLIMBMessage', preProc=[ArrayUnfix('submitCardBillingAddressCheckItems',
                                                                  'SubmitCardBillingAddressCheckLIMBMessage')]),
        GlobalServiceDef('transferFunds'),
        GlobalServiceDef('updatePaymentCard'),
        GlobalServiceDef('viewProfile'),
        GlobalServiceDef('viewProfileV2'),
        GlobalServiceDef('viewReferAndEarn', skipErrorCodes=['NO_RESULTS']),
        GlobalServiceDef('withdrawToPaymentCard'),

        # ######################
        # Vendor API Services
        # ######################
        VendorServiceDef('createVendorAccessRequest'),
        VendorServiceDef('cancelVendorAccessRequest'),
        VendorServiceDef('updateVendorSubscription', requestName='VendorSubscriptionReq',
                         username=''),
        # The 3 parameters below are declared as "N" (non-mandatory) in the docs, but the WSDL
        # requires them and if not provided an INTERNAL ERROR is generated
        VendorServiceDef('getVendorUsers', postProc=[ArrayFix('vendorUsers', 'vendorUser')],
                         usernameSearchModifier='CONTAINS', customFieldSearchModifier='CONTAINS', status='ACTIVE'),
        # status below is declared as "N" (non-mandatory) in the docs, but the WSDL
        # requires it and if not provided an INTERNAL ERROR is generated
        VendorServiceDef('getVendorAccessRequests', postProc=[ArrayFix('vendorAccessRequests', 'vendorAccessRequest')],
                         status='ACTIVE'),
        VendorServiceDef('getSubscriptionInfo',
                         username=''),
        VendorServiceDef('getVendorInfo', postProc=[ArrayFix('vendorInfo', 'vsInfo')]),
        ]
