# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:54:58 2018

@author: Wacharabuhm
"""
import time
import hmac
import urllib
import requests
import hashlib
import base64
import json

from exchanges import Exchange
from exchanges import TradePair
from exchanges import Currency

API_KEY = ""
API_SECRET = ""

class Cryptopia(Exchange):
    def init_currency(self):
        super().init_currency()
        currencies_data = api_query("GetCurrencies")["Data"]
        for c in currencies_data:
            self.currencies[c["Symbol"]] = Currency(c["Symbol"], c["Name"], withdraw_fee=c["WithdrawFee"])
    
    def init_tradepairs(self):
        super().init_tradepairs()
        tradepairs_data = api_query("GetTradePairs")["Data"]
        for p in tradepairs_data:
            if self.currencies.get(p["Symbol"]) and self.currencies.get(p["BaseSymbol"]):
                self.tradepairs[p["Label"]] = TradePair(self.currencies.get(p["Symbol"]), self.currencies.get(p["BaseSymbol"]), p["TradeFee"])
    
    def update_currency(self):
        balances_data = api_query("GetBalance")["Data"]
        for b in balances_data:
            balance = self.currencies.get(b["Symbol"])
            balance.balance = b["Available"]
            balance.deposit_pending = b["Unconfirmed"]
            balance.withdraw_pending = b["PendingWithdraw"]
            balance.trade_held = b["HeldForTrades"]
    
    def update_tradepairs(self):
        markets_data = api_query("GetMarkets")["Data"]
        for m in markets_data:
            tradepair = self.tradepairs.get(m["Label"])
            if not tradepair == None:
                tradepair.bids = m["BidPrice"]
                tradepair.asks = m["AskPrice"]
        print(self.tradepairs["NMC/BTC"])
        
def api_query( method, req = None ):
    if not req:
        req = {}
    #print "def api_query( method = " + method + ", req = " + str( req ) + " ):"
    time.sleep( 1 )
    public_set = set([ "GetCurrencies", "GetTradePairs", "GetMarkets", "GetMarket", "GetMarketHistory", "GetMarketOrders" ])
    private_set = set([ "GetBalance", "GetDepositAddress", "GetOpenOrders", "GetTradeHistory", "GetTransactions", "SubmitTrade", "CancelTrade", "SubmitTip" ])
    if method in public_set:
        url = "https://www.cryptopia.co.nz/api/" + method
        if req:
            for param in req:
                url += '/' + str( param )
        r = requests.get( url )
    elif method in private_set:
        url = "https://www.cryptopia.co.nz/Api/" + method
        nonce = str( int( time.time() ) )
        post_data = json.dumps( req );
        m = hashlib.md5()
        m.update(post_data.encode("UTF-8"))
        requestContentBase64String = base64.b64encode(m.digest()).decode("UTF-8")
        signature = API_KEY + "POST" + urllib.parse.quote_plus( url ).lower() + nonce + requestContentBase64String
        hmacsignature = base64.b64encode(hmac.new(base64.b64decode( API_SECRET ), signature.encode("UTF-8"), hashlib.sha256).digest())
        header_value = "amx " + API_KEY + ":" + hmacsignature.decode("UTF-8") + ":" + nonce
        headers = { 'Authorization': header_value, 'Content-Type':'application/json; charset=utf-8' }
        r = requests.post( url, data = post_data, headers = headers )
    response = r.text
    #print("( Response ): " + response)
    return json.loads(response)
    

        
c = Cryptopia()
c.update()
while True:
    time.sleep(15)
    c.update_tradepairs()