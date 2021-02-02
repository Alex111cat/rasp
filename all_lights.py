import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
leds = [10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 24, 26]
 
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
 
time.sleep(10)
 
for led in leds:
    GPIO.output(led, GPIO.LOW)
 
GPIO.cleanup()
