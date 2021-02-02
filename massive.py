import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [12, 13, 14, 18]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    
time.sleep(3)

for led in leds:
    GPIO.output(led, GPIO.LOW)
    
GPIO.cleanup()
