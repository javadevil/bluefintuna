#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:22:18 2018

@author: wt
"""

class Exchange():
    
    def __init__(self, name):
        self.name = name
        self.currencies = dict()
        self.tradepairs = dict()
        self.initCurrencies()
        self.initTradepairs()
        
    def __str__(self):
        return "Exchange: {0}".format(self.name)
    
    def getCurrency(self, symbol):
        return self.currencies.get(symbol)
    
    def getTradepair(self, symbol):
        return self.tradepairs.get(symbol)
    
    def initCurrencies(self):
        pass
    
    def initTradepairs(self):
        pass
    
    def updateCurrencies(self):
        pass
    
    def updateTradepairs(self):
        pass
    
class Currency():
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.fee = 0.0
        self.setValues()
        
    def setValues(self, balance=0.0, deposit=0.0, withdraw=0.0, ordering=0.0):
        self.balance    = balance
        self.deposit    = deposit
        self.withdraw   = withdraw
        self.ordering   = ordering
    
    def isNotZero(self):
        return self.balance + self.deposit + self.withdraw + self.ordering > 0.0
    
    def __str__(self):
        return "{0} : (B){1:5.8f}, (D){2:5.8f}, (W){3:5.8f}, (O){4:5.8f} :{5:5.8f}" \
        .format(self.symbol, self.balance, self.deposit, self.withdraw, self.ordering, self.fee)

class Tradepairs():
    
    def __init__(self, symbol):
        self.symbol = symbol
        self.fee = 0.0
        self.setValues()
    
    def setValues(self, asks=0.0, bids=0.0):
        self.asks = asks
        self.bids = bids
        
    def __str__(self):
        return "{0}: (A){1:5.8f} (B){2:5.8f}".format(self.symbol, self.asks, self.bids)