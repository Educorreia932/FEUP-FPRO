# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:58:43 2018

@author: Asus
"""

def roman_to_integer(astring):
  counter = 0
  result = 0
  mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}  
    
  while True:
    if counter == len(astring) - 1:
      result += mapping.get(astring[counter])
      break
    
    if counter > len(astring) - 1:
      break
      
    if mapping.get(astring[counter + 1]) > mapping.get(astring[counter]):
      result += mapping.get(astring[counter + 1]) - mapping.get(astring[counter])
      counter += 1
      
    else: 
      result += mapping.get(astring[counter])
    
    counter +=1
       
  return result   