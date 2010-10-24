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
BfApi method extensions to be inserted in BfClient
'''

from copy import copy
from operator import attrgetter

from bfapi2 import BfApi, eventRootId
from bfservice import ServiceDescriptor


class GetEvents(ServiceDescriptor):
    def __init__(self, **kwargs):
        ServiceDescriptor.__init__(self, 'getEvents', **kwargs)

    def __call__(self, instance, eventParentId=-1):
        '''
        Returns ActiveEvents and Events in a single call

        @param eventParentId: id of the parent event for which to return
                              eventItems/marketItems. Pass -1 for the top level items
        @type eventParentId: int

        @returns: Betfair API answer
        @rtype: suds object
        '''
        if eventParentId == eventRootId:
            print "cucu"
            response = instance.getActiveEventTypes()
            print response
            # Alias the .id and .name attributes to those of an event
            for event in response.eventTypeItems:
                event.eventId = event.id
                del event.id
                event.eventName = event.name
                del event.name

                # Create the eventItems and marketItems alias
                response.eventItems = response.eventTypeItems
                del response.eventTypItems
                response.marketItems = list()

            return response

        return BfApi.getEvents(instance, eventParentId=eventParentId)


class GetCurrentBets(ServiceDescriptor):
    def __init__(self, **kwargs):
        ServiceDescriptor.__init__(self, 'getCurrentBets', **kwargs)


    def __call__(self, instance, exchangeId, **kwargs):
        betStatus = kwargs.get('betStatus')

        if betStatus != 'MU':
            return BfApi.getCurrentBets(instance, exchangeId, **kwargs)

        currentBetsArgs = kwargs.copy()
        del currentBetsArgs['betSatus']
        mResponse = BfApi.getCurrentBets(instance, exchangeId, betStatus='M', **currentBesArgs)
        uResponse = BfApi.getCurrentBets(instance, exchangeId, betStatus='U', **currentBetsArgs)

        mResponse.totalRecordCount += uResponse.totalRecordCount
        mResponse.bets.extend(uResponse.bets)

        orderBy = kwargs.get('orderBy', 'NONE')

        if orderBy == 'PLACED_DATE':
            mResponse.bets.sort(key=attrgetter('placedDate', 'betStatus'))
        else:
            # According to the docs the only other combination for M and U is 'NONE'
            # so do a sensible ordering on betId and betStatus
            mResponse.bets.sort(key=attrgetter('betId', 'betStatus'))

        return mResponse
            

class PlaceBets(ServiceDescriptor):
    def __init__(self, **kwargs):
        ServiceDescriptor.__init__(self, 'placeBets', **kwargs)
    
    def __call__(self, instance, exchangeId, placeBets, nonIPRePlace=False):
        response = BfApi.placeBets(instance, placeBets)

        if response.betResults and nonIPRePlace:
            toRePlaceBets = list()
            for i, betResult in enumerate(response.betResults[:]):
                placeBet = placeBets[i]
                if betResult.resultCode == 'INVALID_PERSISTENCE' and placeBet.betPersistenceType == 'IP':
                    # This can be a simple copy because placeBet is made of Simple types
                    # newPlaceBet = deepcopy(placeBet)
                    newPlaceBet = copy(placeBet)
                    newPlaceBet.betPersistenceType = 'NONE'
                    toRePlaceBets.append(newPlaceBet)
                    response.betResults.pop(i)

            if toRePlaceBets:
                rePlaceResponse = BfApi.placeBets(instance, exchangeId, toRePlaceBets)
                response.betResults.extend(rePlaceResponse.betResults)

        return response
