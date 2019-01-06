# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:39:09 2018

@author: Asus
"""

def pascal(n):
  result = ""
  
  def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
  
  def combinations(r, n):
    combination = int(factorial(n) / (factorial(n - r) * factorial(r)))
    return combination

  for line in range(n):
    for r in range(line + 1):
      result += str(combinations(r, line)) + " "
    result += "\n"    
   
  return result 

  

    
      