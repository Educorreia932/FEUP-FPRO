# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:43:19 2018

@author: Asus
"""

def sparse_dot_product(dict1, dict2):
  result= 0
  
  for coord in dict1:
    if coord in dict2:
      result += dict1.get(coord) * dict2.get(coord)
      
  return result