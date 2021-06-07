# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:28:12 2019

@author: Asus
"""

def mail_merge(names, mail_template):
    with open(names, "r") as names:
        with open(mail_template, "r") as template:
            names_lines = names.readlines()
            template_lines= template.readlines()
            result = []
    
        for name in names_lines:
            text = ""
            
            for line in template_lines:
                if "<name>" in line:
                    text += line.replace("<name>", name[:-1]) 
            
                else:
                    text+= line
                    
            result.append(text)
            
        return result    
    
print(mail_merge("names.txt", "template.txt"))