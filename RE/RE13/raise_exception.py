# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:04:51 2019

@author: Asus
"""

def raise_exception(alist, value):
    result = []
    
    for number in alist:
        if number <= value:
            result.append(ValueError(str(number) + " is not greater than " + str(value)))
            
    return result