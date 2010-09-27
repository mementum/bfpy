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
# ByPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

version = 0.50

try:
    import suds
except ImportError:
    # If no high level suds module exists, import the internal suds copy
    # But because suds expects to be at the top of the hierarchy, the import
    # has to be faked by loading it with a top hierarchy name but from the
    # local directory
    import imp
    import os.path
    moddir = os.path.dirname(__file__)
    module = imp.load_module('suds', None, '%s/suds' % moddir, ('.py', 'r', imp.PKG_DIRECTORY))
    # Create the suds symbol
    suds = module

from betfair import *
from bfapi import *
from bferror import *
