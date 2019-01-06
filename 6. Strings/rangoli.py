# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:42:44 2018

@author: Asus
"""

def rangoli(N):
  alphabet= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  lines = []
  result = ""
  fill = 2 * N - 2
  
  for n in range(N):
      line = []
      n_range = n * 2 + 1
      letter = N - 1
      
      for i in range(n_range):
          line.append(alphabet[letter]) 
          
          if i >= n:
              letter = letter + 1
              
          else:
              letter = letter - 1         
            
      lines.append(line)
      
  for line in lines:
      lines[lines.index(line)] = "-" * fill + "-".join(line) + "-" * fill
      fill += -2  
  
  remaining = lines.copy()[:-1][::-1]
  compound = lines + remaining
  
  for element in compound:
      result += element + "\n"
  
  return result

print(rangoli(15))
    
