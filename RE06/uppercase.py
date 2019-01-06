# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:51:41 2018

@author: Asus
"""

def uppercase(astring):
  
  for n in range(3):
    if astring[n].upper() == astring[n] and astring[n].isalpha():
      result = astring.upper()
      return result
        
  return astring

  