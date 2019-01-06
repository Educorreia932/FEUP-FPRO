# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:11:51 2018

@author: Asus
"""

def local_minima(alist, n):
  counter = 0
  n_range = int(n / 2)
  enumerated_list = list(enumerate(alist))
  minimum_list = []
  occurrence_list = []
  conflict_list = []
  numbers_interval = []
  result = []
  
  for (index, element) in enumerated_list:
    if index < n_range:
      interval = enumerated_list[: index + n_range + 1]
      
      for (index, number) in interval:
        numbers_interval.append(number)

      minimum = min(numbers_interval)
      
      for (index, element) in interval:
        if element == minimum:
          minimum_list.append((element, index, counter))
          
    elif index >= n_range and index <= len(alist) - n_range - 1: 
      interval = enumerated_list[index - n_range: index + n_range + 1]
      
      for (index, number) in interval:
        numbers_interval.append(number)
        
      minimum = min(numbers_interval)
      
      for (index, element) in interval:
        if element == minimum:
          minimum_list.append((element, index, counter))
          
    else:
      interval = enumerated_list[len(alist) - n_range:]

      for (index, number) in interval:
        numbers_interval.append(number)

      minimum = min(numbers_interval)

      for (index, element) in interval:
        if element == minimum:
          minimum_list.append((element, index, counter))
    
    numbers_interval = []   
    counter += 1
    
  minimum_list = list(set(minimum_list))

  for triple_one in minimum_list:
    occurrence_list.append(triple_one[2])

  for triple_two in minimum_list:
    if occurrence_list.count(triple_two[2]) == 1:
      result.append((triple_two[0], triple_two[1]))
    else:
      conflict_list.append(triple_two)
  
  def sorting_rule(list):
    return list[1]
  
  result = sorted(list(set(result)), key = sorting_rule)
  
  new_counter = 0
  
  for pair in result:
    if new_counter < len(result) - 1:
      next = result[new_counter + 1]
      
      if pair[1] + 1 == next[1] and pair[0] == next[0]:
        result.remove(next)
      
    new_counter += 1 
  
  return result

print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))    