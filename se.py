#python

import os

i=0
while True:
    if i==4:
        os.system("curl -X POST  https://rest.nexmo.com/sms/json \-d api_key=f88e06bd \-d api_secret=a2ef00734f879756 \-d to=886978711793 \-d from=\"NEXMO\" \-d text=\"Hels我好lo from Nexmo\"")
    else:
        print("ss")
    i=i+1