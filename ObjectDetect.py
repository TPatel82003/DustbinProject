import RPi.GPIO as GPIO
import time
from gpiozero import Servo
from time import sleep
servo = Servo(25)
val = -1
TRIG = 23
ECHO = 24
GPIO.setmode(GPIO.BCM)

def LidOpenClose():
    try:
        while True:
            servo.value = val
            sleep(0.1)
            val = val + 0.1
            if val > 1:
                val = -1
    except KeyboardInterrupt:
        print("Program stopped")

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
    time.sleep(1)
