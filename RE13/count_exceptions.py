# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:53:29 2019

@author: Asus
"""

def count_exceptions(f, n1, n2):
    result = 0
    
    for n in range(n1, n2 + 1):
        try:
            f(n)
            
        except Exception:
            result +=1
                        
    return result     