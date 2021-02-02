import sys
from PyQt5.QtWidgets import (QApplication, QLCDNumber, QLineEdit, QPushButton,
                             QGridLayout, QWidget)
import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    break

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Влажность и температура')
button = QPushButton('Enter')
textfield = "Press enter"

grid = QGridLayout()
grid.maximumSize()
grid.addWidget(textfield, 1, 1, 1, 2)
grid.addWidget(button, 2, 2)
window.setLayout(grid)


def sync_lcd():
    textfield.clean()
    textfield = QLineEdit("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    textfield.setFocus()
    textfield.show()


button.clicked.connect(sync_lcd)  # update LCD on click
button.setAutoDefault(True)  # click on <Enter>
textfield.returnPressed.connect(button.click)  # click on <Enter>
sync_lcd()

window.show()
sys.exit(app.exec())
