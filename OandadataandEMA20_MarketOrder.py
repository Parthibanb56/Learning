"""
Created on Wed Oct  2 23:32:19 2019

@author: Parthiban
"""

#https://oanda-api-v20.readthedocs.io/en/latest/contrib/orders/marketorderrequest.html
#Steps:
#    1. Buy or Sell order decision based on EMA20
#    2. Created order with CMP(Corrent Market Price) - Marketorderrequest
#    3. Setup stop loss use last closed value

import oandapyV20.endpoints.pricing as pricing
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20 import API    # the client
import mysql.connector as mysql
import json
#from oandapyV20.contrib.requests import LimitOrderRequest
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.trades as trades


##Connect MySQL
db = mysql.connect(
    host = "localhost",
    user = "robotuser",
    passwd = "robotpass",
    database = "testdb"
)

cursor = db.cursor()

#access_token = "024af7bed182e0a42a205b39cc424598-f0f1aacef36bfaeb997ce4a4ea65278c"
#accountID = "101-011-12154697-001"
#
access_token = "1a9a034c3e637d5721281edc1f7461e1-0b2e59994d3ef7c4fc9a5d67a67d5a65"
accountID = "101-011-7592314-001"
api = API(access_token=access_token)

closedVal=""
####Get Last candle details######################################
import oandapyV20.endpoints.instruments as instruments
      
data ={"count": 2,"granularity": "M15"}      
r=instruments.InstrumentsCandles(instrument="EUR_USD",params=data)
#api.request(r)

rv = api.request(r)  
print("ID - " + rv['instrument'])
print("Complete Status - " + str(rv['candles'][0]['complete']))
print("Last Closed Price - " + rv['candles'][0]['mid']['c'])
closedVal=rv['candles'][0]['mid']['c']
#print(json.dumps(rv, indent=2))

currPrice=""
##Get current price
params ={"instruments": "EUR_USD"}        
r = pricing.PricingInfo(accountID=accountID, params=params)
rv = api.request(r)
#print (json.dumps(rv, indent=2))

for dt in rv['prices']:    
    print("instrument - " + dt['instrument'])
    print("type - " + dt['type'])
    print("time - " + dt['time'])
    print("Current price - " + dt['bids'][0]['price'])
    currPrice=dt['bids'][0]['price']
    ## defining the Query
    query = "INSERT INTO tbloandaprice (instrument,Type, Time, Price) VALUES (%s, %s, %s, %s)"
    ## storing values in a variable
    values = (dt['instrument'], dt['type'],dt['time'],dt['bids'][0]['price'])
    
    ## executing the query with values
    cursor.execute(query, values)
    
    ## to make final output we have to run the 'commit()' method of the database object
    db.commit()

###################################################################################
    
##SQL data capture for EMA 20 stratagy

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
timestamp=""

flgLastbuy="NO"
flgLastsell="NO"
LastTranID="NA"

for x in myresult:
    if loopVal==cursor.rowcount-1:
        print("Price - ",x[4])
        lastVal=x[4]
        flgLastbuy=x[6]
        flgLastsell=x[7]
        LastTranID=x[9]
    loopVal+=1
    #closedVal=x[4]
    timestamp=x[0]
    
if lastVal=="" or lastVal==None:
    lastVal=closedVal
    
print("Last Amount - ",lastVal)
print("Closed Amount - ",closedVal)
print("Present Timestamp - ",timestamp)
print("flgLastbuy - ",flgLastbuy)
print("flgLastsell - ",flgLastsell)
print("LastTranID - ",LastTranID)

flgOrderPresent=False

print("-------------------Check Open Order--------------------------")
##Check open order###############################################
r=trades.OpenTrades(accountID=accountID)
#api.request(r)
try:
    rv = api.request(r)  
    print("Tran ID - " + rv['lastTransactionID'])
    print("ID - " + rv['trades'][0]['id'])
    print("Status - " + rv['trades'][0]['state'])
    flgOrderPresent=True
except IndexError as err:
    print("ERROR: {}".format(err))
