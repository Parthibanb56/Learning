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
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.trades as trades
#from oandapyV20.contrib.requests import OrderReplace

#db = mysql.connect(
#    host = "localhost",
#    user = "robotuser",
#    passwd = "robotpass",
#    database = "testdb"
#)
#
#access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
#accountID = "101-011-12154697-001"
#api = API(access_token=access_token)
#
#
###Get Last Order ID
#r = orders.OrderList(accountID)
#api.request(r)
#rv=api.request(r)
#print (r.response)
#
#print(rv['lastTransactionID'])
#
#
#
#####################
#
##import oandapyV20
#
#
#r = positions.PositionDetails(accountID=accountID,instrument="EUR_USD")
#api.request(r)
##print (r.response)
###############
#
##Get Order details with order ID
#
#try:
#    r1 = orders.OrderDetails(accountID=accountID, orderID=int(rv['lastTransactionID'])-0)
#    print("@1")
#    rv=api.request(r1)
#    print("@2")
#    print(r1.response)
#except:
#    print("@3")
#    print(r1.expected_status)
#else:
#    print("@4")
#    print(json.dumps(rv, indent=2))

##
#mktOrder = MarketOrderRequest(instrument="EUR_USD",units=10000)
#        # create the OrderCreate request
#r = orders.OrderCreate(accountID, data=mktOrder.data)
#        
#try:
#   # create the OrderCreate request
#   rv = api.request(r)  
#   print("ID Processed - " + rv['orderCreateTransaction']['id'])
#   print("ID Actual - " + rv['orderFillTransaction']['tradeOpened']['tradeID'])
#except API.exceptions.V20Error as err:
#            print(r.status_code, err)
#else:
#            print(json.dumps(rv, indent=2))
#            
#

##Update Stop Loss with ID
#from oandapyV20.contrib.requests import StopLossOrderRequest
#
##ordr = StopLossOrderRequest(tradeID=rv['orderFillTransaction']['tradeOpened']['tradeID'], price=1.10445)
#ordr = StopLossOrderRequest(tradeID=291, price=1.10446)
#print(json.dumps(ordr.data, indent=4))
#
## now we have the order specification, create the order request
#r = orders.OrderCreate(accountID, data=ordr.data)
## perform the request
#rv = api.request(r)
#print(json.dumps(rv, indent=4))
#    
#Replace Order
import oandapyV20.endpoints.trades as trades
#import oandapyV20.endpoints.orders as orders
access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
accountID = "101-011-12154697-001"
api = API(access_token=access_token)
#EUR_USD_STOP_LOSS = 1.1044
#data ={"order": {"instrument": "EUR_USD", "stopLossOnFill":StopLossDetails(price=EUR_USD_STOP_LOSS).data}}
#r = orders.OrderReplace(accountID=accountID, orderID=279, data=data)
##r = StopLossOrderRequest(tradeID=291, price=1.10446)
#api.request(r)
#print(r.response)

#
#import oandapyV20.endpoints.instruments as instruments
#params = None
#r = instruments.InstrumentsCandles(instrument="EUR_USD",params=params)
#api.request(r)
#print (r.response)


###Check open order###############################################
#import oandapyV20.endpoints.orders as orders
#access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
#accountID = "101-011-12154697-001"
#api = API(access_token=access_token)


#print(r.response)

##Update Order#####################################################

r=trades.OpenTrades(accountID=accountID)
#data ={"takeProfit": {"stopLoss": {"timeInForce": "GTC","price": "1.09958"}}
data ={"stopLoss": {"timeInForce": "GTC","price": "1.09990"}}
r=trades.TradeCRCDO(accountID=accountID, tradeID=416, data=data)
rv = api.request(r)  
print(json.dumps(rv, indent=4))

#
#r=trades.OpenTrades(accountID=accountID)
#    #api.request(r)
#activeID=False
#activeStatus=""
#try:
#        rv = api.request(r)  
#        print("Tran ID - " + rv['lastTransactionID'])
#        TranID=rv['lastTransactionID']
#        print("ID - " + rv['trades'][0]['id'])
#        print("Status - " + rv['trades'][0]['state'])
#        print("Status - " + str(float(rv['trades'][0]['currentUnits']))) 
#        
#        activeStatus=rv['trades'][0]['state']
#        activeID=True
#        TranID=rv['trades'][0]['id']
#except:
#        print("Error")
#else:
#        print(json.dumps(rv, indent=4))
#
#
#if float("-1000")>0:
#    print("pass")
#else:
#    print("fail")


