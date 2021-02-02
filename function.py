import RPi.GPIO as GPIO
import time

def isPressed(btn, led):
    if GPIO.input(btn) == False:
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)
        
button1 = 3
button2 = 4
led1 = 14
led2 = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
pwm = GPIO.PWM(led1, 1000)
pwm = GPIO.PWM(led2, 1000)
dutyCycle = 50
pwm.start(dutyCycle)

try:
    while True:
        isPressed(button1, led1)
        isPressed(button2, led2)
            
except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
