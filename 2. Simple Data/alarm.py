# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 09:55:57 2018

@author: Asus
"""

def alarm(hour, minutes):
  hour = (hour + 6) % 24  
  minutes = (minutes + 51) 
  
  if minutes > 60:
    hour += 1
    minutes = minutes % 60
  
  return str(hour).zfill(2) + ":" + str(minutes).zfill(2)