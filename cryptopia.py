#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:59:47 2018

@author: wt
"""
import time
import hmac
import urllib
import requests
import hashlib
import base64
import json

from exchange import Exchange
from exchange import Currency

API_KEY = ""
API_SECRET = ""

class Cryptopia(Exchange):
    
    def __init__(self):
        super().__init__("Cryptopia")
    
    def initCurrencies(self):
        currencies_data = api_query("GetCurrencies")["Data"]
        for c in currencies_data:
            if c["Status"] == "OK":
                currency = Currency(c["Symbol"])
                currency.fee = c["WithdrawFee"]
                self.currencies[currency.symbol] = currency

    def updateCurrencies(self):
        currencies_data = api_query("GetBalance")["Data"]
        for c in currencies_data:
            if c["Status"] == "OK":
                currency = self.currencies[c["Symbol"]]
                currency.setValues(c["Available"], c["Unconfirmed"], c["PendingWithdraw"], c["HeldForTrades"])
def api_query( method, req = None ):
    if not req:
        req = {}
    #print "def api_query( method = " + method + ", req = " + str( req ) + " ):"
    time.sleep(1)
    public_set = set([ "GetCurrencies", "GetTradePairs", "GetMarkets", "GetMarket", "GetMarketHistory", "GetMarketOrders" ])
    private_set = set([ "GetBalance", "GetDepositAddress", "GetOpenOrders", "GetTradeHistory", "GetTransactions", "SubmitTrade", "CancelTrade", "SubmitTip" ])
    if method in public_set:
        url = "https://www.cryptopia.co.nz/api/" + method
        if req:
            for param in req:
                url += '/' + str(param)
        r = requests.get(url)
    elif method in private_set:
        url = "https://www.cryptopia.co.nz/Api/" + method
        nonce = str(int(time.time()))
        post_data = json.dumps(req);
        m = hashlib.md5()
        m.update(post_data.encode("UTF-8"))
        requestContentBase64String = base64.b64encode(m.digest()).decode("UTF-8")
        signature = API_KEY + "POST" + urllib.parse.quote_plus( url ).lower() + nonce + requestContentBase64String
        hmacsignature = base64.b64encode(hmac.new(base64.b64decode( API_SECRET ), signature.encode("UTF-8"), hashlib.sha256).digest())
        header_value = "amx " + API_KEY + ":" + hmacsignature.decode("UTF-8") + ":" + nonce
        headers = {"Authorization": header_value, "Content-Type":"application/json; charset=utf-8"}
        r = requests.post(url, data = post_data, headers = headers)
    response = r.text
    #print("( Response ): " + response)
    return json.loads(response)

c = Cryptopia()
c.updateCurrencies()
print(c)
for i in c.currencies.values():
    if i.isNotZero():
        print(i)