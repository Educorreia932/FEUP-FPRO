# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:38:07 2019

@author: Asus
"""

def rec_exceptions(l):
    result = []
    
    for function in l:
        try:
            function()
            
        except Exception as ex:
            result.append(ex)
            
        else:
            result += rec_exceptions(function())
        
    return result
