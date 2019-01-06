# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:47:38 2018

@author: Asus
"""

import datetime

now= datetime.datetime.now()

alarm_hour = (now.hour + 8) % 24
alarm_minute = (now.minute + 30) % 60

print("O alarme irá tocar às: " + str(alarm_hour).zfill(2) + ":" + str(alarm_minute).zfill(2))    
