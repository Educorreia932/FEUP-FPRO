# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:25:15 2018

@author: Asus
"""

def fib(n):
    result = []
    
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
        
    for number in range(n):
        result.append(fibonacci(number))
    
    return result