# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:13:04 2018

@author: Asus
"""

def translate(astring, table):  
  result = ""
  n = 0
  
  for character in astring:
    for element in table:
      if character == element[0]:
        result += str(element[1])
        n = 1
        break    
    
    if n == 0:  
      result += str(character)
      
    n = 0  
    
  return result 