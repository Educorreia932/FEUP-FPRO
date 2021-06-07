# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:13:05 2018

@author: Asus
"""

def academy_awards(alist):
  result = {}
  
  for movie in alist:
    if movie[1] not in result:
      result[movie[1]] = 1
    
    else:
      result[movie[1]] += 1
      
  return result      