else:
    print(json.dumps(rv, indent=4))

print("----------------EMA20 Calculation----------------------------")
###EMA calculation
##Formule =D80*2/(20+1)+F79*(1-2/(20+1)) --- Col no D row is 80
#
EMA20=float(str(closedVal))*2/(20+1)+float(str(lastVal))*(1-2/(20+1))
##Test - EMA20=float("1.11565")*2/(20+1)+float("1.1063")*(1-2/(20+1))
#
print("EMA20 Price - ",round(EMA20,5))

print("Flag Order Present - ",flgOrderPresent)
flgbuy="No"
flgsell="No"

if flgOrderPresent==False:
    #########################New Buy or Sell order###################################    
    print("--------------Started Buy or Sell actions---------------------")
    TranID=""    
    print("Closed Val - ",closedVal)
    
    #EMA>Closing - Sell and EMA<Closing - Buy
    if float(round(EMA20,5))<float(closedVal):
        print("Process Buy")
        if flgLastbuy=="No" or flgLastbuy=="None":
            mktOrder = MarketOrderRequest(
            instrument="EUR_USD",
            units=10000)   #price=float(round(EMA20,5)))        
            # create the OrderCreate request
            r = orders.OrderCreate(accountID, data=mktOrder.data)            
            try:
                # create the OrderCreate request
                rv = api.request(r)
                print("ID - " + rv['orderCreateTransaction']['id'])
                print("ID Actual - " + rv['orderFillTransaction']['tradeOpened']['tradeID'])
                #TranID=rv['orderFillTransaction']['tradeOpened']['tradeID']
                print("Pass")
            except API.exceptions.V20Error as err:
                print(r.status_code, err)
            else:
                print(json.dumps(rv, indent=2))
            flgbuy="Yes"
        else:
            flgbuy="NA"
            TranID=LastTranID        
        
    elif float(round(EMA20,5))>float(closedVal):
        print("Process Sell")
        if flgLastsell=="No" or flgLastsell=="None":                
            mktOrder = MarketOrderRequest(
            instrument="EUR_USD",
            units=-10000)  #price for select manual
        
            # create the OrderCreate request
            r = orders.OrderCreate(accountID, data=mktOrder.data)
            
            try:
                # create the OrderCreate request
                rv = api.request(r)
                print("ID Actual - " + rv['orderFillTransaction']['tradeOpened']['tradeID'])
                #TranID=rv['orderFillTransaction']['tradeOpened']['tradeID']
                print("Pass")
            except API.exceptions.V20Error as err:
                print(r.status_code, err)
            else:
                print(json.dumps(rv, indent=2))
            flgsell="Yes"
        else:
            flgsell="NA"
            TranID=LastTranID
    else:
        print("No Action")        
    
    ##Check open order###############################################
    r=trades.OpenTrades(accountID=accountID)
    activeID=False
    try:
        rv = api.request(r)  
        print("Tran ID - " + rv['lastTransactionID'])
        TranID=rv['lastTransactionID']
        print("ID - " + rv['trades'][0]['id'])
        print("Status - " + rv['trades'][0]['state'])
        activeID=False
        
    except:
        print("Error")
    else:
        print(json.dumps(rv, indent=4))
     
    print("Order ID Active - ",activeID)
    
    query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
    
    print(query)
    
    cursor.execute(query)
    db.commit()
