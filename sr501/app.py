#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

input_channel=14
output_channel=12
sound_energy_channel=23
sound_pwm_channel=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(input_channel, GPIO.IN)
GPIO.setup(output_channel, GPIO.OUT, initial=GPIO.LOW)
# sound
GPIO.setup(sound_pwm_channel, GPIO.OUT)
p=GPIO.PWM(sound_pwm_channel, 2000)
GPIO.setup(sound_energy_channel, GPIO.OUT, initial=GPIO.LOW)

justnow_nobody = True

def switch():
    global justnow_nobody
    if GPIO.input(input_channel):
        if justnow_nobody:
            justnow_nobody = False
            GPIO.output(output_channel, GPIO.HIGH)
            p.start(20)
            GPIO.output(sound_energy_channel, GPIO.HIGH)
    else:
        if not justnow_nobody:
            justnow_nobody=True
            GPIO.output(output_channel, GPIO.LOW)
            GPIO.output(sound_energy_channel, GPIO.LOW)
            p.stop()

try:
    while True:
        switch()
        time.sleep(0.1)
    # GPIO.add_event_detect(input_channel, GPIO.BOTH, callback=switch)
    # GPIO.add_event_detect(input_channel, GPIO.FALLING, callback=switch_off)
    # time.sleep(100)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("end")
