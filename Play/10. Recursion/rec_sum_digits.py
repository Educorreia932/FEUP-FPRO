# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:31:04 2018

@author: Asus
"""

def rec_sum_digits(n):
  n = str(n)
  result = 0
  
  for number in n:
    result += int(number)
    
  return result