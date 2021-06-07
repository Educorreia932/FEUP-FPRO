# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:25:04 2019

@author: Asus
"""

def summary(text):
    result = [0, 0]
    words = text.split()
    result[0] = len(words)
    
    for word in words:
        if "e" in word or "E" in word:
            
            result[1] += 1
            
    return tuple(result)      