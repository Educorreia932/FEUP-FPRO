# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:38:43 2018

@author: Asus
"""

def count_elems(tup):
  result = []
  types = ["tuple", "list", "str"]
  
  for element in tup:
    if type(element).__name__ in types:
      result.append(len(element))        
    
    else:
      result.append(1)

  return tuple(result)
