# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:09:50 2018

@author: Asus
"""

dirs_list =  ["home",
                ["Documents",
                   [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
                   [ "Python", "hello_world.py", "readme.md" ],
                ],
                ["Downloads",
                   [ "Movies",
                      [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
                      "1.avi", "22", "001.mp4"
                   ],
                ],
                "tmp.txt", "page.html"
             ]

def file_finder(dirs, file_name):
  if dirs == file_name:
    return file_name
  
  for subdirs in dirs[1:]:
    r = file_finder(subdirs, file_name)
    
    if r != None:
      return dirs[0] + "/" + r