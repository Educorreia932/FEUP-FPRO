# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:13:43 2018

@author: Asus
"""

def override(l1, l2):
  result = []
  atomic_list = []
  
  for element in l2:
    atomic_list.append(element[0])    
  
  for element in l1:
    if element[0] not in atomic_list:
      result.append(element)
      
  for element in l2:
    result.append(element)   
    
  return sorted(result, key = lambda element: element[0])