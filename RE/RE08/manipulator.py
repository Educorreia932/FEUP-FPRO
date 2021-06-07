# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:56:20 2018

@author: Asus
"""

def manipulator(l, cmds):
  result = ""
  
  for command in cmds:
    command = command.split()
    
    if len(command) == 2:
      i = int(command[1])
      
    elif len(command) == 3:
      i = int(command[1])
      e = int(command[2])
    
    if command[0] == "insert":
      l.insert(i, e)
      
    elif command[0] == "print":
      result += str(l) + " "
      
    elif command[0] == "remove":
      l.remove(i)
      
    elif command[0] == "append":
      l.append(i)
      
    elif command[0] == "sort":
      l.sort()
      
    elif command[0] == "pop":
      l.remove(l[-1])
    
    elif command[0] == "reverse":  
      l = l[::-1]
    
  return result