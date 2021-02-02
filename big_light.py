# библиотека для работы с пинами GPIO
import RPi.GPIO as GPIO
# библиотека для работі с временем
import time
 
# выбираем имена пинов BCM
GPIO.setmode(GPIO.BCM)
# устанавливаем светодиод в режим выхода
GPIO.setup(4, GPIO.OUT)
 
try:
    while True:
        # ждём одну секунду
        time.sleep(1)
        # зажигаем светодиод
        GPIO.output(4, GPIO.HIGH)
        # ждём одну секунду
        time.sleep(1)
        # гасим светодиод
        GPIO.output(4, GPIO.LOW)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')
