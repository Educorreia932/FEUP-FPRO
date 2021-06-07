# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:33:11 2018

@author: Asus
"""

def fetch_middle(lists):
  result = []
  
  for element in lists:
    if len(element) % 2 != 0:
      result.append(element[len(element) // 2])
      
    else:
      result.append((element[len(element) // 2 - 1] + element[len(element) // 2]) / 2)
  
  return result