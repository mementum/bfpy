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
Definition of services and metaclass to install them in an API provider
'''

import types


class ServiceDescriptor(object):
    '''
    Base abstract descriptor class for the implementation of the methods
    provided by the Betfair API

    @ivar _instanceCache: cache holding a copy of the method served to instances
    @type _instanceCache: dict of methods
    @ivar methodName: name the descriptor will be invoked by
    @type methodName: str
    @ivar kwargs: extra variables passed to the method
    @type kwargs: dict
    '''
    
    def __init__(self, methodName, **kwargs):
        '''
        Initialize the cache of instances and make a copy of the extra arguments

        @param methodName: name the descriptor will be invoked by
        @type methodName: str
        @param kwargs: extra variables passed to the method
        @type kwargs: dict
        '''
        self.methodName = methodName
        
        # Cache for descriptor calls
        self._instanceCache = dict()

        # Extra arguments for calls
        self.kwargs = kwargs


    def __get__(self, instance, owner=None):
        '''
        Non-data descriptor implementation.

        It returns a method type pointing to itself. This forces the invocation
        of __call__
        '''
        return self._instanceCache.setdefault(instance,
                                              types.MethodType(self, instance, owner))


    def __call__(self, *args, **kwargs):
        '''
        Pure virtual function to be implemented by Service implementation classes

        @raise NotImplemented: pure virtual function
        '''
        raise NotImplemented


class ServiceDef(ServiceDescriptor):
    '''
    Definition and implementation of a service. The definition includes the
    name of the method, the service name, endPoint to go to, name of the request
    argument (and if an API header has to be added to it) and error codes that
    should be skipped, together with a list of post processing callables.

    The service name can be derived from the methodName and so can the
    requestName from the methodName. This is due to the regularity of many
    services in the Betfair API.

    Some of the Betfair API errorCodes are indications and that is why they
    can be skipped. This also serves to delay checking for wrongly served
    errorCodes (INVALID_MARKET instead of MARKET_CLOSED in
    getMarketProfitAndLoss)

    The extra (kwargs) held by the parent class, allows the provision of
    default values for arguments to a method, so the user will not need
    to provide them. This feature also covers the problem that some
    parameters are signaled as optional in the Betfair documentation when
    they are not. If the user does not provide them the default value will
    be applied.

    @ivar endPoint: location endPoint of the service (0 Global, 1 Exchange)
    @type endPoint: int
    @ivar methodName: name the method will be invoked by
    @type methodName: str
    @ivar serviceName: name of the service to invoke
    @type serviceName: str
    @ivar requestName: name of the request to pass to the service
    @type requestName: str
    @ivar apiHeader: whether to add an API header to the request
    @type apiHeader: bool
    @ivar skipErrorCodes: errorCodes that will not signal an error
    @type skipErrorCodes: list
    @ivar preProc: callables that will pre process a service request
    @type preProc: list
    @ivar postProc: callables that will post process a service response
    @type postProc: list
    '''

    def __init__(self, endPoint,
                 methodName, serviceName=None, requestName=None,
                 apiHeader=True, skipErrorCodes=None,
                 preProc=None, postProc=None, weight=0,
                 **kwargs):
        '''
        Initializes the service and variables
        
        @param endPoint: location endPoint of the service (0 Global, 1 Exchange)
        @type endPoint: int
        @param methodName: name the method will be invoked by
        @type methodName: str
        @param serviceName: name of the service to invoke
        @type serviceName: str
        @param requestName: name of the request to pass to the service
        @type requestName: str
        @param apiHeader: whether to add an API header to the request
        @type apiHeader: bool
        @param skipErrorCodes: errorCodes that will not signal an error
        @type skipErrorCodes: list
        @param preProc: callables that will pre process a service request
        @type preProc: list
        @param postProc: callables that will post process a service response
        @type postProc: list
        @param weight: weight count into data charges. Negative values are assumed
                       to be multiplied by 5 (and passed as positive)
        @type weight: int
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        ServiceDescriptor.__init__(self, methodName, **kwargs)

        self.endPoint = endPoint

        if serviceName is None:
            serviceName = self.methodName[0].lower() + self.methodName[1:]
        self.serviceName = serviceName
            
        if requestName is None:
            requestName = self.serviceName[0].upper() + self.serviceName[1:] + 'Req'
        self.requestName = requestName

        self.apiHeader = apiHeader

        self.skipErrorCodes = ['INVALID_LOCALE_DEFAULTING_TO_ENGLISH']
        if skipErrorCodes:
            self.skipErrorCodes.extend(skipErrorCodes)

        if preProc is None:
            preProc = list()
        self.preProc = preProc

        if postProc is None:
            postProc = list()
        self.postProc = postProc

        self.weight = weight


    def __call__(self, instance, *args, **kwargs):
        '''
        Invocation of a service in a generic manner.

        It is in charge of deciding the final endPoint (global or exchange,
        and if exchange, which one from the parameters), get a reference
        to the service method from the instance, the request to be passed
        and filling in the request values (with the default and provided
        kwargs)

        Once the response is received, it is passed through the defined
        post processing callables and then returned

        @param instance: object whose method is being invoked
        @type instance: object
        @param args: exchange services will receive the exchangeId there
        @type args: tuple
        @param kwargs: names and values of args for the service request
        @type kwargs: dict
        '''
        # Calls to Exchanges need the specific exchange endPoint
        # passed to the functions as 1st unnamed arg
        endPoint = self.endPoint if not self.endPoint else args[0]

        # Get the service from the appropriate endpoint
        service = instance.getService(endPoint, self.serviceName)

        # Get the service request argument from the appropriate endpoint
        request = instance.getRequest(endPoint, self.requestName, self.apiHeader)

        # Make a copy dictionary of args with default values
        requestArgs = self.kwargs.copy()
        # Update the dictionary with new args/updated args
        requestArgs.update(kwargs)

        # Pre-process
        if instance.preProcess:
            for preProc in self.preProc:
                preProc(request, requestArgs,
                        instance=instance, service=service, exchangeId=endPoint,
                        methodArgs=kwargs)

        # Fill in the defined argument values in the service request
        for name, value in requestArgs.iteritems():
            setattr(request, name, value)

        # Calculate the data charges weight
        if self.weight < 0:
            # A marketId parameter is supposed to be in place
            try:
                if not request.marketId:
                    weight = 5 * -self.weight
                else:
                    weight = -self.weight
            except:
                weight = 5 * -self.weight
        else:
            weight = self.weight
            
        # Add the weight to the instance - blocking the call if needed
        instance.addDataWeight(endPoint, weight)

        # Execute the call and fetch the response
        response = instance.invoke(self.methodName, service, request, self.skipErrorCodes)

        # Post-Process the response if needed
        if instance.postProcess:
            for postProc in self.postProc:
                postProc(response, instance=instance, service=service,exchangeId=endPoint,
                         request=request)

        return response


