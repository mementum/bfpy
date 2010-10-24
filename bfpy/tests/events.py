import sys

import bfpy
import bfpy.bfclient as bfclient

print 'Creating a Betfair Client'
bf = bfclient.BfClient()
print 'Created a Betfair Client'

loginInfo = sys.modules['__main__'].loginInfo

response = bf.login(**loginInfo)
print response

response = bf.getActiveEventTypes()
print response

response = bf.getAllEventTypes()
print response

response = bf.getEvents(eventParentId=-1)
print response

response = bf.getEvents(eventParentId=1)
print response
