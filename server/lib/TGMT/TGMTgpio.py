from threading import Thread, Lock
import cv2
from django.conf import settings as djangoSettings
import threading
import time, datetime
from django.conf import settings as djangoSettings
if(djangoSettings.IS_LINUX):
    import RPi.GPIO as GPIO

class TGMTgpio(threading.Thread):
    def __init__(self, _gpio_pin, _delay, _triggerValue):
        threading.Thread.__init__(self)
        self.gpio_pin = _gpio_pin
        self.delay = _delay
        self.triggerValue = _triggerValue

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(_gpio_pin, GPIO.OUT)
        djangoSettings.GPIO_VALUE[self.gpio_pin] = True

    def run(self):
        startTime = time.time()
        while True:
            GPIO.output(self.gpio_pin, self.triggerValue)     

            if(self.delay > 0):
                time.sleep(self.delay)
                GPIO.output(self.gpio_pin, not self.triggerValue)
                djangoSettings.GPIO_VALUE[self.gpio_pin] = False
                break
            else:                
                time.sleep(0.1)
                if(djangoSettings.GPIO_VALUE[self.gpio_pin] == False):
                    GPIO.output(self.gpio_pin, not self.triggerValue)
                    break


