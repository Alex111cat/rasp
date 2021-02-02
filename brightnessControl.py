import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
dutyCycle = 50
pwm.start(dutyCycle)
 
try:
    while True:
        time.sleep(0.01)
        dutyCycle = dutyCycle + 1
        if (dutyCycle > 100):
            dutyCycle = 0
        pwm.ChangeDutyCycle(dutyCycle)
            
except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
