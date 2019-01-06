# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:15:09 2018

@author: Asus
"""

def add_item(tup, idx, item):
  tup = list(tup)
  
  if idx == 0 or idx == len(tup) - 1:
    tup[idx] = item
    result = tuple(tup)
    
  else:
    result = tup[0: idx]
    result.append(item)
    
    for element in tup[idx:]:
      result.append(element)
      
    result = tuple(result)

  return result    
