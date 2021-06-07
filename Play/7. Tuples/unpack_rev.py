# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:37:08 2018

@author: Asus
"""

def unpack_rev(atuple):
  list = []
  
  for string in atuple:
    list = [string] + list
    
  result = " ".join(list)
  
  return result

print(unpack_rev(("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")))