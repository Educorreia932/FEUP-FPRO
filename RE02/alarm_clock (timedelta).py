# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:47:38 2018

@author: Asus
"""

import datetime
now= datetime.datetime.now()
alarm_hour = now + datetime.timedelta(hours=8, minutes=30)

print("O alarme irá tocar às: " + alarm_hour.strftime("%H:%M"))    
