from arduinoIF import Arduino
import serial
from time import sleep

arduino = Arduino()
arduino.connect()
sleep(1)

while True:
    msg = arduino.read()
    #msg = "k"
    print(msg)
    #if str(1) in msg.decode():
        #print("NYT!")
