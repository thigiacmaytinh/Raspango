import os
import time
import requests
import json
from django.conf import settings as djangoSettings

currentPath = os.path.abspath(__file__)
IS_LINUX = currentPath[0] == '/'
IS_WINDOWS = currentPath[1] == ':'

if(IS_LINUX):
    import RPi.GPIO as GPIO

#from api.models import Option

PIN_TRIGGER1 = 21
PIN_ECHO1 = 19

PIN_TRIGGER2 = 13
PIN_ECHO2 = 6

PIN_LED = 22

MIN_DISTANCE = 50
MAX_DISTANCE = 100

###################################################################################################

def InitSensor():
    if(not IS_LINUX):
        return
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
    GPIO.setup(PIN_ECHO1, GPIO.IN)

    GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
    GPIO.setup(PIN_ECHO2, GPIO.IN)

    GPIO.setup(PIN_LED, GPIO.OUT)

    print("Init ultrasonic success")

###################################################################################################

def DistanceUltraSonic(sensorID):
    GPIO.output(PIN_LED, GPIO.HIGH)

    # set Trigger to HIGH
    GPIO_TRIGGER = PIN_TRIGGER1
    GPIO_ECHO = PIN_ECHO1

    if(sensorID == 2):
        GPIO_TRIGGER = PIN_TRIGGER2
        GPIO_ECHO = PIN_ECHO2

    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while (GPIO.input(GPIO_ECHO) == 0 and time.time() - StartTime < 0.1):
        StartTime = time.time()
 
    # save time of arrival
    while (GPIO.input(GPIO_ECHO) == 1 and time.time() - StartTime < 0.1):
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    GPIO.output(PIN_LED, GPIO.LOW)
    return distance

####################################################################################################

def SendRequest():
    GPIO.output(PIN_LED, GPIO.HIGH)
    try:
        url = "http://localhost/api/webcam/play"
        response = requests.post(url, timeout=6)

        jsonObj = json.loads(response.text)        

        if("MIN_DISTANCE" in jsonObj):
            if(jsonObj["MIN_DISTANCE"] > 0):
                global MIN_DISTANCE
                MIN_DISTANCE = jsonObj["MIN_DISTANCE"]
                print("MIN_DISTANCE: " + MIN_DISTANCE)
        if("MAX_DISTANCE" in jsonObj):
            if(jsonObj["MAX_DISTANCE"] > 0):
                global MAX_DISTANCE
                MAX_DISTANCE = jsonObj["MAX_DISTANCE"]
                print("MAX_DISTANCE: " + MAX_DISTANCE)

        GPIO.output(PIN_LED, GPIO.LOW)
        return jsonObj["text"]
    except Exception as e:
        GPIO.output(PIN_LED, GPIO.LOW)
        return str(e)

####################################################################################################

if __name__ == '__main__':
    time.sleep(10) #wait to system boot complete
    InitSensor()
    validDistance = False

    while True:
        
        distance1 = int(DistanceUltraSonic(1))
        distance2 = int(DistanceUltraSonic(2))
        if(abs(distance1 - distance2) > 10):            
            time.sleep(0.2)            
            continue

        distance = distance2
        print("distance: " + str(distance))

        if(MIN_DISTANCE < distance and distance < MAX_DISTANCE):
            validDistance = True
        else:
            validDistance = False

        if(validDistance):
            response = SendRequest()
            if(response != None and response != ""):
                time.sleep(3)

        time.sleep(0.2)
        


