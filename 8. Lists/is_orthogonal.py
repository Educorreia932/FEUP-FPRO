# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:48:36 2019

@author: Asus
"""

def is_orthogonal(mx):
    transpose = list(zip(*mx))
    identity = []
    index = 0
    
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
  
    for n in range(len(mx)):
        element = []
        cursor = 0
        
        for n in range(len(mx)):
            if cursor == index:
                element.append(1)
                
            else:   
                element.append(0)
                
            cursor += 1
            
        identity.append(element)
        index += 1
  
    if mult(mx, transpose) == identity:
        return True
    
    else:   
        return False