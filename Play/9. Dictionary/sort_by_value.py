# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:34:05 2019

@author: Asus
"""

def sort_by_value(dict):
    result = []
    
    def sorting(color):
        value = int(color[1][1:], 16)
        
        return value
    
    for color in dict:
        result.append([color, dict[color]])
        
    return sorted(result, key = sorting)    