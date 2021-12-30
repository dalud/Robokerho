from wlanIF import Wlan
from arduinoIF import Arduino
from random import random
from time import sleep
import sys
import signal


# Helpers
flush = sys.stdout.flush

# Init Wlan
wlan = Wlan()
flush()

# Init Arduino
arduino = Arduino()
arduino.connect()
flush()

def signal_term_handler(signal, frame):
    print("STOPPED")
    resetMotors()
    sys.exit()

signal.signal(signal.SIGTERM, signal_term_handler)

def speak(amp):
    print("MEikä puhhuu" + amp)
    arduino.write('mm' + amp)
    arduino.write('ex' + amp)
    arduino.write('kv' + amp)
    arduino.write('ko' + amp)

    # Blink
    if(random() < .2):
        arduino.write('b')
        sleep(.3)
    #arduino.write('')

def resetMotors():
    #arduino.write('kv' + str(90))
    #arduino.write('ko' + str(90))
    #arduino.write('mm' + str(0))
    arduino.write('ex' + str(500))
    arduino.write('z')
    arduino.write('')
resetMotors()

# Main loop
while(True):
    #print(hear[0].decode().split(':')[1])
    try:
        hear = wlan.listen()
        flush()
        if("veke" in hear[0].decode()):
            #print("NYT!")
            #print(hear[1])
            speak(hear[0].decode().split(':')[1])
        else:
            resetMotors()

    # TODO: except general error
    except KeyboardInterrupt:
        print("User exit")
        resetMotors()
        sys.exit()

    except:
        resetMotors()
