# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:46:50 2018

@author: Asus
"""

def sum_numbers(n):
  result = 0
  for i in range(n+1):
    result += i
  return result

print(sum_numbers(3))

