# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:53:08 2019

@author: Asus
"""

def grep(pattern, files_list, flags=''):
    with open(files_list[0], "r") as file1:
        with open(files_list[1], "r") as file2:
            result = ""
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            lines1_copy = lines1.copy()
            lines2_copy = lines2.copy()
            index1 = 0
            index2 = 0
            
            if "-i" in flags:
                for line in lines1:
                    lines1[lines1.index(line)] = line.lower()
                    
                for line in lines2:
                    lines2[lines2.index(line)] = line.lower()   
               
                pattern = pattern.lower()
                
            if flags == "-i":
                for line in lines1:
                    if pattern in line[: -1]:
                        result +=  files_list[0] + ":" + str(index1 + 1) + ":" + lines1_copy[index1]
          
                    index1 += 1
            
                for line in lines2:
                    if pattern in line[: -1]:
                        result +=  files_list[1] + ":" + str(index2 + 1) + ":" + lines2_copy[index2]
            
                    index2 += 1
            
            index1 = 0
            index2 = 0
                
            if "-x" in flags:   
                for line in lines1:
                    if pattern == line[: -1]:
                        result +=  files_list[0] + ":" + str(index1 + 1) + ":" + lines1_copy[index1]
          
                    index1 += 1
            
                for line in lines2:
                    if pattern == line[: -1]:
                        result +=  files_list[1] + ":" + str(index2 + 1) + ":" + lines2_copy[index2]
            
                    index2 += 1
            
            index1 = 0
            index2 = 0
            
            if "-v" in flags:
                for line in lines1:
                    if pattern not in line:
                        result +=  files_list[0] + ":" + str(index1 + 1) + ":" + lines1_copy[index1]
          
                    index1 += 1
                  
                result += "\n"   
                    
                for line in lines2:
                    if pattern not in line:
                        result +=  files_list[1] + ":" + str(index2 + 1) + ":" + lines2_copy[index2]
            
                    index2 += 1
            
                result += "\n"   
                
            index1 = 0
            index2 = 0
            
            if "-l" in flags:
                for line in lines1:
                    if pattern in line:
                        result +=  files_list[0]
                        break
            
                result += "\n" 
            
                for line in lines2:
                    if pattern in line:
                        result +=  files_list[1]
                        break
                         
                result += "\n" 
            
            if "-c" in flags:    
                count1 = 0
                count2 = 0
                
                for line in lines1:
                    if pattern in line:                        
                        count1 += 1   
            
                for line in lines2:
                    if pattern in line:
                        count2 += 1
                        
                result += files_list[0] + ":" + str(count1) + "\n" + files_list[1] + ":" + str(count2) + "\n"      
            
            if flags == "":
                for line in lines1:
                    if pattern in line:
                        result +=  files_list[0] + ":" + str(lines1.index(line) + 1) + ":" + line
          
                for line in lines2:
                    if pattern in line:
                        result +=  files_list[1] + ":" + str(lines2.index(line) + 1) + ":" + line
            
            return result[:-1]
        
print(grep('Hello', ['file1g.txt', 'file2g.txt'], ''))