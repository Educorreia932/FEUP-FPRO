# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 14:47:03 2019

@author: Asus
"""

def diff(filename1, filename2):
    with open(filename1, "r") as file1:
        with open(filename2, "r") as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            result = ""
            
            for line in lines1:
                if line not in lines2:
                    result += "- " + line 
            
            for line in lines2:
                if line not in lines1:
                    result += "+ " + line
                     
            return result[:-1]
        
print(diff("file1d.txt", "file2d.txt"))