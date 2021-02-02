import numpy
import time
import datetime
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt	
import json

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 27
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

ORG = "fwrgzm"
DEVICE_TYPE = "raspi" 
TOKEN = "cJutGT)xU)teGgBfU?"
DEVICE_ID = "dca6324f3207"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/status1/fmt/json";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

try:
    while True:
        today = datetime.datetime.today()
        
        if (today.hour == 5 and today.minute == 55 and today.second == 0):
            dist = []
            
            if DEVICE_ID == "dca6324f3207":
                dev_id = '0001'
            #print ("Device id =", dev_id)
                    
            for i in range(9):
                dist.append(distance())
                time.sleep(30)
                #print(dist)
            dist1 = round(numpy.mean(dist))
            print ("Measured Distance = %.1f cm" % dist1)
            
            #transfer data to IBM IOT Platform by json-file
            json_dist_data = json.dumps({'id': dev_id, 'distance': dist1})
            mqttc.publish(pubTopic1, json_dist_data)
            print ("Distance level is Published");
        
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

#mqttc.loop_forever()
