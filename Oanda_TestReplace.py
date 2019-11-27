# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:40:22 2019

@author: Admin
"""

import mysql.connector as mysql
import json

#from oandapyV20.contrib.requests import LimitOrderRequest

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


###################Replace order stoploss and take profit#######
#
#import oandapyV20.endpoints.trades as trades
#
#data ={"stopLoss": {"timeInForce": "GTC","price": "1.09"}}
#
#r=trades.TradeCRCDO(accountID=accountID, tradeID='323',data =data)
#api.request(r)
#print(r.response)

#################################################################

###Check open order###############################################
#import oandapyV20.endpoints.trades as trades
#r=trades.OpenTrades(accountID=accountID)
##api.request(r)
#try:
#    rv = api.request(r)  
#    print("Tran ID - " + rv['lastTransactionID'])
#    print("ID - " + rv['trades'][0]['id'])
#    print("Status - " + rv['trades'][0]['state'])
#except:
#    print("Error")
#else:
#    print(json.dumps(rv, indent=4))


################################################################
#
####Get Last candle details######################################
#import oandapyV20.endpoints.instruments as instruments
#      
#data ={"count": 2,"granularity": "M15"}      
#r=instruments.InstrumentsCandles(instrument="EUR_USD",params=data)
##api.request(r)
#
#rv = api.request(r)  
#print("ID - " + rv['instrument'])
#print("Complete Status - " + str(rv['candles'][0]['complete']))
#print("Last Closed Price - " + rv['candles'][0]['mid']['c'])
#print(json.dumps(rv, indent=2))

##################################################################

query = "UPDATE tbloandaprice SET EMA20 = '"+str(round("1.0098",5))+"',Buy = '"+"No"+"',Sell = '"+"NO"+"',Processed_Amt = '"+str(float("1.0098"))+"',orderID = '"+"1.0098"+"' WHERE TimeStamp = '"+str("aaa")+"'"
    
print(query)
