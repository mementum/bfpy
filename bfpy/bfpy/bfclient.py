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
BfClient object implementation.
'''

from bfapi2 import BfApi
from bfservice import BfService
import bfclientext 


class BfClient(BfApi):

    __metaclass__ = BfService

    # Methods that override base class non-data descriptors, are implemented
    # as non-data descriptors also (simple override doesn't work)
    serviceDefs = [
        bfclientext.GetEvents(),
        bfclientext.GetCurrentBets(),
        bfclientext.PlaceBets(),
        ]

    def __init__(self, **kwargs):
        BfApi.__init__(self, **kwargs)


    def reLogin(self):
        return self.login(username=self.username, password=self.password,
                          productId=self.productId, vendorSoftwareId=self.vendorSoftwareId)


# Alias to look like version 1 of the API
Betfair = BfClient
