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
BfPy suds transport
'''

#
# Contains classes for a suds http(s) transport implementation
#

from copy import deepcopy
from cStringIO import StringIO
import logging
from urlparse import urlparse

import suds

from util import NullHandler

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
        HTTP transport using httxlib. Provides http/https transport
        with cookies, authentication (basic and digest), redirection,
        certificate support and certificate validation
        and proxy support
        '''

        def __init__(self, httxmanager=None, **kwargs):
            '''
            Initialize the transport.

            If an httxmanager is passed it will be used as the underlying transport
            else a new one will be created

            @param httxmanager: A HttxManager object to do actual transport
            @type httxmanager: HttxManager
            @param kwargs: keyword arguments
            @type kwargs: dict
            '''
            suds.transport.Transport.__init__(self)
            self.httxmanager = httxmanager if httxmanager else HttxManager()


        def setproxy(self, proxydict):
            '''
            Set the proxy options for the transport

            @param proxydict: proxy options
            @type proxydict: dict
            '''
            self.httxmanager.setproxy(proxydict)


        def setuseragent(self, useragent):
            '''
            Set the useragent option for the transport

            @param useragent: the useragent to fake
            @type useragent: str
            '''
            self.httxmanager.setuseragent(useragent)


        def setdecompmethods(self, decompmethods):
            '''
            Set the decompression methods option for the transport

            @param decompmethods: the useragent to fake
            @type decompmethods: list
            '''
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

    import base64
    import bz2
    from cookielib import CookieJar
    import copy
    import cStringIO
    import gzip
    from logging import getLogger
    import socket
    import urllib2 as u2
    from urlparse import urlparse
    import zlib

    from suds.properties import Unskin, Definition
    from suds.transport import Reply, Transport, TransportError

    log = getLogger(__name__)

    class BfTransport(Transport):
        """
        HTTP transport using urllib2.  Provided basic http transport
        that provides for cookies, proxies but no authentication.
        """
    
        def __init__(self, **kwargs):
            """
            Initialize. It adds some options to the standard options from suds and forces
            them to the default values (useragent, compression and compression methods)

            @param kwargs: Keyword arguments.
                - B{proxy} - An http proxy to be specified on requests.
                    The proxy is defined as {protocol:proxy,}
                        - type: I{dict}
                        - default: {}
                - B{timeout} - Set the url open timeout (seconds).
                        - type: I{float}
                        - default: 90
            """
            Transport.__init__(self)

            # Add options to the default set of options in case they do not exist
            if 'useragent' not in Unskin(self.options).definitions:
                Unskin(self.options).definitions['useragent'] = Definition('useragent', basestring, '')
                Unskin(self.options).definitions['compression'] = Definition('compression', basestring, 'yes')
                Unskin(self.options).definitions['compmethods'] = Definition('compmethods', list, ['gzip', 'deflate', 'bzip2'])
                # Force the new options to take the default value supplied
                Unskin(self.options).prime()

            Unskin(self.options).update(kwargs)
            self.cookiejar = CookieJar()
            self.proxy = dict()
            self.urlopener = None


        def setproxy(self, proxydict):
            '''
            Set the proxy options for the transport

            @param proxydict: proxy options
            @type proxydict: dict
            '''
            self.options.proxy = proxydict


        def setuseragent(self, useragent):
            '''
            Set the useragent option for the transport

            @param useragent: the useragent to fake
            @type useragent: str
            '''
            self.options.useragent = useragent


        def setdecompmethods(self, decompmethods):
            '''
            Set the decompression methods option for the transport

            @param decompmethods: the useragent to fake
            @type decompmethods: list
            '''
            self.options.compmethods = decompmethods


        # This implementation of "open" and "send"
        # could make it to the base class "Transport"

        def open(self, request):
            """
            Open a file or url
            If request.url can't be identified as a url, it will
            return the content in a file-like object
            @param request: A suds Request
            @type request: suds.transport.Request
            @return: A file-like object
            @rtype: file
            """
            log.debug('opening: (%s)', request.url)

            fp = None
            location = request.url.lstrip()
            if location.startswith('<?') == True:
                log.debug('returning url (%s) as StringIO file')
                fp = cStringIO.StringIO(location)
            else:
                parsed = urlparse(request.url)
                if parsed.scheme == 'file':
                    log.debug('opening file (%s) with open', parsed.path)
                    try:
                        fp = open(parsed.path)
                    except Exception, e:
                        raise TransportError(str(e), 500, None)
                else:
                    log.debug('opening scheme (%s) over the network', parsed.scheme)
                    fp = self.invoke(request, retfile=True)

            return fp

        def send(self, request):
            """
            Send a soap request

            @param request: A suds Request
            @type request: suds.transport.Request
            @return: suds Reply
            @rtype: suds.transport.Reply
            """
            log.debug('sending: %s', request)
            return self.invoke(request)


        # for the base class Transport
        # this would be the definition of "invoke"
        # called by either open or send
        #
        # def invoke(self, request, retfile = False):
        #     raise NotImplementedError
        def invoke(self, request, retfile=False):
            """
            Open a connection.
            @param request: A suds Request
            @type request: suds.transport.Request
            @param retfile: indicates if a file-like object is to be returned
            @type retfile: bool 
            @return: A file-like object or a suds Reply
            @rtype: file or suds.transport.Reply
            """
            tm = self.options.timeout

            request = self.prerequest(request)
            u2request = u2.Request(request.url, request.message, request.headers)

            self.addcookies(u2request)

            request.headers = u2request.headers
            log.debug('request final headers:\n%s', request.headers)

            urlopener = self.u2opener()
            try:
                if self.u2ver() < 2.6:
                    socket.settimeout(tm)
                    u2response = urlopener.open(u2request)
                else:
                    u2response = urlopener.open(u2request, timeout=tm)
            except u2.HTTPError, e:
                # This error is to mimic the original exception code
                if not retfile and e.code in (202,204):
                    result = None
                else:
                    raise TransportError(e.msg, e.code, e.fp)

            # Updatecookies in the cookie jar
            self.getcookies(u2response, u2request)

            reply = Reply(200, u2response.headers.dict, u2response.read())
            reply = self.postreply(reply)
            log.debug('received reply:\n%s', reply)

            # Return what "open" is expecting ... a file-like object
            if retfile == True:
                reply = cStringIO.StringIO(reply.message)

            return reply

            
        # I would personally remove this function
        # it is a one-liner that would substitute a one liner
        def addcookies(self, u2request):
            """
            Add cookies in the cookiejar to the request.
            @param u2request: A urllib2 request.
            @rtype: u2request: urllib2.Requet.
            """
            self.cookiejar.add_cookie_header(u2request)

        
        # I would personally remove this function
        # it is a one-liner that would substitute a one liner
        def getcookies(self, u2response, u2request):
            """
            Add cookies in the request to the cookiejar.
            @param u2request: A urllib2 request.
            @rtype: u2request: urllib2.Requet.
            """
            self.cookiejar.extract_cookies(u2response, u2request)
        
        # I think there was a bug in the original code since self.urlopener
        # was never assigned a value and the code kept on creating a new
        # opener


        # Of course if self.urlopener is None or self.options.proxy have changed
        # a new urlopener has to be created and stored
        def u2opener(self):
            """
            Create a urllib opener.
            @return: An opener.
            @rtype: I{OpenerDirector}
            """
            if self.urlopener == None or self.proxy != self.options.proxy:
                self.urlopener = u2.build_opener(*self.u2handlers())

            return self.urlopener
        
        # Make a copy (if needed) of the options.proxy to detect changes
        # during runtime
        def u2handlers(self):
            """
            Get a collection of urllib handlers.
            @return: A list of handlers to be installed in the opener.
            @rtype: [Handler,...]
            """
            handlers = []
            self.proxy = copy.copy(self.options.proxy)
            handlers.append(u2.ProxyHandler(self.proxy))
            return handlers

            
        def u2ver(self):
            """
            Get the major/minor version of the urllib2 lib.
            @return: The urllib2 version.
            @rtype: float
            """
            try:
                part = u2.__version__.split('.', 1)
                n = float('.'.join(part))
                return n
            except Exception, e:
                log.exception(e)
                return 0

        
        def __deepcopy__(self, memo={}):
            """
            Do a deepcopy of self
            @return: a cloned object
            @rtype: suds.transport.Transport
            """
            clone = self.__class__()
            p = Unskin(self.options)
            cp = Unskin(clone.options)
            cp.update(p)
            return clone


        def clone(self):
            """
            Easy alias for clone
            @return: a cloned object
            @rtype: suds.transport.Transport
            """
            return deepcopy(self)


        # This function pre-processes the request before sending it
        # In my opinion, the base class Transport should define it as an empty stub
        # or simply with "return request"

        # The HttpAuthenticated (below) is a perfect example, because instead of
        # redifining "open" and "send" to add the credentials it would only
        # redefine "preprequest" and then call the baseclass.prequest
        def prerequest(self, request):
            """
            Do preprocessing of the request before sending it

            @param request: the request to preprocess
            @type request: suds.transport.Request
            @return: the request (although the reference is being modified)
            @rtype: suds.transport.Request
            """
            if self.options.compression == 'yes':
                compmethods = ','.join(self.options.compmethods)
                request.headers['Accept-Encoding'] = compmethods
                log.debug('requesting the following compressions: %s', compmethods)

            if self.options.useragent != '':
                request.headers['User-Agent'] = self.options.useragent

            return request

        # This function post-processes the reply after receiving it (obvious!)
        # In my opinion, the base class Transport should define it as an empty stub
        # or simply with "return reply"
        def postreply(self, reply):
            """
            Do postprocessing of the received reply before returning it

            @param reply: the reply to process
            @type reply: suds.transport.Reply
            @return: the reply (although the reference is being modified)
            @rtype: suds.transport.Replay
            """
            if self.options.compression in ['yes', 'auto']:
                for header, headerval in reply.headers.iteritems():
                    if header.lower() == 'content-encoding':
                        log.debug('http reply with a content-encoding header')
                        if headerval == 'gzip':
                            log.debug('decompressing gzip content')
                            replydatafile = cStringIO.StringIO(reply.message)
                            gzipper = gzip.GzipFile(fileobj=replydatafile)
                            reply.message = gzipper.read()
                        elif headerval == 'deflate':
                            # decompress the deflate content
                            log.debug('decompressing deflate content')
                            try:
                                reply.message = zlib.decompress(reply.message)
                            except zlib.error:
                                # Many web sites fail to send the first bytes of the header
                                reply.message = zlib.decompress(reply.message, -zlib.MAX_WBITS)
                        elif headerval == 'bzip2':
                            # decompress bzip content
                            log.debug('decompressing unix compress content')
                            reply.message = bz2.decompress(reply.message)
                        else:
                            # unknown scheme
                            log.debug('unsupported content-encoding scheme')
                        break

            return reply
