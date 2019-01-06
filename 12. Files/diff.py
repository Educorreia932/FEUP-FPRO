# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:44:40 2019

@author: Asus
"""
 
def diff(filename1, filename2):
    with open(filename1, "r") as file1:
        with open(filename2, "r") as file2:
            minus = ""
            plus = ""
            index = 0            
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            
            for line in lines2:
                if index > len(lines1) - 1:
                    plus += "+ " + lines2[index + 1]
                                        
                    return minus + plus
                
                else:               
                    if index != 0 and line == lines1[index] :
                        return (minus + plus)[:-1]
                    
                    elif line != lines1[index]:
                        this_line = lines1[index]
                        lines1.remove(lines1[index])
                        
                        if index > len(lines1) - 1:
                            minus += "- " + this_line + "\n"
                            plus += "+ " + lines2[index]
                            
                            return (minus + plus)[:-1]
                        
                        elif line == lines1[index]:
                            minus += "- " + this_line
                            
                            return (minus + plus)[:-1]
                        
                                                    
                        else:      
                            lines1.insert(index, line)
                            minus += "- " + this_line
                            plus += "+ "+ line
                    
                index += 1
        
print(diff("file1d.txt", "file2d.txt"))