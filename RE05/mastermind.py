# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:25:38 2018

@author: Asus
"""
  
def mastermind(g1, g2, g3, c1, c2, c3):
  result = 0
  if g1 == c1:
    result += 3
  elif g1 == c2 or g1 == c3:
    result += 1
  if g2 == c2:
    result += 3
  elif g2 == c1 or g2 == c3:
    result += 1 
  if g3 == c3:
    result += 3
  elif g3 == c1 or g3 == c2:
    result += 1
  return result

print(mastermind('b', 'b', 'y', 'b', 'y', 'b'))