class GlobalServiceDef(ServiceDef):
    '''
    Service Definition for global services. It is a ServiceDefinition
    subclass with the endPoint set to the global value
    '''
        
    def __init__(self,
                 methodName, serviceName=None, requestName=None,
                 apiHeader=True, skipErrorCodes=None,
                 preProc=None, postProc=None, weight=0,
                 **kwargs):
        '''
        Initializes the service and variables, setting the the
        endPoint to the global endPoint (0)
        
        @param methodName: name the method will be invoked by
        @type methodName: str
        @param serviceName: name of the service to invoke
        @type serviceName: str
        @param requestName: name of the request to pass to the service
        @type requestName: str
        @param apiHeader: whether to add an API header to the request
        @type apiHeader: bool
        @param skipErrorCodes: errorCodes that will not signal an error
        @type skipErrorCodes: list
        @param preProc: callables that will pre process a service request
        @type preProc: list
        @param postProc: callables that will post process a service response
        @type postProc: list
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        ServiceDef.__init__(
            self, 0,
            methodName, serviceName=serviceName, requestName=requestName,
            apiHeader=apiHeader, skipErrorCodes=skipErrorCodes,
            preProc=preProc, postProc=postProc, weight=weight,
            **kwargs)


class ExchangeServiceDef(ServiceDef):
    '''
    Service Definition for exchane services. It is a ServiceDefinition
    subclass with the endPoint set to the exchange value
    '''

    def __init__(self,
                 methodName, serviceName=None, requestName=None,
                 apiHeader=True, skipErrorCodes=None,
                 preProc=None, postProc=None, weight=0,
                 **kwargs):
        '''
        Initializes the service and variables, setting the the
        endPoint to the global endPoint (0)
        
        @param methodName: name the method will be invoked by
        @type methodName: str
        @param serviceName: name of the service to invoke
        @type serviceName: str
        @param requestName: name of the request to pass to the service
        @type requestName: str
        @param apiHeader: whether to add an API header to the request
        @type apiHeader: bool
        @param skipErrorCodes: errorCodes that will not signal an error
        @type skipErrorCodes: list
        @param preProc: callables that will pre process a service request
        @type preProc: list
        @param postProc: callables that will post process a service response
        @type postProc: list
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        ServiceDef.__init__(
            self, 1,
            methodName, serviceName=serviceName, requestName=requestName,
            apiHeader=apiHeader, skipErrorCodes=skipErrorCodes,
            preProc=preProc, postProc=postProc, weight=weight,
            **kwargs)


