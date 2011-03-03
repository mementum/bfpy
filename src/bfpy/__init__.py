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
BfPy main module. It imports the main objects to let them be re-imported
'''

version = 0.81

import logging
# logging.basicConfig(level=logging.INFO)
from util import NullHandler

handler = NullHandler()

# suds logging
log = logging.getLogger('suds')
log.setLevel(logging.ERROR)
log.addHandler(handler)

from bfapi import *
from bfclient import *
from bferror import *

def GetPriceTicksUp(price, ticks):
    priceTicks = {
        2.0: 0.01, 3.0: 0.02, 4.0: 0.05, 6.0: 0.1,
        10.0: 0.2, 20.0: 0.5, 30.0: 1.0, 50.0: 2.0,
        100.0: 5.0, 1000.0: 10.0
        }

    # Price is assumed to be well formed
    limits = priceTicks.keys()
    limits.sort()
    for limit in limits:
        inc = priceTicks[limit]
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
