# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:34:05 2019

@author: Asus
"""

def sort_by_key(dict):
    result = []
    
    def sorting(color):
        key = color[0]
        
        return key
    
    for color in dict:
        result.append((color, dict[color]))
        
    return sorted(result, key = sorting) 