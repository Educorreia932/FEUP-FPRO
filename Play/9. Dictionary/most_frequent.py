# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:33:39 2018

@author: Asus
"""

def most_frequent(alist):
    result = {}
    maximum_list = []
    
    for element in alist:
        if element not in result:
            result[element] = 1
        else:
            result[element] += 1
    
    maximum = max(result.values())
    
    for key in result:
        if result[key] == maximum:
            maximum_list.append(key)
    
    return max(maximum_list)