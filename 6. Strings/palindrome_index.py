# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:22:03 2018

@author: Asus
"""

def palindrome_index(s):
  if s[::-1] == s:
    return -1 
  
  for letter in s:
    letter_index = s.index(letter)
    
    palindrome = s[0: letter_index] + s[letter_index + 1:]
    
    print(palindrome)
  
    if palindrome[::-1] == palindrome:
      return letter_index
    
  return -1
  
