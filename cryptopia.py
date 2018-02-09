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

API_KEY = ""
API_SECRET = ""

class Cryptopia(Exchange):
    def init_currency(self):
        api_query("GetBalance")  

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
    print("( Response ): " + response)
    return json.loads(response)
    

        
c = Cryptopia()