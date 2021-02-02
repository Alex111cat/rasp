from time import sleep
import Adafruit_DHT
import paho.mqtt.client as mqtt	
import json

gpio=4
sensor=Adafruit_DHT.DHT11

ORG = "fwrgzm"
DEVICE_TYPE = "raspi" 
TOKEN = "cJutGT)xU)teGgBfU?"
DEVICE_ID = "dca6324f3207"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/status1/fmt/json";
pubTopic2 = "iot-2/evt/status2/fmt/json";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")
    temperature = json.dumps({'temperature': temperature})
    humidity = json.dumps({'humidity': humidity})
    mqttc.publish(pubTopic1, temperature)
    mqttc.publish(pubTopic2, humidity)
    print ("Published")
    sleep(5);

mqttc.loop_forever()
