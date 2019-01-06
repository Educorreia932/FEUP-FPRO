# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:38:14 2018

@author: Asus
"""

def budgeting2(budget, products, wishlist):
  powerset_wishlist = []
  cost_list = []
  result = {}
  
  def costing(alist):
    cost = 0 
    
    for product in alist:
      cost += products.get(product)
      
    return cost
  
  for element in wishlist:
    for n in range(wishlist[element]):
      powerset_wishlist.append(element)
      
  def powerset(A):
    if A == []:
        return [[]]
      
    a = A[0]
    incomplete_pset = powerset(A[1:])
    rest = []
    
    for set in incomplete_pset:
        rest.append([a] + set)
        
    return rest + incomplete_pset   
  
  powerset_wishlist = powerset(powerset_wishlist)
  
  for set in powerset_wishlist:
    cost_list.append(costing(set))
  
  for cost in cost_list:
    if cost > budget:
      cost_list[cost_list.index(cost)] = 0
      
  print(budget)
  print(cost_list)
  
  index = cost_list.index(max(cost_list))
  powerset_wishlist = powerset_wishlist[index]
 
  for element in powerset_wishlist:
    if element not in result:
      result[element] = 1
      
    else:
      result[element] += 1
  
  return result  
      
print(budgeting2(1000, {'laptop': 2000, 'jeans': 50}, {'laptop': 2,'jeans': 3}))