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
BfPy global variables and functions module.

@var libname: name of this library
@type libname: string
@var version: the version number of the library
@type version: float
@var libstring: the combined library name and version number
@type libstring: string

@type freeApiId: int
@var freeApiId: default Betfair product Id, the one for the free API
@type Global: int
@var Global: endPoint id (internal) for the Global Betfair endpoint service
@type Exchange: int
@var Exchange: endPoint id (internal) to point out that a call goes to an Exchange
@type ExchangeUK: int
@var ExchangeUK: endPoint id (Betfair) for the UK Exchange Betfair endpoint service
@type ExchangeAus: int
@var ExchangeAus: endPoint id (Betfair) for the Aus Exchange Betfair endpoint service
@type Exchanges: list
@var Exchanges: list of available Exchange endpoints
@type EndPoints: list
@var EndPoints: list of available Betfair EndPoints
@type EndPointUrls: list
@var EndPointUrls: list of available Betfair EndPoint Urls

@type wsdlDefs: dict
@var wsdlDefs: mapping of EndPoints to the WSDL contents

@type eventRootId: int
@var eventRootId: default parentEventId to identify ActiveEventTypes in the joint
                  call that unifies GetActiveEventTypes and GetEvents

@type preProcess: bool
@var preProcess: default library behaviour: process (easing use) the user requests
                 before sending them to Betfair
@type postProcess: bool
@var postProcess: default library behaviour: process (easing use) Betfair answers
                  before sending them to Betfair

@type forceDirect: bool
@var forceDirect: to force the library always use the DirectAPI method
                  If suds importing fails, it will be set to True


@type sudsWebFault: object
@var sudsWebFaults: an alias to suds.WebFault or None if no suds is used 

@type sudsClient: module
@var sudsClient: an alias so suds.client or None if no suds is used

'''
libname = 'BfPy'
version = 1.10
libstring = '%s %s' % (libname, str(version))

forceDirect = False
wsdlDefs = dict()

freeApiId = 82

Vendor = -1
Global = 0
Exchange = 1
ExchangeUK = 1
ExchangeAus = 2

Exchanges = [ExchangeUK, ExchangeAus]
EndPoints = [Vendor, Global, ExchangeUK, ExchangeAus]

EndPointUrls = {
    Vendor: 'https://api.betfair.com/admin-api/v2/VendorService',
    Global: 'https://api.betfair.com/global/v3/BFGlobalService',
    ExchangeUK: 'https://api.betfair.com/exchange/v5/BFExchangeService',
    ExchangeAus: 'https://api-au.betfair.com/exchange/v5/BFExchangeService',
    }

sudsWebFault = None
sudsClient = None

try:
    # Try importing suds
    import suds
except ImportError:
    # No suds, so only DirectAPI calls can be used
    forceDirect = True
else:
    # Suds is available. Import the wsdl contents, clients and fault
    import bfwsdl
    wsdlDefs = {
        Vendor: bfwsdl.BFVendorService,
        Global: bfwsdl.BFGlobalService,
        ExchangeUK: bfwsdl.BFExchangeService,
        ExchangeAus: bfwsdl.BFExchangeServiceAus,
        }

    import suds.client
    sudsClient = suds.client
    from suds import WebFault
    sudsWebFault = WebFault

    import logging
    # logging.basicConfig(level=logging.INFO)
    from util import NullHandler

    handler = NullHandler()

    # suds logging
    log = logging.getLogger('suds')
    log.setLevel(logging.ERROR)
    log.addHandler(handler)


eventRootId = -1

preProcess = True
postProcess = True


def GetPriceTicksUp(price, ticks):
    '''
    Returns the next price tick upwards for a given price

    @type  price: floast
    @param price: base price for next tick
    @type  ticks: int
    @param ticks: number of ticks to increase price

    @rtype: float
    @return: the passed prices increased x ticks
    '''
    priceTicksUp = {
        2.0: 0.01, 3.0: 0.02, 4.0: 0.05, 6.0: 0.1,
        10.0: 0.2, 20.0: 0.5, 30.0: 1.0, 50.0: 2.0,
        100.0: 5.0, 1000.0: 10.0
        }
    limits = priceTicksUp.keys()
    limits.sort()
    for limit in limits:
        inc = priceTicksUp[limit]
        if price < limit:
            while ticks:
                ticks -= 1
                price += inc
                if price == limit:
                    break;
            if not ticks:
                return price
    return price


def GetPriceTicksDown(price, ticks):
    '''
    Returns the next price tick downwards for a given price

    @type  price: floast
    @param price: base price for next tick
    @type  ticks: int
    @param ticks: number of ticks to decrease price

    @rtype: float
    @return: the passed prices decreased x ticks
    '''
    priceTicksDown = {
        100.0: 10.0, 50.0: 5.0, 30.0: 2.0,
        20.0: 1.0, 10.0: 0.5, 6.0: 0.2,
        4.0: 0.1, 3.0: 0.05, 2.0: 0.02,
        1.01: 0.01
        }

    # Price is assumed to be well formed
    limits = priceTicksDown.keys()
    limits.sort(reverse=True)
    for limit in limits:
        inc = priceTicksDown[limit]
        if price > limit:
            while ticks:
                ticks -= 1
                price -= inc
                if price == limit:
                    break
            if not ticks:
                return price
    return price


def GetPriceTicks(price, ticks, betType):
    '''
    Returns the next price tick upwards/downwards for a given price
    and bet type

    Back bets increase price upwards
    Lay bets increase price downwards

    @type  price: floast
    @param price: base price for next tick
    @type  ticks: int
    @param ticks: number of ticks to move the price
    @type  betType: B|L
    @param betType: bet type (determines the direction)

    @rtype: float
    @return: the passed prices decreased x ticks
    '''
    if not ticks:
        return price

    if betType == 'B':
        if ticks > 0:
            return GetPriceTicksUp(price, ticks)
        else:
            return GetPriceTicksDown(price, abs(ticks))
    else:
        if ticks < 0:
            return GetPriceTicksUp(price, ticks)
        else:
            return GetPriceTicksDown(price, abs(ticks))
