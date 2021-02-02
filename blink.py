import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
	while True:
		time.sleep(0.1)
		GPIO.output(17, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(17, GPIO.LOW)
		
		time.sleep(0.1)
		GPIO.output(18, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(18, GPIO.LOW)
		
		time.sleep(0.2)
		GPIO.output(19, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(19, GPIO.LOW)
		
		time.sleep(0.1)
		GPIO.output(24, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(24, GPIO.LOW)
		
		time.sleep(0.1)
		GPIO.output(10, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(10, GPIO.LOW)
		
except KeyboardInterrupt:
	print('The program was stopped by keyboard.')
finally:
	GPIO.cleanup()
	print('GPIO cleanup completed.')
