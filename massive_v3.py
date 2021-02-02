import RPi.GPIO as GPIO
import time


leds = [12, 13, 14, 18]

GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(leds[i], GPIO.OUT)

try:
    while True:
        for i in range(4):
            time.sleep(0.25)
            GPIO.output(leds[i], GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(leds[i], GPIO.LOW)
            
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
