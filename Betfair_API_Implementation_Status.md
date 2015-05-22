**The Full API is now implemented directly**. The table below is kept for historical purposes (and reference). If you happen to find an error in on of the calls, please use the issue tracker.

|API\_Services|Name|Status|Tested|Extended|ArrayUnfix|PreProcess|ArrayFix|PostProcess|skipErrorCodes|Needs Full API|Throttle|
|:------------|:---|:-----|:-----|:-------|:---------|:---------|:-------|:----------|:-------------|:-------------|:-------|
|General      |login|Done  |Yes   |        |          |          |        |           |              |No            |24      |
|General      |logout|Done  |Yes   |        |          |          |        |           |              |No            |        |
|General      |reLogin|Done  |Yes   |Yes     |          |          |        |           |              |No            |24      |
|General      |keepAlive|Done  |Yes   |        |          |          |        |           |              |No            |        |
|Read-Only    |convertCurrency|Done  |Yes   |        |          |          |        |           |              |Yes           |        |
|Read-Only    |getAllCurrencies|Done  |Yes   |        |          |          |Yes     |           |              |Yes           |        |
|Read-Only    |getAllCurrenciesV2|Done  |Yes   |        |          |          |Yes     |           |              |Yes           |        |
|Read-Only    |getAllEventTypes|Done  |Yes   |        |          |          |Yes     |           |NO\_RESULTS   |No            |        |
|Read-Only    |getAllMarkets|Done  |Yes   |        |          |          |        |Yes        |NO\_RESULTS   |No            |        |
|Read-Only    |getActiveEventTypes|Done  |Yes   |        |          |          |Yes     |           |NO\_RESULTS   |No            |        |
|Read-Only    |getBet|Done  |Yes   |        |          |          |Yes     |           |NO\_RESULTS   |No            |60      |
|Read-Only    |getBetHistory|Done  |Yes   |        |Yes       |          |        |           |NO\_RESULTS   |No            |1       |
|Read-Only    |getBetLite|Done  |Yes   |        |          |          |        |           |NO\_RESULTS   |No            |60      |
|Read-Only    |getBetMatchesLite|Done  |Yes   |        |          |          |        |           |NO\_RESULTS   |No            |60      |
|Read-Only    |getCompleteMarketPricesCompressed|Done  |Yes   |        |          |          |        |Yes        |              |No            |60      |
|Read-Only    |getCurrentBets|Done  |Yes   |Yes     |          |          |Yes     |Yes        |NO\_RESULTS   |No            |60      |
|Read-Only    |getCurrentBetsLite|Done  |Yes   |        |          |          |Yes     |           |NO\_RESULTS   |No            |60      |
|Read-Only    |getDetailAvailableMarketDepth|Done  |Yes   |        |          |          |        |Yes        |              |No            |60      |
|Read-Only    |getEvents|Done  |Yes   |Yes     |          |          |Yes     |           |NO\_RESULTS   |No            |        |
|Read-Only    |getInPlayMarkets|Done  |Yes   |        |          |          |        |Yes        |NO\_RESULTS   |Yes           |        |
|Read-Only    |getMarket|Done  |Yes   |        |          |          |        |Yes        |              |No            |5       |
|Read-Only    |getMarketInfo|Done  |Yes   |        |          |          |        |Yes        |              |No            |5       |
|Read-Only    |getMarketPrices|Done  |Yes   |        |          |          |        |Yes        |              |No            |10      |
|Read-Only    |getMarketPricesCompressed|Done  |Yes   |        |          |          |        |Yes        |              |No            |60      |
|Read-Only    |getMarketTradedVolume|Done  |Yes   |        |          |          |        |Yes        |NO\_RESULTS, MARKET\_CLOSED|No            |60      |
|Read-Only    |getMarketTradedVolumeCompressed|Done  |Yes   |        |          |          |        |Yes        |EVENT\_SUSPENDED, EVENT\_CLOSED|No            |60      |
|Read-Only    |getMUBets|Done  |Yes   |        |          |          |Yes     |           |NO\_RESULTS, MARKET\_CLOSED|No            |60      |
|Read-Only    |getMUBetsLite|Done  |Yes   |        |          |          |Yes     |           |NO\_RESULTS, MARKET\_CLOSED|No            |60      |
|Read-Only    |getPrivateMarkets|Done  |Yes   |        |          |          |        |           |NO\_RESULTS   |No            |        |
|Read-Only    |getSilks|Done  |Yes   |        |          |          |        |           |              |Yes           |        |
|Read-Only    |getSilksV2|Done  |Yes   |        |          |          |        |           |              |Yes           |        |
|Bet Placement|cancelBets|Done  |Yes   |        |Yes       |          |Yes     |           |              |No            |        |
|Bet Placement|cancelBetsByMarket|Done  |Yes   |        |          |          |Yes     |           |              |Yes           |        |
|Bet Placement|placeBets|Done  |Yes   |Yes     |Yes       |          |Yes     |           |              |No            |100     |
|Bet Placement|updateBets|Done  |Yes   |        |Yes       |          |Yes     |           |              |No            |        |
|Account Management|getAccountFunds|Done  |Yes   |        |          |          |        |           |              |No            |12      |
|Account Management|transferFunds|Done  |Yes   |        |          |          |        |           |              |No            |        |
|Account Management|addPaymentCard|Done  |No    |        |          |          |        |           |              |Yes           |        |
|Account Management|deletePaymentCard|Done  |No    |        |          |          |        |           |              |Yes           |        |
|Account Management|depositFromPaymentCard|Done  |No    |        |          |          |        |           |              |Yes           |        |
|Account Management|forgotPassword|Done  |No    |        |          |          |        |           |              |Yes           |        |
|Account Management|getAccountStatement|Done  |Yes   |        |Yes       |          |Yes     |           |              |No            |1       |
|Account Management|getPaymentCard|Done  |No    |        |          |          |        |           |              |Yes           |        |
|Account Management|getSubscriptionInfo|Done  |Yes   |        |          |          |Yes     |           |              |No            |        |
|Account Management|modifyPassword|Done  |Yes   |        |          |          |        |           |              |Yes           |        |
|Account Management|modifyProfile|Done  |No    |        |          |          |        |           |              |No            |        |
|Account Management|retrieveLIMBMessage|Done  |No    |        |          |          |        |Yes        |              |Yes           |        |
|Account Management|selfExclude|Done  |No    |        |          |          |        |           |              |No            |        |
|Account Management|setChatName|Done  |No    |        |          |          |        |           |              |N/A           |        |
|Account Management|submitLIMBMessage|Done  |No    |        |          |Yes       |        |           |              |Yes           |        |
|Account Management|updatePaymentCard|Done  |No    |        |          |          |        |           |              |Yes           |        |
|Account Management|viewProfile|Done  |Yes   |        |          |          |        |           |              |Yes           |        |
|Account Management|viewProfileV2|Done  |No    |        |          |          |        |           |              |N/A           |        |
|Account Management|viewReferAndEarn|Done  |Yes   |        |          |          |        |           |NO\_RESULTS   |No            |        |
|Account Management|withdrawToPaymentCard|Done  |No    |        |          |          |        |           |              |Yes           |        |