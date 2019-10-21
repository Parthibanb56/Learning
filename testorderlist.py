# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 06:26:07 2019

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:40:22 2019

@author: Admin
"""

import mysql.connector as mysql
import json

from oandapyV20.contrib.requests import MarketOrderRequest

import oandapyV20.endpoints.orders as orders
from oandapyV20 import API    # the client
from oandapyV20.contrib.requests import *
#from oandapyV20.contrib.requests import OrderReplace

db = mysql.connect(
    host = "localhost",
    user = "robotuser",
    passwd = "robotpass",
    database = "testdb"
)

access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
accountID = "101-011-12154697-001"
api = API(access_token=access_token)


##Get Last Order ID
r = orders.OrderList(accountID)
api.request(r)
rv=api.request(r)
print (r.response)

print(rv['lastTransactionID'])

##Get Order details with order ID

#r1 = orders.OrderDetails(accountID=accountID, orderID=rv['lastTransactionID'])
#api.request(r1)
#print(r1.response)

#
mktOrder = MarketOrderRequest(instrument="EUR_USD",units=10000)
        # create the OrderCreate request
r = orders.OrderCreate(accountID, data=mktOrder.data)
        
try:
   # create the OrderCreate request
   rv = api.request(r)  
   print("ID Processed - " + rv['orderCreateTransaction']['id'])
   print("ID Actual - " + rv['orderFillTransaction']['tradeOpened']['tradeID'])
except API.exceptions.V20Error as err:
            print(r.status_code, err)
else:
            print(json.dumps(rv, indent=2))
            


##Update Stop Loss with ID
from oandapyV20.contrib.requests import StopLossOrderRequest

ordr = StopLossOrderRequest(tradeID=rv['orderFillTransaction']['tradeOpened']['tradeID'], price=1.11445)
print(json.dumps(ordr.data, indent=4))

# now we have the order specification, create the order request
r = orders.OrderCreate(accountID, data=ordr.data)
# perform the request
rv = api.request(r)
print(json.dumps(rv, indent=4))




            