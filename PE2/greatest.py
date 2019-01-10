#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:15:30 2018

@author: exame
"""

def greatest(num):
    result = ""
    list = []
    for digit in str(num):
        list.append(digit)
        
    list = sorted(list, reverse = True)
    
    for number in list:
        result += str(number)
    
    return int(result)