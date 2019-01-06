# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:29:42 2018

@author: Asus
"""

def count_until(tup):
  counter = 0
  
  for element in tup:
    if "tuple" == type(element).__name__:
      result = counter
      return result
    
    counter += 1
    
  return -1
  
