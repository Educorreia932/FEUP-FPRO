# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:41:14 2018

@author: Asus
"""

def anagrams(alist):
  word_list = []
  numbers_list = []
  result = []
  anagram = []
  word_result = ""
  
  for word in alist:
    word = sorted(word.split())
    word = "".join(word)
    word = word.lower()
    word = sorted(word)
    
    for u in word:
      word_result += u
      
    word_list.append(word_result)
    word_result = ""
    
  word_list = list(enumerate(word_list, 0))
  
  def sorting_rule(list):
    key = list[1]
    return key
  
  word_list.sort(key = sorting_rule, reverse = False)
  
  for pair in word_list:
    numbers_list.append(pair[0])
    
    if word_list.index(pair) != len(word_list) - 1 and pair[1] != word_list[word_list.index(pair) + 1][1] :
      numbers_list.append(".")
  print(numbers_list)
  for number in numbers_list:
    
    if number != ".":
      anagram.append(alist[number])
          
    else:
      anagram.sort()
      result.append(anagram)
      anagram = []
  
  if result != []:
    anagram.sort()
    result.append(anagram)
    
  if result == []:
    result = anagram
          
  return result