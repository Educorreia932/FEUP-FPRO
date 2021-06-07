# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:00:08 2019

@author: Asus
"""

def reciprocals(alist):
    result = []
    
    for element in alist:
        if type(element) == int and element != 0:
            result.append(1 / element)
            
    return result