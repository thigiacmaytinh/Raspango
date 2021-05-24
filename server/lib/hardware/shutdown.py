import RPi.GPIO as GPIO
import os

pinInput=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(pinInput, GPIO.FALLING)
    os.system("sudo shutdown -h now")
except:
    pass

GPIO.cleanup()
