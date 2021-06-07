# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:52:02 2018

@author: Asus
"""

def remove_leading(ip):
  ip = ip.split(".")
  result = []
  
  for number in ip:
    if int(number[0]) == 0:
      
      while int(number[0]) == 0 and len(number) > 1:
        number = number[1:]
       
      result.append(number)
      
    else:
      result.append(number)
      
  result = ".".join(result)

  return result
