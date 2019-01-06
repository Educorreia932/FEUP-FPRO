# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:17:48 2018

@author: Asus
"""

def collatz(n):
  result = str(n)
  
  while True:
    if n == 1:
      return result
      break
    
    elif n % 2 == 0:
      n = int(n / 2)
      result += "," + str(n)
           
    elif n % 2 != 0:
      n = int(n * 3 + 1)
      result += "," + str(n)     

 

                 
    

      