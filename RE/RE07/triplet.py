# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:10:06 2018

@author: Asus
"""

#Verificar "lowest index"

def triplet(atuple):
    result = ()
    while True:
      for element_1 in atuple:
        for element_2 in atuple:
          for element_3 in atuple: 
            index_1 = atuple.index(element_1)
            index_2 = atuple.index(element_2)
            index_3 = atuple.index(element_3)
            if element_1 + element_2 + element_3 == 0 and index_1 != index_2 != index_3:
              result = (element_1, element_2, element_3) 
              
              return result
            
      if result == ():
        return result
         
print(triplet((-8, 0, 4, -2, -1, 1, 2)))