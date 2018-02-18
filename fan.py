import RPi.GPIO as GPIO 
import time

channel=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

for i in range(10):
    GPIO.output(channel, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
