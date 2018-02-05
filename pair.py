# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:28:09 2018

@author: Wacharabuhm
"""

class Pair():
    def __init__(self, symbol, asks=0.0, bids=0.0, fee=0.0):
        self.symbol = symbol
        self.fee = fee
        self.update(asks, bids)
        
    def update(self, asks, bids):
        self.asks = asks
        self.bids = bids
        
    def __str__(self):
        return "{0}, bids:{2:5.8f} asks:{1:5.8f} fee:{3:5.8f}".format(self.symbol, self.asks, self.bids, self.fee)