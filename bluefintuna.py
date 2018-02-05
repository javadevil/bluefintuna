# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:51:39 2018

@author: Wacharabuhm
"""

import brokers

t = brokers.Bx()
t.balance = 10.0

print(t.__loadJSON__("https://bx.in.th/api/"))