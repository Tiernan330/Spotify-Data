from datetime import datetime, date

'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This file contains functions used in any of the other files in the parent folder to slim down on code
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

def convertMillis(millis):
    seconds=int((millis/1000)%60)
    minutes=int((millis/(1000*60))%60)
    hours=int((millis/(1000*60*60))%24)
    print(("%d:%02d:%02d" % (hours, minutes, seconds)))
    return ("%d:%02d:%02d" % (hours, minutes, seconds))

def currentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def currentDate():
    return date.today()