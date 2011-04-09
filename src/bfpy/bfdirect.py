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

# FIXME: Add local timezone to date params before textTranslation (matchedSince, fromDate)

import types

from bftransport import sRequest

import bfapicalls
import bfglobals
import bfsoap
import bftypes


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

        for apiCall in clsdict['ApiCalls']:
            clsdict[apiCall.operation] = apiCall

        clsdict['objects'] = {}
        for apiType in bftypes.ApiDataTypes:
            clsdict['objects'][apiType.__name__] = apiType

        # Support pluggable extern Api Calls & Types
        try:
            import bfextern
        except Exception, e:
            pass
        else:
            try:
                for apiCall in bfextern.ApiCalls:
                    clsdict[apiCall.operation] = apiCall
            except:
                pass

            try:
                for apiType in bfextern.ApiDataTypes:
                    clsdict['objects'][apiType.__name__] = apiType
            except:
                pass
            
        return type.__new__(cls, name, bases, clsdict)


class ApiService(object):
    '''
    Holds L{ApiCall} descriptors and L{ApiDataType} classes to enable
    direct interaction with a Betfair service

    @type ApiCalls: list
    @cvar ApiCalls: list of ApiCalls to install

    @type endPointUrl: string
    @ivar endPointUrl: url to the service
    @type transport: L{BfTransport}
    @ivar transport: transport (over http) object
    '''

    __metaclass__ = ApiServiceMeta

    ApiCalls = [
        bfapicalls.ApiCallGlobal('login'),
        bfapicalls.ApiCallGlobal('keepAlive'),
        bfapicalls.ApiCallGlobal('logout'),
        bfapicalls.ApiCallGlobal('getActiveEventTypes'),
        bfapicalls.ApiCallGlobal('getEvents'),
        bfapicalls.ApiCallExchange('getAllMarkets'),
        bfapicalls.ApiCallExchange('getAccountFunds'),
        bfapicalls.ApiCallGlobal('transferFunds'),
        bfapicalls.ApiCallExchange('getCurrentBets'),
        bfapicalls.ApiCallExchange('getMarket'),
        bfapicalls.ApiCallExchange('getMarketPricesCompressed'),
        bfapicalls.ApiCallExchange('getCompleteMarketPricesCompressed'),
        bfapicalls.ApiCallExchange('getMarketTradedVolumeCompressed'),
        bfapicalls.ApiCallExchange('getMarketProfitAndLoss'),
        bfapicalls.ApiCallExchange('getMUBets'),
        bfapicalls.ApiCallExchange('placeBets'),
        bfapicalls.ApiCallExchange('cancelBets'),
        bfapicalls.ApiCallExchange('updateBets'),
        bfapicalls.ApiCallVendor('createVendorAccessRequest'),
        bfapicalls.ApiCallVendor('cancelVendorAccessRequest'),
        bfapicalls.ApiCallVendor('updateVendorSubscription'),
        bfapicalls.ApiCallVendor('getVendorUsers'),
        bfapicalls.ApiCallVendor('getVendorAccessRequests'),
        bfapicalls.ApiCallVendor('getSubscriptionInfo'),
        bfapicalls.ApiCallVendor('getVendorInfo'),
        ]


    def __init__(self, endPoint, transport):
        '''
        Constructor of ApiService
        
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
