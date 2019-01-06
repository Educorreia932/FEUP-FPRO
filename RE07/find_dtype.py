# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:52:10 2018

@author: Asus
"""

def find_dtype(atuple, data_type):
  result = ()
  
  for element in atuple:
    if data_type == type(element).__name__:
      result += (element,)    
  
  return result
