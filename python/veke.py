from wlanIF import Wlan
from arduinoIF import Arduino
from random import random
from time import sleep
import sys


# Helpers
flush = sys.stdout.flush

# Init Wlan
wlan = Wlan()

# Init Arduino
arduino = Arduino()
arduino.connect()


def speak(amp):
    # print(amp)
    arduino.write('mm' + amp)
    arduino.write('ex' + amp)
    arduino.write('kv' + amp)
    arduino.write('ko' + amp)

    # Blink
    if(random() < .1):
        arduino.write('b')
        sleep(.3)
    #arduino.write('')

def resetMotors():
    arduino.write('kv' + str(90))
    arduino.write('ko' + str(90))
    arduino.write('mm' + str(0))
    arduino.write('ex' + str(500))
    arduino.write('')
resetMotors()

# Main loop
while(True):
    hear = wlan.listen()
    flush()
    #print(hear[0].decode().split(':')[1])
    try:
        if("veke" in hear[0].decode()):
            #print("NYT!")
            #print(hear[1])
            speak(hear[0].decode().split(':')[1])
        else:
            resetMotors()
    except:
        #print("Not me")
        pass
