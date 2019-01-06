# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:57:48 2018

@author: Asus
"""

def palindrome(astring):
  counter = 0
  add = 2
  palindrome_counter = 0
  number_counter = 1  
  
  while True:    
    combinations = len(astring) - number_counter
    
    for n in range(combinations):
      palindrome = astring[counter: counter + add]
      counter += 1
               
      if palindrome == palindrome[:: -1] and len(palindrome) != 1:
        palindrome_counter += 1      
          
      if n == combinations - 1:
         counter = 0
         add += 1
         number_counter += 1
      
    if combinations == 1:
      break
          
  result = "For string '{}': {} palindrome substrings".format(astring, palindrome_counter)
  
  return result