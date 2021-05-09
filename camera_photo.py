# подключаем необходимые библиотеки
from picamera import PiCamera
from time import sleep
 
# создаём объект для работы с камерой
camera = PiCamera()
 
# запускаем предпросмотр сигнала с камеры на экране поверх всех окон
camera.start_preview()
 
# даём камере три секунды на автофокусировку и установку баланса белого
sleep(3)
 
# делаем снимок и сохраняем его на рабочий стол с именем image.jpg
camera.capture('/home/pi/Desktop/image.jpg')
 
# выключаем режим предпросмотра
camera.stop_preview()
