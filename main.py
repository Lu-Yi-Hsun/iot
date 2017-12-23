#python

# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
from time import sleep
from gpiozero import  InputDevice
import os

no_rain = InputDevice(18)
 


count_time=0

rain_count=0
#control code 0:no rain 1:alittle 2:

prv_rain_level=0

while True:

    if count_time<60:
        if not no_rain.is_active:
            print("It's raining - get the washing in!")
            rain_count=rain_count+1
        sleep(1)
    else:
        count_time=0
        
        if rain_count==0:
            now_rain_level=0
        elif rain_count>0 and rain_count<=30:
            now_rain_level=1
        elif rain_count>30 and rain_count<=60:
            now_rain_level=2
        elif rain_count>60:
            now_rain_level=3




        if now_rain_level != prv_rain_level:
            print("message")
            if now_rain_level==0:
                os.system("curl -X POST  https://rest.nexmo.com/sms/json \-d api_key=f88e06bd \-d api_secret=a2ef00734f879756 \-d to=886978711793 \-d from=\"NEXMO\" \-d text=\"目前沒有下雨\"")
            elif now_rain_level==1: 
                os.system("curl -X POST  https://rest.nexmo.com/sms/json \-d api_key=f88e06bd \-d api_secret=a2ef00734f879756 \-d to=886978711793 \-d from=\"NEXMO\" \-d text=\"目前下小雨\"")

            elif now_rain_level==2:
                os.system("curl -X POST  https://rest.nexmo.com/sms/json \-d api_key=f88e06bd \-d api_secret=a2ef00734f879756 \-d to=886978711793 \-d from=\"NEXMO\" \-d text=\"目前下雨中等 需要帶雨具\"")
            
            elif now_rain_level==3:       
                os.system("curl -X POST  https://rest.nexmo.com/sms/json \-d api_key=f88e06bd \-d api_secret=a2ef00734f879756 \-d to=886978711793 \-d from=\"NEXMO\" \-d text=\"目前下雨很大 可以等待與停在出門\"")
            else:
                os.system("curl -X POST  https://rest.nexmo.com/sms/json \-d api_key=f88e06bd \-d api_secret=a2ef00734f879756 \-d to=886978711793 \-d from=\"NEXMO\" \-d text=\"程式錯誤請聯絡工程師\"")
            prv_rain_level != now_rain_level
        else:
            pass   
        
        
        
        

