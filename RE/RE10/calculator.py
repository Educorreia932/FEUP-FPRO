# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:46:12 2018

@author: Asus
"""

def calculator(expr):
  if type(expr).__name__ == "int":
    return expr

  elif expr[1] == "+":
    result = calculator(expr[0]) + calculator(expr[2])
    
  elif expr[1] == "*":
    result = calculator(expr[0]) * calculator(expr[2])
    
  elif expr[1] == "-":
    result = calculator(expr[0]) - calculator(expr[2])
    
  return result