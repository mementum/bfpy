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

class BfError(Exception):

    def __init__(self, *args):
        Exception.__init__(self, *args)
        self.requestName = args[0]
        self.name = args[0]
        self.response = args[1]
        self.object = args[1]
        self.text = args[2]
        self.errorCode = args[3]


class BfPythonError(BfError):

    def __init__(self, *args):
        BfError.__init__(self, *args)


class BfSudsError(BfError):

    def __init__(self, *args):
        BfError.__init__(self, *args)


class BfTransportError(BfError):
    def __init__(self, *args):
        BfError.__init__(self, *args)


class BfNetworkError(BfTransportError):

    def __init__(self, *args):
        BfTransportError.__init__(self, *args)


class BfHttpError(BfTransportError):

    def __init__(self, *args):
        BfTransportError.__init__(self, *args)


class BfBetfairError(BfError):

    def __init__(self, *args):
        BfError.__init__(self, *args)


class BfApiError(BfBetfairError):

    def __init__(self, *args):
        BfBetfairError.__init__(self, *args)


class BfServiceError(BfBetfairError):

    def __init__(self, *args):
        BfBetfairError.__init__(self, *args)


class BfApplicationError(BfBetfairError):

    def __init__(self, *args):
        BfBetfairError.__init__(self, *args)