class ServiceObject(ServiceDescriptor):
    '''
    Service descriptor implementation to retrieve named objects defined
    for the services. This allows using those objects to return them with
    decompressed data from the Betfair API "getXXXCompressed" family

    The method name will be automatically set to "create" + the name
    of the object

    @ivar methodName: name the method will be invoked by
    @type methodName: str
    @ivar endPoint: location endPoint of the service (0 Global, 1 Exchange)
    @type endPoint: int
    @ivar objectName: name of the object to be retrieved
    @type objectName: str
    '''
    
    def __init__(self, endPoint, objectName, **kwargs):
        '''
        Initialize the instance and data members for later usage
        
        @param endPoint: location endPoint of the service (0 Global, 1 Exchange)
        @type endPoint: int
        @param objectName: name of the object to be retrieved
        @type objectName: str
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        ServiceDescriptor.__init__(self, 'create' + objectName, **kwargs)
        self.endPoint = endPoint
        self.objectName = objectName


    def __call__(self, instance, **kwargs):
        '''
        Method implementation. It retrieves the object from the specified
        endPoint and fills in the values (default and provided) in the object
        
        @param instance: object whose method is being invoked
        @type instance: object
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        # Retrieve the object from the endPoint
        serviceObject = instance.getObject(self.endPoint, self.objectName)

        # get the default values and update them
        objArgs = self.kwargs.copy()
        objArgs.update(kwargs)

        # Fill in the object with the values
        for name, value in objArgs.iteritems():
            setattr(serviceObject, name, value)

        return serviceObject


class GlobalObject(ServiceObject):
    '''
    Subclass of ServiceObject to retrieve objects from the global endPoint (0)
    '''

    def __init__(self, objectName, **kwargs):
        '''
        Initialize a ServiceObject with the global endPoint (0)
        
        @param objectName: name of the object to be retrieved
        @type objectName: str
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        ServiceObject.__init__(self, 0, objectName, **kwargs)


class ExchangeObject(ServiceObject):
    '''
    Subclass of ServiceObject to retrieve objects from the exchange endPoint (1)
    '''

    def __init__(self, objectName, **kwargs):
        '''
        Initialize a ServiceObject with the global endPoint (1)
        
        @param objectName: name of the object to be retrieved
        @type objectName: str
        @param kwargs: extra arguments (with values) to pass to the method
        @type kwargs: dict
        '''
        ServiceObject.__init__(self, 1, objectName, **kwargs)


class BfService(type):
    '''
    Metaclass for L{BfApi} to initialize the non-data descriptor based
    methods on instantiation
    '''

    def __new__(mcs, name, bases, dict):
        '''
        On L{BfApi} instantiation the service definitions present in the
        class variable I{serviceDefs} are added to the dictionary of the
        instance to generate non-data descriptor based methods
        that allow the invocation of the Betfair API Services
        '''
        for serviceDef in dict['serviceDefs']:
            dict[serviceDef.methodName] = serviceDef

        return type.__new__(mcs, name, bases, dict)
