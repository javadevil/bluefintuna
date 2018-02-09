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
        pass
    
    def init_tradepairs(self):
        pass
    
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
        
class Currency():
    def __init__(self, symbol, name, withdraw_fee=0.0):
        self.symbol = symbol
        self.name = name
        self.withdraw_fee = withdraw_fee
        
    def update_balance(self):
        self.balance = 0.0
        self.deopsit_pending = 0.0
        self.withdraw_pending = 0.0
        self.trade_order = 0.0

    def __eq__(self, other):
        return self.symbol == other.symbol
    
    def __str__(self):
        return "{0} ({1})".format(self.symbol, self.name)
