# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:37:41 2018

@author: Asus
"""

def summary_ranges(astring): 
  index = 0
  begin = 0
  order= []
  result = []
  astring = astring.split(",")
 
  for number in astring:
      if index + 1 <= len(astring) - 1 and int(number) != int(astring[index + 1]) - 1 or index == len(astring) - 1:
          order.append((astring[begin], astring[index]))   
          begin = index + 1
          
      index += 1  
  
  for pair in order:
      if pair[0] == pair[1]:
          result.append(pair[0])
      else:
        result.append(pair[0] + "->" + pair[1])
        
  result = ",".join(result)
    
  return result