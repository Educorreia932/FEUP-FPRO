# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:43:58 2019

@author: Asus
"""

def pattern_hunting(l1, l2, p):
    result = []
    index = 0
    
    for element in l1:
        if p in element:
            result.append(l2[index])
            
        index += 1
        
    index = 0
    
    for element in l2:
        if p in element:
            result.append(l1[index])
            
        index += 1
        
    result = sorted(result, reverse = True)
    
    return result