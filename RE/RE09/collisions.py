# -*- coding: utf-8 -*-+
"""
Created on Tue Nov 27 19:01:26 2018

@author: Asus
"""

def collisions(alist):  
  result = {}
  
  def element_hash(element):
    final_element = []
    element = str(element)
    
    for char in element:
      final_element.append(int(char))
      
    element_sum = sum(final_element)
    
    return (element_sum % 8)
  
  for number in alist:
    if element_hash(number) not in result:
      result[element_hash(number)] = 1
      
    else:
      result[element_hash(number)] += 1
  
  return result