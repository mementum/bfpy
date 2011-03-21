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
Definition of direct construction API call and services
and metaclass to install them in an API provider
'''

# FIXME: Add timezone to time when sending it as param (matchedSince, fromDate)

import types

from bftransport import sRequest

import bfglobals
import bfsoap
import bftypes


class ApiCall(object):
    '''
    Non-data descriptor class to be installed in L{ApiService}

    @type nsGlobal: string
    @cvar nsGlobal: soap namespace for Global Api Services
    @type nsGlobalTypes: string
    @cvar nsGlobalTypes: soap namespace for Global Api Types
    @type nsExchange: string
    @cvar nsExchange: soap namespace for Exchange Api Services
    @type nsExchangeTypes: string
    @cvar nsExchangeTypes: soap namespace for Global Api Types
    @type soappattern: string
    @cvar soappattern: basic string pattern with substitution patterns to form
                       the final soap message

    @type instanceCache: dict
    @ivar instanceCache: cache for instances during descriptor operation
    @type pattern: string
    @ivar pattern: holds the prepared soap message patter
    @type ns: string
    @ivar ns: namespace where this call was defined
    @type resulttag: string
    @ivar resulttag: convenient string to look for the "Result" object in responses
    @type httpreq: bftransport.TransportDirect
    @ivar httpreq: http request holder
    '''
    nsGlobal = 'http://www.betfair.com/publicapi/v3/BFGlobalService/'
    nsGlobalTypes = 'http://www.betfair.com/publicapi/types/global/v3/'

    nsExchange = 'http://www.betfair.com/publicapi/v5/BFExchangeService/'
    nsExchangeTypes = 'http://www.betfair.com/publicapi/types/exchange/v5/'

    soappattern = '''<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="$$ns1$$" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ns2="$$ns2$$" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Header/>
