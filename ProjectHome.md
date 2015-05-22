Python (>= 2.6.3/2.7.x) library to communicate with the Betfair Betting Exchange

## Introduction ##
BfPy eases the communication with the Betfair API by:

  * Automated session management
  * Default value for parameters for many calls (where they make sense)
  * Default value for parameters wrongly described in the Betfair documentation as "non-mandatory" (although the WSDL file)
  * Automatic removal of nullified arrays with empty arrays to allow seamless array iteration
  * In-built (configurable) data request throttler to comply with Betfair Data Request policies
  * Adherence to Betfair naming policies for calls
  * Easy parameter passing to calls (avoids creation and management of request objects)
  * Translation of API responses to Python data types and objects
  * Printable responses for easy inspection of objects
  * In-built multi-threading support
  * Adding extended calls to supplement "missing" functionality in the Betfair API
  * Error handling with Python Exceptions (all deriving from BfError)

BfPy supports:

  * Full Transactional API (Global, Exchange)
  * Full Software Vendor API (first Open Source library allowed to publish it)
  * In-built support for the UK and Australian exchanges

BfPy uses (included in the sources):

  * HttxLib - A Python HTTP/HTTPS Open Source Library for optimum performance and multithreaded support

## Quick Example ##
```
import bfpy
bf = bfpy.BfClient()

try:
  bfresp = bf.login(username='yourusername', password='yourpassword')
except bfpy.BfError, e:
  print "login error: %s" % str(e)
else:
  print bfresp

# And now execute a keepAlive

try:
  bfresp = bf.keepAlive()
except bfpy.BfErrror, e:
  print "keepAlive error: %s" % str(e)
else:
  print bfresp
```

If you followed the Betfair API documentation, this would have been the natural path for the login call
  * Parse the WSDL file
  * To call login, first create a LoginReq object
  * Fill the values: username, password, ipAddress, productId, location, softwareVendorId
  * Send it
  * Parse the XML
  * Handle error codes (in the APIResponseHeader for general API errors and the error codes for the call, plus the network errors)

Once satisfied and to call the keepAlive call (that has no parameters):
  * Create a KeepAliveReq object
  * Create an APIRequestHeader
  * Fill the APIRequestHeader with sessionToken, clientTimestamp
  * Send it
  * ...

And this time there were no parameters. You have probably perceived how the library has eased Session Management and created the "XXXReq" in the background (and the APIRequestHeader) and how everything was parsed in the background to give you a printable object.

## Extended Services ##

  * placeBets
> Sometimes it is impossible to know if placing a bet with keep In-Play will succeed or not because it is unknown if the market will turn In-Play.
> Calling placeBets with `_nonIPRePlace` set to True, the call will immediately re-Place the bet if it fails due to a non-In-Play error
  * getEvents
> It creates a blend of the original getEvents and getActiveEventTypes, to allow seamless recursion from the top events (the ActiveEventTypes) down to BFEvent and Markets
  * getCurrentBets
> That simulates a betStatus='MU', which is not accepted by the Betfair API (M or U have to be passed) returning a unified list of current matched and unmatched bets

## Another Example ##
```
import bfpy

bf = bfpy.BfClient()
try:
  bfresp  = bf.login(username='user', password='pass')
except bfpy.BfError, e:
  print "login error: %s" % str(e)
else:
  print bfresp

try:
  bfresp = bf.getAllEventTypes()
except bfpy.BfError, e:
  print "getAllEvents error: %s" % str(e)
else:
  print bfresp
```

More examples can be found in the sources under the a directory called tests.

A working application is: Bfplusplus (http://code.google.com/p/bfplusplus)