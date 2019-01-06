# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:52:05 2018

@author: Asus
"""

def is_perfect(n):
  result = 0
  if n == 1: 
    return True
  else:
    for i in range(1, n+1):
      if n % i == 0:
        result = result + i
    if result == n :
      return True
    else:
      return False
  
print(is_perfect(0))
      
