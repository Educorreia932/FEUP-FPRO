# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 14:23:52 2019

@author: Asus
"""

def interleave(f1, f2):
    with open(f1, "r") as file1:
        with open(f2, "r") as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            result = ""
            index = 0
            
            if len(lines1) >= len(lines2):        
                for line in lines1:
                    if index <= len(lines2) - 1:
                        result += line + lines2[index]
                        
                    index += 1
             
            else:
                for line in lines2:
                    if index <= len(lines1) - 1:
                        result+= lines1[index] + line 
                    
                    index +=1
                    
            return result          