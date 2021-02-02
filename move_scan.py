from gpiozero import MotionSensor
import time
import datetime
 
# Create object for PIR Sensor
# PIR Sensor is on GPIO-4 (Pin 7)
pir = MotionSensor(4)
 
while True:
    # Wait for a motion to be detected
    pir.wait_for_motion
    # Print text to Shell
    print("Sneaky Person Alert!!")
    time.sleep(2)
