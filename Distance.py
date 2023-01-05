import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)
import urllib.request

import random

def DistancetoPercentange(Distance):
    Fill = 35 - Distance
    return Fill * 100 / 35

def thingspeak_post(Distance):
    URl = "https://api.thingspeak.com/update?api_key="
    KEY = "QKBAEIL8OGG0O5N8"
    TrashLevel = DistancetoPercentange(Distance)
    HEADER = "&field1={}&field2={}&field3={}".format(Distance ,TrashLevel , 100 - TrashLevel)
    NEW_URL = URl + KEY + HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)

i = 1
while i <= 10:
    print("distance measurement in progress")
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("distance:", distance, "cm")
    thingspeak_post(distance)
    time.sleep(40)
    i = i + 1



  
