import sys
from PyQt5 import QtWidgets
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
 
        self.text = ("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
 
        self.label = QtWidgets.QLabel(self.text)
        self.label.setWordWrap(True)    
 
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)   
 
        self.show()

app = QtWidgets.QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
