import RPi.GPIO as GPIO
import time

sound_channel=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound_channel, GPIO.OUT)

p=GPIO.PWM(sound_channel, 500)
p.start(50)
time.sleep(10)
p.stop()
GPIO.cleanup()
