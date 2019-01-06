# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:55:43 2018

@author: Asus
"""

def mult(M, N):
  if len(M[0]) != len(N):
    result = []
    
  else:
    result = []
    list = []
    inner = 0
    
    for row in range(len(M)):
      for column in range(len(N[0])):   
        for element in range(len(M[0])):
          inner += M[row][element] * N[element][column]
        list.append(inner)
        inner = 0
      result.append(list) 
      list = []
    
  return result  

print(mult([[-1, 0], [0,1]], [[-1, 0], [0,1]]))