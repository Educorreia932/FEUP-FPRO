# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:42:39 2018

@author: Asus
"""

def solver(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0 or a == 0:
      result = []
      
    elif discriminant == 0:
      solution = -b / (2 * a)
      result = [solution]
      
    else:
      solution_1 = (-b - (discriminant ** (1/2))) / (2 ** a)

      solution_2 = (-b + (discriminant ** (1/2))) / (2 ** a)
      result = [solution_1, solution_2]
      result = sorted(result)
    
    return result      
#      if solution_1 > solution_2:
#        result = [solution_2, solution_1]
#        return result
#      elif solution_2 > solution_1:
#        result = [solution_1, solution_2]
#        return result