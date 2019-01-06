# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:42:39 2018

@author: Asus
"""

def sort_grades(records): 
  def sort_rule1(item):
    mean = -float(sum(item[2]))/max(len(item[2]),1) 
    return(mean, item[0], item[1])
      
  result = tuple(sorted(records, key = sort_rule1, reverse = False))
  
  return result
