import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt 
import json
import os
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ' + str(chan0.voltage) + 'V')

last_read = 0       # this keeps track of the last potentiometer value
tolerance = 250     # to keep from being jittery we'll only change
                    # volume when the pot has moved a significant amount
                    # on a 16-bit ADC

def remap_range(value, left_min, left_max, right_min, right_max):
    # this remaps a value from original (left) range to new (right) range
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (int)
    valueScaled = int(value - left_min) / int(left_span)

    # Convert the 0-1 range into a value in the right range.
    return int(right_min + (valueScaled * right_span))

gpio=4
sensor=Adafruit_DHT.DHT11

ORG = "fwrgzm"
DEVICE_TYPE = "raspi" 
TOKEN = "cJutGT)xU)teGgBfU?"
DEVICE_ID = "dca6324f3207"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic = "iot-2/evt/status/fmt/json";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

temp_smoke_status = False

try:
    while True:
        if DEVICE_ID == "dca6324f3207":
            dev_id = '0001'
        print ("Device id =", dev_id)
        
        temperature = Adafruit_DHT.read_retry(sensor, gpio)
        if temperature is not None:
            print("Temp=", temperature[1])
        else:
            print("Sensor failure. Check wiring.")
        
        # assume that the pot didn't move
        trim_pot_changed = False
        
        # read the analog pin
        trim_pot = chan0.value
        
        # how much has it changed since the last read?
        pot_adjust = abs(trim_pot - last_read)
        
        if pot_adjust > tolerance:
            trim_pot_changed = True
        
        if trim_pot_changed:
            # convert 16bit adc0 (0-65535) trim pot read into 0-100 volume level
            set_volume = remap_range(trim_pot, 0, 65535, 0, 100)
            
            # set OS volume playback volume
            print('Volume = {volume}%' .format(volume = set_volume))
            set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
            .format(volume = set_volume)
            os.system(set_vol_cmd)
            
            # save the potentiometer reading for the next loop
            last_read = trim_pot
            #print ("CH0:", trim_pot)


        if set_volume >= 40 or temperature[1] >= 35:
            temp_smoke_status = True
        else:
            temp_smoke_status = False
        
        #transfer data to IBM IOT Platform by json-file
        json_temp_smoke_data = json.dumps({'id': dev_id, 'temperature': temperature[1], 'smoke': set_volume})
        mqttc.publish(pubTopic, json_temp_smoke_data)
        print ("Temperature and Smoke levels are Published")
        
        if temp_smoke_status is True:
            time.sleep(5);
        else:
            time.sleep(10);
        
        
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

#mqttc.loop_forever()
