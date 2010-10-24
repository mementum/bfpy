import sys

import bfpy
import bfpy.bfclient as bfclient

print 'Creating a Betfair Client'
bf = bfclient.BfClient()
print 'Created a Betfair Client'

loginInfo = sys.modules['__main__'].loginInfo

response = bf.login(**loginInfo)
print response

response = bf.keepAlive()
print response

response = bf.reLogin()
print response

response = bf.logout()
print response

response = bf.reLogin()
print response
