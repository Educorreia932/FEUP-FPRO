# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 17:40:42 2018

@author: Asus
"""

def rec_gcd(n1, n2):
    n1_divisors = []
    n2_divisors = []
    
    for i1 in range(1, n1 + 1):
        if n1 % i1 == 0:
            n1_divisors.append(i1)
        
    for i2 in range(1, n2 + 1):
        if n2 % i2 == 0:
            n2_divisors.append(i2)
            
    result = list(filter(lambda a: a in n1_divisors and a in n2_divisors, n1_divisors))
    result = max(result)
    
    return result