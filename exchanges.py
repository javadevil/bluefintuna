# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:41:39 2018

@author: Wacharabuhm
"""

class Exchange():
    def __init__(self):
        self.init_currency()
        self.init_tradepairs()

    def init_currency(self):
        self.currencies = dict()
    
    def init_tradepairs(self):
        self.tradepairs = dict()
    
    def update(self):
        self.update_currency()
        self.update_tradepairs()
        
    def update_currency(self):
        pass
    
    def update_tradepairs(self):
        pass
    
class TradePair():
    def __init__(self, secondary_currency, primary_currency, trade_fee=0.0):
        self.secondary_currency = secondary_currency
        self.primary_currency = primary_currency
        self.trade_fee = trade_fee
        self.bids = 0.0
        self.asks = 0.0
    
    def __str__(self):
        return "{0}/{1}\t Bids:{2:5.8f} Asks:{3:5.8f} TF:{4:5.8f}".format(self.secondary_currency.symbol, self.primary_currency.symbol, self.bids, self.asks, self.trade_fee)
    
class Currency():
    def __init__(self, symbol, name, address=None, withdraw_fee=0.0):
        self.symbol = symbol
        self.name = name
        self.address = address
        self.withdraw_fee = withdraw_fee
        self.balance = 0.0
        self.deopsit_pending = 0.0
        self.withdraw_pending = 0.0
        self.trade_held = 0.0

    def total(self):
        return self.balance + self.deopsit_pending + self.withdraw_pending + self.trade_held
    def __eq__(self, other):
        return self.symbol == other.symbol
    
    def __str__(self):
        return "{0}\t Bal:{1:5.8f} DP:{2:5.8F} WP:{3:5.8f} TH:{4:5.8f} WF:{5:5.8f}".format(self.symbol, self.balance, self.deopsit_pending, self.withdraw_pending, self.trade_held, self.withdraw_fee)
