# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:58:07 2018

@author: Asus
"""

n = input("Pick a number: 6")
first= str(n)
second= first + first
third= first + second
result= int(first) + int(second) + int(third)
print(first + " + " + second + " + " + third + " = " + str(result))