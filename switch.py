import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
 
try:
    while True:
        button = GPIO.input(8)
        if button != False:
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(26, GPIO.LOW)
        else:
            GPIO.output(24, GPIO.LOW)
            GPIO.output(26, GPIO.HIGH)
            
except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
