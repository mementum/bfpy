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
Classes for definition and management of API types
'''

import datetime
import types

class ApiParam(object):
    '''
    Non-data descriptor class to be installed in a L{ApiDataType}

    @type name: string
    @ivar name: public name of the "param"
    @type nullable: bool
    @ivar nullable: if the parameter can be nullified upon sending the request
    @type defvalue: any
    @ivar defvalue: if not None the default value will be applied if no other
                    has been later specified
    @type listtype: string
    @ivar listtype: if the para specifies a list type, this defines the 'soap' type
    @type patternList: string
    @ivar patternList: pre-computed listtype pattern for element list substitution
    @type patternFill: string
    @ivar patternFill: pre-computed patter for substitution
    @type patternNull: string
    @ivar patternNull: precomputed pattern for substitution if the value is nullified
    @type instanceval: dict
    @ivar instanceval: holds the assigned value to the param on a per instance basis
    @type instanceCache: dict
    @ivar instanceCache: holds the generated method to be called by holding instances
    '''
    def __init__(self, name, nullable=False, xsd=True, value=None, listtype=None):
        '''
        Initializes the descriptor precomputing the needed patterns

        @type name: string
        @param name: public name of the "param"
        @type nullable: bool
        @param nullable: if the parameter can be nullified upon sending the request
        @type xsd: bool
        @param xsd: if the type is xsd standard or not (to be used with nullable)
        @type value: any
        @param value: to be stored as defvalue
        @type listtype: string
        @param listtype: if the para specifies a list type, this defines the 'soap' type
        '''
        self.instanceCache = dict()
        self.instanceval = dict()

        self.name = name
        self.nullable = nullable
        self.defvalue = value
        self.listtype = listtype

        self.patternFill = '<%s>%%s</%s>' % (name, name)

        if self.nullable:
            self.patternNull = '<%s' % name
            if xsd:
                self.patternNull += ' xsi:nil="true"'
            self.patternNull += '/>'

        self.patternList = '<ns2:%s>%%s</ns2:%s>' % (self.listtype, self.listtype)


    def __set__(self, instance, value):
        '''
        Stores the value passed to later generate the exception

        @type instance: instance
        @param instance: instance that is calling the descriptor
        @type value: any
        @param value: value to be stored for substitution in pattern
        '''
        self.instanceval[instance] = value


    def __get__(self, instance, owner=None):
        '''
        Non-data descriptor implementation.

        If invoked at class level it returns and unbound method pointing that forces the invocation
        of __call__. The invocation has to be done with an instance

        If invoked from an instance it returns the value that is currently stored for such instance

        @type instance: instance of class
        @param instance: instance that calls the descriptor
        @type owner: class
        @param owner: the class that holds the descriptor
        '''
        if instance is None:
            return self.instanceCache.setdefault(owner, types.MethodType(self, None, owner))
        return self.instanceval.get(instance, self.defvalue)


    def __call__(self, instance):
        '''
        Returns the pattern for this param

        @type instance: instance
        @param instance: instance that is calling the descriptor

        @return: textual representation of the defined ApiParam type
        @rtype: string

        '''
        value = self.instanceval.get(instance, self.defvalue)

        if value is None and self.nullable:
            # NOTE: A exception could be raised if not "nullable"
            return self.patternNull

        if isinstance(value, (int, long, float, basestring)):
            pattern = str(value)
        elif isinstance(value, bool):
            pattern = str(value).lower()
        elif isinstance(value, (list, tuple)):
            pattern = ''
            for val in value:
                pattern += self.patternList % str(val)
        elif isinstance(value, datetime.datetime):
            pattern = value.isoformat()
        else:
            pattern = str(value)

        return self.patternFill % pattern


ApiDataTypes = list()

class ApiDataTypeMeta(type):
    '''
    Metaclass for L{ApiDataType} that install L{ApiParam} descriptors
    '''
    def __new__(cls, name, bases, clsdict):
        '''
        Modifies L{ApiDataType} class creation

        @type cls: class
        @param cls: the class to be modifies on creation
        @type name: string
        @param name: name of the class
        @type bases: list
        @param bases: list of base classes for cls
        @type clsdict: dict
        @param clsdict: the dictionary of cls
        '''
        clsdict['params'] = list()
        if 'apiParams' in clsdict:
            for apiParam in clsdict['apiParams']:
                clsdict[apiParam.name] = apiParam
                clsdict['params'].append(apiParam.name)

        newcls = type.__new__(cls, name, bases, clsdict)
        ApiDataTypes.append(newcls)

        return newcls


class ApiDataType(object):
    '''
    Holds L{ApiParam} descriptors to later generate an entire pattern
    for an ApiDataType

    @type pattern: string
    @cvar pattern: pre-computed pattern for the type in the soap call
    @type header: ApiDataType
    @cvar header: a header that ApiDataType instances may carry (most do)
    '''
    __metaclass__ = ApiDataTypeMeta

    def __init__(self, name='ns1:request'):
        '''
        Initializes the pattern using the given name

        @type name: string
        @param name: name of the type in the soap call
                     if name is None, the pattern will be empty
                     (except for the substitution)
        '''
        self.header = None
        if name is not None:
            self.pattern = '<%s>\n%%s</%s>' % (name, name)
        else:
            self.pattern = '\n%s'


    def __call__(self):
        '''
        Returns the final computed pattern for the type
        '''
        subpattern = ''

        if self.header is not None:
            subpattern += self.header()
            subpattern += '\n'

        for param in self.params:
            subpattern += getattr(self.__class__, param)(self)
            subpattern += '\n'

        return self.pattern % subpattern


    def __str__(self):
        '''
        Returns the final computed pattern for the type
        '''
        return self()


    def __unicode__(self):
        '''
        Returns the final computed pattern for the type in unicode
        '''
        return unicode(self()).encode('utf-8')


'''ApiDataType definitions'''

class APIRequestHeader(ApiDataType):
    apiParams = [
        ApiParam('clientStamp'), ApiParam('sessionToken'),
        ]

    def __init__(self):
        ApiDataType.__init__(self, name='header')


class LoginReq(ApiDataType):
    apiParams = [
        ApiParam('ipAddress'), ApiParam('locationId'),
        ApiParam('password'), ApiParam('productId'),
        ApiParam('username'), ApiParam('vendorSoftwareId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class KeepAliveReq(ApiDataType):
    def __init__(self):
        ApiDataType.__init__(self)


class LogoutReq(ApiDataType):
    def __init__(self):
        ApiDataType.__init__(self)


class GetEventTypesReq(ApiDataType):
    apiParams = [
        ApiParam('locale', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetEventsReq(ApiDataType):
    apiParams = [
        ApiParam('eventParentId'),
        ApiParam('locale', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetAllMarketsReq(ApiDataType):
    apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('eventTypeIds', nullable=True, xsd=False, listtype='int'),
        ApiParam('countries', nullable=True, xsd=False, listtype='Country'),
        ApiParam('fromDate', nullable=True),
        ApiParam('toDate', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetAccountFundsReq(ApiDataType):
    def __init__(self):
        ApiDataType.__init__(self)


class TransferFundsReq(ApiDataType):
    apiParams = [
        ApiParam('sourceWalletId'),
        ApiParam('targetWalletId'),
        ApiParam('amount'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetCurrentBetsReq(ApiDataType):
    apiParams = [
        ApiParam('betStatus', xsd=False),
        ApiParam('detailed'),
        ApiParam('locale', nullable=True),
        ApiParam('timezone', nullable=True),
        ApiParam('marketId'),
        ApiParam('orderBy', xsd=False),
        ApiParam('recordCount'),
        ApiParam('startRecord'),
        ApiParam('noTotalRecordCount'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketReq(ApiDataType):
    apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('marketId'),
        ApiParam('includeCouponLinks', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketPricesCompressedReq(ApiDataType):
    apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetCompleteMarketPricesCompressedReq(ApiDataType):
    apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketTradedVolumeCompressedReq(ApiDataType):
    apiParams = [
        ApiParam('currencyCode', nullable=True),
        ApiParam('marketId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMarketProfitAndLossReq(ApiDataType):
    apiParams = [
        ApiParam('locale', nullable=True),
        ApiParam('includeSettledBets', nullable=True),
        ApiParam('includeBspBets'),
        ApiParam('marketID'),
        ApiParam('netOfComission', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class GetMUBetsReq(ApiDataType):
    apiParams = [
        ApiParam('betStatus', xsd=False),
        ApiParam('marketId', nullable=True),
        ApiParam('betIds', nullable=True, xsd=False, listtype='betId'),
        ApiParam('orderBy', xsd=False),
        ApiParam('sortOrder', xsd=False),
        ApiParam('recordCount'),
        ApiParam('startRecord'),
        ApiParam('matchedSince', nullable=True),
        ApiParam('excludeLastSecond', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class PlaceBetsReq(ApiDataType):
    apiParams = [
        ApiParam('bets', listtype='PlaceBets'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class PlaceBets(ApiDataType):
    apiParams = [
        ApiParam('asianLineId'),
        ApiParam('betType', xsd=False),
        ApiParam('betCategoryType', xsd=False),
        ApiParam('betPersistenceType', xsd=False),
        ApiParam('marketId'),
        ApiParam('price'),
        ApiParam('selectionId'),
        ApiParam('size'),
        ApiParam('bspLiability', nullable=True),
        ]
    def __init__(self):
        ApiDataType.__init__(self, name=None)


class CancelBetsReq(ApiDataType):
    apiParams = [
        ApiParam('bets', listtype='CancelBets'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class CancelBets(ApiDataType):
    apiParams = [
        ApiParam('betId'),
        ]
    def __init__(self):
        ApiDataType.__init__(self, name=None)


class UpdateBetsReq(ApiDataType):
    apiParams = [
        ApiParam('bets', listtype='UpdateBets'),
        ]
    def __init__(self):
        ApiDataType.__init__(self)


class UpdateBets(ApiDataType):
    apiParams = [
        ApiParam('betId'),
        ApiParam('newPrice'),
        ApiParam('newSize'),
        ApiParam('oldPrice'),
        ApiParam('oldSize'),
        ApiParam('newBetPersistenceType', xsd=False),
        ApiParam('oldBetPersistenceType', xsd=False),
        ]
    def __init__(self):
        ApiDataType.__init__(self, name=None)


##############################################
# DirectAPI implementation of Vendor API types
##############################################
class CreateVendorAccessRequestReq(ApiDataType):
    apiParams = [
        ApiParam('vendorCustomField'),
        ApiParam('vendorSoftwareId'),
        ApiParam('expiryDate', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class CancelVendorAccessRequestReq(ApiDataType):
    apiParams = [
        ApiParam('accessRequestToken'),
        ApiParam('vendorSoftwareId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class VendorSubscriptionReq(ApiDataType):
    apiParams = [
        ApiParam('username'),
        ApiParam('vendorCustomField'),
        ApiParam('vendorClientId'),
        ApiParam('vendorSoftwareId'),
        ApiParam('expiryDate', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetVendorUsersReq(ApiDataType):
    apiParams = [
        ApiParam('vendorSoftwareId'),
        ApiParam('username', nullable=True),
        ApiParam('usernameSearchModifier', xsd=False),
        ApiParam('vendorCustomField', nullable=True),
        ApiParam('customFieldSearchModifier', xsd=False),
        ApiParam('expiryDateFrom', nullable=True),
        ApiParam('expiryDateTo', nullable=True),
        ApiParam('status', xsd=False),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetVendorAccessRequestsReq(ApiDataType):
    apiParams = [
        ApiParam('vendorSoftwareId'),
        ApiParam('status', xsd=False),
        ApiParam('requestDateFrom', nullable=True),
        ApiParam('requestDateTo', nullable=True),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetSubscriptionInfoReq(ApiDataType):
    apiParams = [
        ApiParam('username'),
        ApiParam('vendorClientId'),
        ApiParam('vendorSoftwareId'),
        ]

    def __init__(self):
        ApiDataType.__init__(self)


class GetVendorInfoReq(ApiDataType):
    apiParams = [
        ]

    def __init__(self):
        ApiDataType.__init__(self)
