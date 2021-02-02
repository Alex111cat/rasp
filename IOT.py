# Импортируем библиотеку и создаем инстанс REST клиента
from Adafruit_IO import Client
aio = Client('aio_RKMF083OFeAkGmPtfSJX1JBb9JGU')

# Отправляем значение 100 в канал с названием 'Foo'
aio.send('Foo', 100)

# Получаем последнее значение из канал 'Foo'
data = aio.receive('Foo')
print('Received value: {0}'.format(data.value))
