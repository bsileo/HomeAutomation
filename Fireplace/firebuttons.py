#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

MATRIX = [ ['3','4','1','2']
         ]

ROW = [5,6,13,19]
COL = [26]

#client id and client secret
uri = 'https://graph.api.smartthings.com/api/smartapps/installations/187b091d-eb18-483a-aae4-4a9beb30bed2'
access_token='d7d70e8a-c8a7-42c3-991e-1bbb6524a3d3'


for j in range(1):
    print("Set out on %s ",COL[j])    
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4) :
    print("Set IN on %s",ROW[i])
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while (True):

        # test #
        for j in range(1):
            GPIO.output(COL[j], 0)

            for i in range(4) :
                    if GPIO.input (ROW[i]) == 0:
                         btn = MATRIX[j][i]
                         print ("Button " + btn + " pressed")
                         temp_url = uri + "/press/" + btn
                         headers = { 'Authorization' : 'Bearer ' + access_token }
                         r = requests.put(temp_url, headers=headers)
                         print ("Button" + btn + " pressed - call:" + temp_url)
 
                         while(GPIO.input(ROW[i]) == 0):
                             pass   
            GPIO.output(COL[j],1)
            time.sleep(0.1)
                                
except KeyboardInterrupt:
    GPIO.cleanup()