<ns0:Body>
<ns1:$$operation$$>
$$request$$
</ns1:$$operation$$>
</ns0:Body>
</SOAP-ENV:Envelope>'''

    def __init__(self, exchange, operation):
        '''
        Initializes most of the pattern and the HTTP request, leaving just the last second
        specific value substitutions for the soap call

        @type exchange: boolean
        @param exchange: if the call is defined in the Global or Exchange namespace
        @type operation: string
        @param operation: name of the call
        '''
        self.instanceCache = dict()

        self.pattern = self.soappattern

        self.ns = self.nsGlobal if not exchange else self.nsExchange
        self.ns2 = self.nsGlobalTypes if not exchange else self.nsExchangeTypes
        self.resulttag = '{%s}Result' % self.ns
        self.pattern = self.patternSub('ns1', self.ns)
        self.pattern = self.patternSub('ns2', self.ns2)

        self.operation = operation
        self.pattern = self.patternSub('operation', self.operation)

        self.httpreq = sRequest('', None)
        self.httpreq.headers['Content-type'] = 'text/xml; charset=utf-8'
        self.httpreq.headers['User-agent'] = bfglobals.libstring
        self.httpreq.headers['SoapAction'] = '"%s"' % self.operation


    def patternSub(self, name, value):
        '''
        Initializes most of the pattern and the HTTP request, leaving just the last second
        specific value substitutions for the soap call

        @type name: string
        @param name: pattern name to be substituted in the soap message
        @type value: string
        @param value: the string to put into the soap message
        '''
        return self.pattern.replace('$$%s$$' % name, value)


    def __get__(self, instance, owner):
        '''
        Non-data descriptor implementation.

        It returns a method type pointing to itself. This forces the invocation of __call__

        @type instance: instance of class
        @param instance: instance that calls the descriptor
        @type owner: class
        @param owner: the class that holds the descriptor
        '''
        return self.instanceCache.setdefault(instance, types.MethodType(self, instance, owner))


    def __call__(self, instance, request):
        '''
        Invoked as method by L{ApiService} instances. It receives the instance and a request

        It finishes preparation of the soap message with the value of the request object and
        also the preparation of the http request.

        Invokes the http request, the parsing of the soap and return the "Result" part of the
        entire response

        @type instance: an object
        @param instance: object that is invoking the descriptor
        @type request: L{ApiDataType}
        @param request: the request to be sent to the servers
        '''
        self.httpreq.url = instance.endPointUrl

        # 'Calling' the request delivers the content
        self.httpreq.message = self.patternSub('request', request())

        # print "sending httpreq %s" % self.httpreq
        reply = instance.transport.send(self.httpreq)
        # print "reply is %s" % reply

        response = bfsoap.soap_process(reply.message)
        # print "xml response: %s" % str(response)

        # return getattr(response, self.resulttag)
        # return getattr(response, 'Result')
        return response.Result


class ApiCallGlobal(ApiCall):
    '''
    Specialized version of L{ApiCall} for Global calls
    '''

    def __init__(self, operation):
        '''
        Initializes the parent class with exchange set to False

        @type operation: string
        @param operation: name of the call
        '''
        ApiCall.__init__(self, exchange=False, operation=operation)


class ApiCallExchange(ApiCall):
    '''
    Specialized version of L{ApiCall} for Exchange calls
    '''

    def __init__(self, operation):
        '''
        Initializes the parent class with exchange set to True

        @type operation: string
        @param operation: name of the call
        '''
        ApiCall.__init__(self, exchange=True, operation=operation)


class ApiServiceMeta(type):
    '''
    Metaclass for L{ApiService} that install L{ApiCall} and L{ApiDataType}
    as descriptors and values into a dictionary to enable ApiService to
    return the values via member retrieval or with getService and getObject
    '''

    def __new__(cls, name, bases, clsdict):
        '''
        Modifies L{ApiService} class creation

        @type cls: class
        @param cls: the class to be modifies on creation
        @type name: string
        @param name: name of the class
        @type bases: list
        @param bases: list of base classes for cls
        @type clsdict: dict
        @param clsdict: the dictionary of cls
        '''

        for apiCall in clsdict['apiCalls']:
            clsdict[apiCall.operation] = apiCall

        clsdict['objects'] = {}
        for apiType in bftypes.ApiDataTypes:
            clsdict['objects'][apiType.__name__] = apiType
            
        return type.__new__(cls, name, bases, clsdict)


class ApiService(object):
    '''
    Holds L{ApiCall} descriptors and L{ApiDataType} classes to enable
    direct interaction with a Betfair service

    @type apiCalls: list
    @cvar apiCalls: list of ApiCalls to install

    @type endPointUrl: string
    @ivar endPointUrl: url to the service
    @type transport: L{BfTransport}
    @ivar transport: transport (over http) object
    '''

    __metaclass__ = ApiServiceMeta

    apiCalls = [
        ApiCallGlobal('login'),
        ApiCallGlobal('keepAlive'),
        ApiCallGlobal('logout'),
        ApiCallGlobal('getActiveEventTypes'),
        ApiCallGlobal('getEvents'),
        ApiCallExchange('getAllMarkets'),
        ApiCallExchange('getAccountFunds'),
        ApiCallGlobal('transferFunds'),
        ApiCallExchange('getCurrentBets'),
        ApiCallExchange('getMarket'),
        ApiCallExchange('getMarketPricesCompressed'),
        ApiCallExchange('getCompleteMarketPricesCompressed'),
        ApiCallExchange('getMarketTradedVolumeCompressed'),
        ApiCallExchange('getMarketProfitAndLoss'),
        ApiCallExchange('getMUBets'),
        ApiCallExchange('placeBets'),
        ApiCallExchange('cancelBets'),
        ApiCallExchange('updateBets'),
        ]

    # ApiCallExchange('updateBets'),

    def __init__(self, endPoint, transport):
        '''
        Initializes the parent class with exchange set to True

        @type endPoint: int
        @param endPoint: which enpoint will do the call
        @type transport: L{BfTransport}
        @param transport: transport (over http) object
        '''
        self.endPointUrl = bfglobals.EndPointUrls[endPoint]
        self.transport = transport


    def getObject(self, name):
        '''
        Returns an L{ApiDataType} by name

        @type name: string
        @param name: the object to be returned
        '''
        return self.objects[name]()


    def getService(self, name):
        '''
        Returns an L{ApiCall} by name

        @type name: string
        @param name: the api call to be returned
        '''
        return getattr(self, name)
