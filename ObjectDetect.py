import RPi.GPIO as GPIO
import time
from gpiozero import Servo
from time import sleep
TRIG = 23
ECHO = 24
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)

def LidOpenClose():
    angle = float(input('Enter angle between 0 & 180: '))
    servo1.ChangeDutyCycle(7)
    time.sleep(5)
    servo1.ChangeDutyCycle(0)


while True:
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
    if(distance < 10):
        LidOpenClose()
    time.sleep(5)
