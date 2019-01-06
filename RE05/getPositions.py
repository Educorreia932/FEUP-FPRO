# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:49:32 2018

@author: Asus
"""

def get_positions(word_list, sentence):
  result = ""
  if word_list[0] + " " + word_list[1] == sentence:
    result = "0 1"
  elif word_list[0] + " " + word_list[2] == sentence:
    result = "0 2"
  elif word_list[1] + " " + word_list[0] == sentence:
    result = "1 0"
  elif word_list[1] + " " + word_list[2] == sentence:
    result = "1 2"
  elif word_list[2] + " " + word_list[0] == sentence:
    result = "2 0"  
  elif word_list[2] + " " + word_list[1] == sentence:
    result = "2 1"  
  return result

print(get_positions(["hello", "brave", "hello"], "hello hello"))
