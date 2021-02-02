import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
 
try:
    while True:
        button = GPIO.input(2)
        GPIO.output(24, button)
except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
