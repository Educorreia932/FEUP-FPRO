import datetime

# Using modular arithmetic

now = datetime.datetime.now()

alarm_hour = (now.hour + 8) % 24
alarm_minute = (now.minute + 30) % 60

print("O alarme irá tocar às: " + str(alarm_hour).zfill(2) + ":" + str(alarm_minute).zfill(2))    

# Using timedelta

now = datetime.datetime.now()
alarm_hour = now + datetime.timedelta(hours=8, minutes=30)

print("O alarme irá tocar às: " + alarm_hour.strftime("%H:%M"))    
