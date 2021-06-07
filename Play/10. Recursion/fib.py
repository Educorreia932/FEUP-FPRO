# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:13:33 2018

@author: Asus
"""

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)