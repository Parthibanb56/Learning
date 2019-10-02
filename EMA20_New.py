# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:51:46 2019

@author: Parthiban
"""

##SQL data capture for EMA 20 stratagy
##https://pynative.com/python-mysql-select-query-to-fetch-data/
import mysql.connector as mysql
import json

from oandapyV20.contrib.requests import MarketOrderRequest
#from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails
from oandapyV20.contrib.requests import LimitOrderRequest

import oandapyV20.endpoints.orders as orders
from oandapyV20 import API    # the client

db = mysql.connect(
    host = "localhost",
    user = "robotuser",
    passwd = "robotpass",
    database = "testdb"
)

access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
accountID = "101-011-12154697-001"
api = API(access_token=access_token)

cursor = db.cursor()

cursor.execute("select * from tbloandaprice ORDER BY TimeStamp ASC")

myresult = cursor.fetchall()

print("Total number of rows is: ", cursor.rowcount)

loopVal=1

lastVal=""
closedVal=""
timestamp=""

flgLastbuy="NO"
flgLastsell="NO"


for x in myresult:
    if loopVal==cursor.rowcount-1:
        print("Price - ",x[5])
        lastVal=x[5]
        flgLastbuy=x[6]
        flgLastsell=x[7]
    loopVal+=1
    closedVal=x[4]
    timestamp=x[0]
    
if lastVal=="":
    lastVal=closedVal
    
print("Last Amount - ",lastVal)
print("Closed Amount - ",closedVal)
print("Present Timestamp - ",timestamp)

#Formule =D80*2/(20+1)+F79*(1-2/(20+1)) --- Col no D row is 80

EMA20=float(closedVal)*2/(20+1)+float(lastVal)*(1-2/(20+1))
#Test - EMA20=float("1.11565")*2/(20+1)+float("1.1063")*(1-2/(20+1))

print("EMA20 Price - ",round(EMA20,5))

flgbuy="No"
flgsell="No"

#EMA>Closing - Sell and EMA<Closing - Buy
if float(round(EMA20,5))<float(closedVal):
    print("Process Buy")
    if flgLastbuy=="No":
        mktOrder = LimitOrderRequest(
        instrument="EUR_USD",
        units=100,price=float(closedVal))   #price=float(round(EMA20,5)))
    
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
        flgbuy="Yes"
    else:
        flgbuy="NA"
    
    
elif float(round(EMA20,5))>float(closedVal):
    print("Process Sell")
    if flgLastsell=="No":
        mktOrder = LimitOrderRequest(
        instrument="EUR_USD",
        units=-100,price=float(closedVal))  #price for select manual
    
        print(json.dumps(mktOrder.data, indent=4))
        
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
        flgsell="Yes"
    else:
        flgsell="NA"
else:
    print("No Action")
    
query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"'\
,Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(round(EMA20,5))+"' \
WHERE TimeStamp = '"+str(timestamp)+"'"

print(query)

cursor.execute(query)
db.commit()


  
