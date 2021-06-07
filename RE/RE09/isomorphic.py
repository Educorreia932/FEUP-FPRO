# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:33:54 2018

@author: Asus
"""

def isomorphic(astring1, astring2):
  counter = 0
  result = []
  dictionary = {}
  different1 = []
  different2 = []
  
  for char1 in astring1:
    if char1 not in different1:
      different1.append(char1)
      
  for char2 in astring2:
    if char2 not in different2:
      different2.append(char2)
      
  if len(different1) != len(different2):
    return "'" + astring1 + "'" + " and " + "'" + astring2 + "'"  + " are not isomorphic"
  
  for char in astring1:
    dictionary[char] = astring2[counter]
    counter += 1
  
  for element in dictionary:
    result.append((element, dictionary[element])) 
    
  return "'" + astring1 + "'" + " and " + "'" + astring2 + "'" + " are isomorphic because we can map: " + str(result)