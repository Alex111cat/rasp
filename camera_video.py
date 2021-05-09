from picamera import PiCamera
from time import sleep
 
camera = PiCamera()
 
# Запускаем предпросмотр сигнала с камеры на экране поверх всех окон
camera.start_preview()
 
# Начинаем запись видеофайла
camera.start_recording('/home/pi/Desktop/video.h264')
 
# Минуту пишем потоковое видео
camera.wait_recording(60)
 
# Останавливаем запись
camera.stop_recording()
 
# Выключаем предпросмотр
camera.stop_preview()
