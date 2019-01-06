# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:59:03 2018

@author: Asus
"""

def adigits(n1, n2, n3):
  result = ""
  if int(n1) >= int(n2) and int(n1) >= int(n3):
      result = n1
      if n2 >= n3:
        result = result + n2 + n3
      else: 
        result = result + n3 + n2
  elif int(n2) >= int(n1) and int(n2) >= int(n3):
      result = n2
      if n1 >= n3:
        result = result + n1 + n3
      else: 
        result = result + n3 + n1 
  elif int(n3) >= int(n1) and int(n3) >= int(n2):
      result = n3
      if n1 >= n2:
        result = result + n1 + n2
      else: 
        result = result + n2 + n1
  return int(result)   

print(adigits("3", "2", "1"))
