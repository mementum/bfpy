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
BfPy utility classes
'''

import logging

class NullHandler(logging.Handler):
    '''
    Definition of a Null logging class to avoid any output
    from suds
    '''
    def emit(self, record):
        '''
        Simply discard the incoming param and does nothing

        @param record: logging record
        @type record: str
        '''
        pass


# Code from suds: no changes
def tostr(obj, encoding=None):
    """ get a unicode safe string representation of an obj """
    if isinstance(obj, basestring):
        if encoding is None:
            return obj
        else:
            return obj.encode(encoding)
    if isinstance(obj, tuple):
        s = ['(']
        for item in obj:
            if isinstance(item, basestring):
                s.append(item)
            else:
                s.append(tostr(item))
            s.append(', ')
        s.append(')')
        return ''.join(s)
    if isinstance(obj, list):
        s = ['[']
        for item in obj:
            if isinstance(item, basestring):
                s.append(item)
            else:
                s.append(tostr(item))
            s.append(', ')
        s.append(']')
        return ''.join(s)
    if isinstance(obj, dict):
        s = ['{']
        for item in obj.items():
            if isinstance(item[0], basestring):
                s.append(item[0])
            else:
                s.append(tostr(item[0]))
            s.append(' = ')
            if isinstance(item[1], basestring):
                s.append(item[1])
            else:
                s.append(tostr(item[1]))
            s.append(', ')
        s.append('}')
        return ''.join(s)
    try:
        return unicode(obj)
    except:
        return str(obj)

# Code from suds (removed the 'Object' references
# to do a pretty print of an object
class Printer(object):
    """ 
    Pretty printing of a Object object.
    """
    
    @classmethod
    def indent(cls, n): return '%*s'%(n*3,' ')

    def tostr(self, obj, indent=-2):
        """ get s string representation of object """
        history = []
        return self.process(obj, history, indent)
    
    def process(self, obj, h, n=0, nl=False):
        """ print obj using the specified indent (n) and newline (nl). """
        if obj is None:
            return 'None'
        if isinstance(obj, EmptyObject):
            if len(obj) == 0:
                return '<empty>'
            else:
                return self.print_object(obj, h, n+2, nl)
        if isinstance(obj, dict):
            if len(obj) == 0:
                return '<empty>'
            else:
                return self.print_dictionary(obj, h, n+2, nl)
        if isinstance(obj, (list,tuple)):
            if len(obj) == 0:
                return '<empty>'
            else:
                return self.print_collection(obj, h, n+2)
        if isinstance(obj, basestring):
            return '"%s"' % tostr(obj)
        return '%s' % tostr(obj)
    
    def print_object(self, d, h, n, nl=False):
        """ print complex using the specified indent (n) and newline (nl). """
        s = []
        cls = d.__class__
        if d in h:
            s.append('(')
            s.append(cls.__name__)
            s.append(')')
            s.append('...')
            return ''.join(s)
        h.append(d)
        if nl:
            s.append('\n')
            s.append(self.indent(n))

        s.append('(')
        s.append(cls.__name__)
        s.append(')')
        s.append('{')

        for item in d.__dict__.iteritems():
            # item = self.unwrap(d, item)
            s.append('\n')
            s.append(self.indent(n+1))
            if isinstance(item[1], (list,tuple)):            
                s.append(item[0])
                s.append('[]')
            else:
                s.append(item[0])
            s.append(' = ')
            s.append(self.process(item[1], h, n, True))
        s.append('\n')
        s.append(self.indent(n))
        s.append('}')
        h.pop()
        return ''.join(s)

    def print_dictionary(self, d, h, n, nl=False):
        """ print complex using the specified indent (n) and newline (nl). """
        if d in h: return '{}...'
        h.append(d)
        s = []
        if nl:
            s.append('\n')
            s.append(self.indent(n))
        s.append('{')
        for item in d.items():
            s.append('\n')
            s.append(self.indent(n+1))
            if isinstance(item[1], (list,tuple)):            
                s.append(tostr(item[0]))
                s.append('[]')
            else:
                s.append(tostr(item[0]))
            s.append(' = ')
            s.append(self.process(item[1], h, n, True))
        s.append('\n')
        s.append(self.indent(n))
        s.append('}')
        h.pop()
        return ''.join(s)

    def print_collection(self, c, h, n):
        """ print collection using the specified indent (n) and newline (nl). """
        if c in h: return '[]...'
        h.append(c)
        s = []
        for item in c:
            s.append('\n')
            s.append(self.indent(n))
            s.append(self.process(item, h, n-2))
            s.append(',')
        h.pop()
        return ''.join(s)
    

class EmptyObject(object):
    '''
    Used to implement objects, like those arising from
    compressed answers
    '''
    printer = Printer()
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        return self.printer.tostr(self)

    def __len__(self):
        return len(self.__dict__)


