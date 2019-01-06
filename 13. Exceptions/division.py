# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:06:49 2019

@author: Asus
"""

def division(a, b):
    try:
        a
        b
    
    except NameError:
        return "unsupported operand type(s) for division"
        return "unsupported operand type(s) for division"
    
    try:
        assert b != 0
        assert type(a) == int and type(b) == int
    
    except AssertionError:
        return "can't divide by 0!"
        return "unsupported operand type(s) for division"
       
    result = str(a) + "/" + str(b) + " = " + str(a / b)
    
    return result

print(division(10, b))