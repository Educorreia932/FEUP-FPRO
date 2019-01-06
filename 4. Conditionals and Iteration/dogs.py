# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:20:28 2018

@author: Asus
"""

def dogs(h_age):
  result = 0
  
  while h_age > 2:
    result += 4
    h_age += -1
    
  while h_age <= 2 and h_age > 0:
    result += 10.5
    h_age += -1
    
  return result