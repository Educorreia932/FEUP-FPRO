# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:53:08 2019

@author: Asus
"""

def grep(pattern, files_list, flags=''):
    result = ""
    
    for file in files_list:
        with open(file, "r") as this_file:            
            lines = this_file.readlines()
            
        lines_copy = lines.copy()
        index = 0
        
        if "-i" in flags:
            for line in lines:
                lines[index] = line.lower()
                index += 1
           
            pattern = pattern.lower()
         
        index = 0    
            
        if flags == "-i":
            for line in lines:
                if pattern in line[: -1]:
                    result +=  file + ":" + str(index + 1) + ":" + lines_copy[index]
      
                index += 1
   
        index = 0
           
        if "-x" in flags:   
            for line in lines:
                if pattern == line[: -1]:
                    result +=  file + ":" + str(index + 1) + ":" + lines_copy[index]
      
                index += 1
        
        index = 0
        
        if "-v" in flags:
            for line in lines:
                if pattern not in line:
                    result +=  file + ":" + str(index + 1) + ":" + lines_copy[index]
      
                index += 1
              
            result += "\n"   
                
        index = 0
        
        if "-l" in flags:
            for line in lines:
                if pattern in line:
                    result += file
                    break
        
            result += "\n" 
        
        
        if "-c" in flags:    
            count = 0
            
            for line in lines:
                if pattern in line:                        
                    count += 1   
                    
            result += file + ":" + str(count) + "\n"  
        
        if flags == "":
            for line in lines:
                if pattern in line:
                    result +=  file + ":" + str(lines.index(line) + 1) + ":" + line
          
    return result[:-1]
        
print(grep('Hello', ['file1g.txt', 'file2g.txt'], ''))