# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:40:22 2019

@author: Admin
"""

import mysql.connector as mysql
import json

#from oandapyV20.contrib.requests import LimitOrderRequest

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

#mktOrder = MarketOrderRequest(instrument="EUR_USD",units=10000)
#        # create the OrderCreate request
#r = orders.OrderCreate(accountID, data=mktOrder.data)
#        
#try:
#   # create the OrderCreate request
#   rv = api.request(r)  
#   print("ID - " + rv['orderCreateTransaction']['id'])
#except API.exceptions.V20Error as err:
#            print(r.status_code, err)
#else:
#            print(json.dumps(rv, indent=2))
#            

#ordr = OrderReplace(price: "1.25000")
#
#r = orders.OrderCreate(accountID, data=ordr.data)
#rv = api.request(r)
#print(json.dumps(rv, indent=4))

r = orders.OrderDetails(accountID=accountID, orderID='221')
api.request(r)
print(r.response)

#EUR_USD_TAKE_PROFIT = 1.10966
#print("#1")
#mktOrder = MarketOrderRequest(
#    instrument="EUR_USD",
#    units=100,
#    takeProfitOnFill=TakeProfitDetails(price=EUR_USD_TAKE_PROFIT).data,
#    stopLossOnFill=StopLossDetails(price=EUR_USD_STOP_LOSS).data)
EUR_USD_TAKE_PROFIT = 1.09817

#params ={"stopLossOnFill":"StopLossDetails(price=EUR_USD_STOP_LOSS).data"}

data ={"order": {"stopLossOnFill": StopLossDetails(price=EUR_USD_STOP_LOSS).data}}

r=OrderReplace(accountID=accountID, orderID='221',params =params)
api.request(r)
print(r.response)


            