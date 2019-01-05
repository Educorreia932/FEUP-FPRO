# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:18:06 2018

@author: Asus
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)