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
#
# Contains classes for a suds http(s) transport implementation
#

from copy import deepcopy
from cStringIO import StringIO
import logging
from urlparse import urlparse

import suds


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

log = logging.getLogger(__name__)
if False:
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -\n%(message)s")
    handler = logging.FileHandler('bftransport.log', mode='w')
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
else:
    handler = NullHandler()

log.addHandler(handler)

try:
    from httxlib import HttxManager, HttxRequest, HttxException, SocketException
    TransportException = SocketException

    class BfTransport(suds.transport.Transport):
        '''
        HTTP transport using httxlib.  Provides http/https transport
        with cookies, authentication (basic and digest), redirection,
        certificate support and certificate validation
        and proxy support
        '''


        def __init__(self, httxmanager=None, **kwargs):
            """
            Initialize the transport.

            If an httxmanager is passed it will be used as the underlying transport
            else a new one will be created

            @param httxmanager: A HttxManager object to do actual transport
            @type httxmanager: HttxManager
            @param kwargs: keyword arguments
            @type kwargs: dict
            """
            suds.transport.Transport.__init__(self)
            self.httxmanager = httxmanager if httxmanager else HttxManager()


        def setproxy(self, proxydict):
            self.httxmanager.setproxy(proxydict)


        def setuseragent(self, useragent):
            self.httxmanager.setuseragent(useragent)


        def setdecompmethods(self, decompmethods):
            self.httxmanager.setdecompmethods(decompmethods)

        
        def open(self, request):
            """
            Open a file or url
            If request.url can't be identified as a url, it will
            return the content in a file-like object

            @param request: A suds Request
            @type Request: suds.transport.Request
            @return: A file-like object
            @rtype: file
            """
            log.debug('opening: (%s)', request.url)

            fp = None
            location = request.url.lstrip()
            if location.startswith('<?'):
                log.debug('returning url (%s) as StringIO file')
                fp = StringIO(location)
            else:
                parsed = urlparse(request.url)
                if parsed.scheme == 'file':
                    log.debug('opening file (%s) with open', parsed.path)
                    try:
                        fp = open(parsed.path)
                    except Exception, e:
                        raise suds.transport.TransportError(str(e), 503, StringIO(''))
                else:
                    log.debug('opening scheme (%s) over the network', parsed.scheme)
                    fp = self.invoke(request, retfile=True)

            return fp


        def send(self, request):
            """
            Send a soap request

            @param request: A suds Request
            @type Request: suds.transport.Request
            @return: suds Reply
            @rtype: suds.transport.Reply
            """
            log.debug('sending: %s', request)
            return self.invoke(request)


        def invoke(self, request, retfile=False):
            """
            Open a connection.
        
            @param request: A suds Request
            @type Request: suds.transport.Request
            @param retfile: indicates if a file-like object is to be returned
            @type: bool 
            @return: A file-like object or a suds Reply
            @rtype: file or suds.transport.Reply
            """
            httxrequest = HttxRequest(request.url, request.message, request.headers)

            # The final "sent" headers are unknown until urlopen is called
            # because the httxmanager will add compression, cookies, authentication
            # and may do that on a dynamic basis
            try:
                httxresponse = self.httxmanager.urlopen(httxrequest)

                # This check is to replicate original suds http transport behaviour
                if httxresponse.status in (202, 204):
                    return None if not retFile else StringIO('')

                if httxresponse.status < 200 and httxresponse.status >= 300:
                    raise suds.transport.TransportError(httxresponse.reason, httxresponse.status, httxresponse.bodyfile)

                if not httxresponse.body.startswith('<?xml'):
                    raise suds.transport.TransportError('Wrong answer received from server. Please check connection',
                                         503, httxresponse.bodyfile)
                    # raise suds.transport.TransportError(httxresponse.reason, httxresponse.status, httxresponse.bodyfile)

            except suds.transport.TransportError:
                raise
            except HttxException, e:
                # This error is to mimic the original exception code
                httxresponse = e.response
                raise suds.transport.TransportError(httxresponse.reason, httxresponse.status, httxresponse.bodyfile)
            except Exception, e:
                # This will be a non-HTTP error (python syntax, socket closed, socket timeout, ssl, ...)
                # Original transport from suds does not handle "non-http" errors
                # But they could be handled in something like
                # to generate a WebFault
                # 503 is chosen following the HTTP return codes definition
                # raise suds.transport.TransportError(str(e), 503, StringIO(''))
                raise

            reply = suds.transport.Reply(200, httxresponse.headers, httxresponse.body)
            log.debug('received reply:\n%s', reply)

            # if needed return what "open" is expecting ... a file-like object
            if retfile:
                reply = httxresponse.bodyfile
                # reply = StringIO(reply.message)

            return reply

            
        def __deepcopy__(self, memo):
            """
            Deepcopy support

            It does a copy of itself with the existing HttxManager object
            because the httxmanager is already multithreaded safe
            and can handle multiple connections
        
            @param memo: Standard deepcopy memo parameter to avoid loops
            @type memo: dict
            @return: a cloned object
            @rtype: HttxTransport
            """
            clone = self.__class__(self.httxmanager)
            return clone


        def clone(self):
            """
            Just an alias for __deepcopy__
            """
            return deepcopy(self)


except ImportError:
    TransportException = None

    import urllib2 as u2

    # Small replica from original suds transport that allows
    # setting a proxy via a method and opening wsdl files
    # stored in a string
    class BfTransport(suds.transport.Transport):
        def __init__(self, **kwargs):
            suds.transport.Transport.__init__(self, **kwargs)


        def setproxy(self, proxy):
            self.options.proxy = proxy


        def open(self, request):
            """
            Open a file or url
            If request.url can't be identified as a url, it will
            return the content in a file-like object

            @param request: A suds Request
            @type Request: suds.transport.Request
            @return: A file-like object
            @rtype: file
            """
            log.debug('opening: (%s)', request.url)

            fp = None
            location = request.url.lstrip()
            if location.startswith('<?'):
                log.debug('returning url (%s) as StringIO file')
                fp = StringIO(location)
            else:
                parsed = urlparse(request.url)
                if parsed.scheme == 'file':
                    log.debug('opening file (%s) with open', parsed.path)
                    try:
                        fp = open(parsed.path)
                    except Exception, e:
                        raise suds.transport.TransportError(str(e), 503, StringIO(''))
                else:
                    log.debug('opening scheme (%s) over the network', parsed.scheme)
                    try:
                        url = request.url
                        log.debug('opening (%s)', url)
                        u2request = u2.Request(url)
                        self.proxy = self.options.proxy
                        return self.u2open(u2request)
                    except u2.HTTPError, e:
                        raise suds.transport.TransportError(str(e), e.code, e.fp)
            return fp
