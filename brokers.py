# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:49:37 2018

@author: Wacharabuhm
"""
import requests as req
from io import StringIO
from pair import Pair
import json

class Broker():
    def __init__(self,name):
        self.name = name
        self.balance = 0.0
        self.pairs = dict()
        self.withdraws = dict()
    def __str__(self):
        return "Broker:{0} balance:{1:5.8f} BTC".format(self.name, self.balance)
    
    def __loadJSON__(self, url):
        io = StringIO(req.get(url).content.decode("UTF-8"))
        return json.load(io)

class Bx(Broker):
    def __init__(self):
        super().__init__("BX.in.th")
    
    def update(self):
        pairs = self.__loadJSON__("https://bx.in.th/api/")
        #Bx.in.th fixed trade fee
        fee = 0.0025
        for i in pairs:
            #Filter for BTC Pairs only
            if pairs[i]["primary_currency"] == "BTC":
                symbol = "{0}:{1}".format(pairs[i]["secondary_currency"],pairs[i]["primary_currency"])
                asks = pairs[i]["orderbook"]["asks"]["highbid"]
                bids = pairs[i]["orderbook"]["bids"]["highbid"]
    
                if symbol in self.pairs:
                    self.pairs.get(symbol).update(asks, bids)
                else :
                    self.pairs[symbol] = Pair(symbol, asks, bids, fee)
        
        for i in self.pairs.items():
            print(i[1])
        
Bx().update()