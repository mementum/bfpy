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
# Timezone classes. Adapted (if needed) from the Python documentation to make
# them more generic
#

from datetime import datetime, timedelta, tzinfo
import time as _time

class UTC(tzinfo):
    ZERO = timedelta(0)

    def utcoffset(self, dt):
        return UTC.ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return UTC.ZERO


class GMT(tzinfo):
    def __init__(self, timeOffset=0):
        self.timeOffset = timeOffset

    def utcoffset(self, dt):
        return timedelta(hours=self.timeOffset) + self.dst(dt)

    def dst(self, dt):
        d = datetime(dt.year, 4, 1) # DST starts last Sunday in March
        self.dston = d - timedelta(days=d.weekday() + 1)

        d = datetime(dt.year, 11, 1) # DST ends last Sunday in October
        self.dstoff = d - timedelta(days=d.weekday() + 1)

        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            deltaVal = 1
        else:
            deltaVal = 0

        return timedelta(hours=deltaVal)

    def tzname(self, dt):
        text = 'GMT'
        if self.timeOffset > 0:
            text += '+' + self.timeOffset
        elif self.timeOffset < 0:
            text += '-' + self.timeOffset

        return text


class LocalTimezone(tzinfo):
    ZERO = timedelta(0)
    STDOFFSET = timedelta(seconds=-_time.timezone)
    if _time.daylight:
        DSTOFFSET = timedelta(seconds=-_time.altzone)
    else:
        DSTOFFSET = STDOFFSET

    DSTDIFF = DSTOFFSET - STDOFFSET

    def utcoffset(self, dt):
        if self._isdst(dt):
            return LocalTimezone.DSTOFFSET
        else:
            return LocalTimezone.STDOFFSET

    def dst(self, dt):
        if self._isdst(dt):
            return LocalTimezone.DSTDIFF
        else:
            return LocalTimezone.ZERO

    def tzname(self, dt):
        return _time.tzname[self._isdst(dt)]

    def _isdst(self, dt):
        tt = (dt.year, dt.month, dt.day,
              dt.hour, dt.minute, dt.second,
              dt.weekday(), 0, -1)
        stamp = _time.mktime(tt)
        tt = _time.localtime(stamp)
        return tt.tm_isdst > 0
