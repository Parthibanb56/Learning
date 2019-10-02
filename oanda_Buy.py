##https://www.quantstart.com/articles/Forex-Trading-Diary-2-Adding-a-Portfolio-to-the-OANDA-Automated-Trading-System

import json

from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails

import oandapyV20.endpoints.orders as orders
from oandapyV20 import API    # the client

#from exampleauth import exampleAuth


#accountID, access_token = exampleAuth()
#api = oandapyV20.API(access_token=access_token)

#access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
#accountID = "101-011-12154697-001"

access_token = "1a9a034c3e637d5721281edc1f7461e1-0b2e59994d3ef7c4fc9a5d67a67d5a65"
accountID = "101-011-7592314-001"
api = API(access_token=access_token)

# EUR_USD (today 1.0750)
EUR_USD_STOP_LOSS = 1.07966
EUR_USD_TAKE_PROFIT = 1.10966
print("#1")
mktOrder = MarketOrderRequest(
    instrument="EUR_USD",
    units=100)

("#2")
# create the OrderCreate request
r = orders.OrderCreate(accountID, data=mktOrder.data)

try:
    # create the OrderCreate request
    rv = api.request(r)
    print("Pass")
except API.exceptions.V20Error as err:
    print(r.status_code, err)
else:
    print(json.dumps(rv, indent=2))