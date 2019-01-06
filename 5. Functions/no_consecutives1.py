# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:03:08 2018

@author: Asus
"""

def no_consecutives1(k):
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
        
    return fib(k + 2)