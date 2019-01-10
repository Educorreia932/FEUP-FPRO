# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:41:03 2018

@author: Asus
"""

n = int(input("Insert a number: "))

divisors = 0

for i in range(1, n+1):
  if n % i == 0:
    divisors = divisors + i
    
print(divisors)