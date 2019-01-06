# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:38:14 2018

@author: Asus
"""

def budgeting(budget, products, wishlist):
  def costing(dictionary):
    cost = 0 
    
    for product in dictionary:
      cost += products.get(product) * wishlist.get(product)
      
    return cost
  
  while costing(wishlist) > budget:  
    minimum = min(products, key = products.get)
    
    if minimum in wishlist:      
      if wishlist[minimum] == 0:
        del wishlist[minimum]        
        
      else:
        wishlist[minimum] += -1 
    
    else:
      del products[minimum]
      
  wishlist = {x:y for x,y in wishlist.items() if y!=0}
   
  return wishlist