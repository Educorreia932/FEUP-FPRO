# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:16:12 2019

@author: Asus
"""

def juggler(n, p):
    if p == 0:
        return n
    
    elif juggler(n, p - 1) % 2 == 0:
        return round((juggler(n, p - 1)) ** (1/2))
    
    else:
        return round((juggler(n, p - 1)) ** (3/2))       
    
print(juggler(9, 1))