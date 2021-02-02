import RPi.GPIO as GPIO

def isPressed(btn, led):
    state = 1 - GPIO.input(btn)
    GPIO.output(led, state) 

leds = [12, 13, 14, 18]
buttons = [2, 3, 4, 8]

GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(buttons[i], GPIO.IN)
    GPIO.setup(leds[i], GPIO.OUT)

try:
    while True:
        for i in range(4):
            isPressed(buttons[i], leds[i])
            
except KeyboardInterupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed')