else:
    ##Update stop loss amount to order
    print("------------------Start Update Stop Loss------------------------")
    
    tradeType=""
    
    ##Check open order###############################################
    r=trades.OpenTrades(accountID=accountID)
    #api.request(r)
    activeID=False
    activeStatus=""
    try:
        rv = api.request(r)  
        print("Tran ID - " + rv['lastTransactionID'])
        TranID=rv['lastTransactionID']
        print("ID - " + rv['trades'][0]['id'])
        print("Status - " + rv['trades'][0]['state'])
        tradeType=float(rv['trades'][0]['currentUnits'])
        if float(rv['trades'][0]['currentUnits'])>0:
            tradeType="Buy"
        else:
            tradeType="Sell"
        activeStatus=rv['trades'][0]['state']
        activeID=True
        TranID=rv['trades'][0]['id']
    except:
        print("Error")
    else:
        print(json.dumps(rv, indent=4))
        
    print("Active ID - ",activeID)
    print("Active ID Status - ",activeStatus)
    
    if flgbuy=="Yes":
        flgbuy="NA"
            
    if flgsell=="Yes":
        flgsell="NA"    
        
    print("Current Price - ",currPrice)
    print("Closed Amount - ",closedVal)
    print("Trade Type - ",tradeType)
    print("Trade ID - ",TranID)
    
    acceptLoss=0.00500
    
    print("---------------Open order validation--------------------------")
    
    if activeID==True and activeStatus=="OPEN" and tradeType=="Buy":          
        print("Action started for Buy stop loss")
        if float(str(currPrice))>float(str(closedVal)):    
            
            print("Tran 1")
            #Update Stop Loss with ID
            #from oandapyV20.contrib.requests import StopLossOrderRequest
            #ordr = StopLossOrderRequest(tradeID=TranID, price=closedVal)
#            ordr = StopLossOrderRequest(tradeID=TranID, price=closedVal)
#            print(json.dumps(ordr.data, indent=4))
            
            data ={"stopLoss": {"timeInForce": "GTC","price": str(closedVal)}}
            r=trades.TradeCRCDO(accountID=accountID, tradeID=TranID, data=data)
            rv = api.request(r)  
            print(json.dumps(rv, indent=4))
            query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '"+str(float(closedVal))+"',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
            print(query)
            cursor.execute(query)
            db.commit()
        elif (float(str(currPrice))+acceptLoss)<float(str(closedVal)):    
            print("Tran 2")
            #Update Stop Loss with ID
            data ={"stopLoss": {"timeInForce": "GTC","price": str(currPrice)}}
            r=trades.TradeCRCDO(accountID=accountID, tradeID=TranID, data=data)
            rv = api.request(r)  
            print(json.dumps(rv, indent=4))
            query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '"+str(float(closedVal))+"',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
            print(query)
            cursor.execute(query)
            db.commit()
        
        else:
            print("Stop Loss Not Required for Buy")
            query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '""',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
            print(query)
            cursor.execute(query)
            db.commit()
    elif activeID==True and activeStatus=="OPEN" and tradeType=="Sell":          
        print("Action started for Sell stop loss")
        if float(str(currPrice))<float(str(closedVal)):    
            
            print("Tran 1")
            #Update Stop Loss with ID
            data ={"stopLoss": {"timeInForce": "GTC","price": str(closedVal)}}
            r=trades.TradeCRCDO(accountID=accountID, tradeID=TranID, data=data)
            rv = api.request(r)  
            print(json.dumps(rv, indent=4))
            query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '"+str(float(closedVal))+"',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
            print(query)
            cursor.execute(query)
            db.commit()
        elif (float(str(currPrice))+acceptLoss)>float(str(closedVal)):    
            print("Tran 2")
            #Update Stop Loss with ID
            data ={"stopLoss": {"timeInForce": "GTC","price": str(currPrice)}}
            r=trades.TradeCRCDO(accountID=accountID, tradeID=TranID, data=data)
            rv = api.request(r)  
            print(json.dumps(rv, indent=4))
            query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '"+str(float(closedVal))+"',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
            print(query)
            cursor.execute(query)
            db.commit()
        
        else:
            print("Stop Loss Not Required for Sell")
            query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '""',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
            print(query)
            cursor.execute(query)
            db.commit()
    else:
        print("------------------Order Not In Active----------------------")
        query = "UPDATE tbloandaprice SET EMA20 = '"+str(round(EMA20,5))+"',Buy = '"+flgbuy+"',Sell = '"+flgsell+"',Processed_Amt = '"+str(float(closedVal))+"',Stoploss_Amt = '""',orderID = '"+TranID+"' WHERE TimeStamp = '"+str(timestamp)+"'"
        print(query)
        cursor.execute(query)
        db.commit()
        
###################################################################################################
