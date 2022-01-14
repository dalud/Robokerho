import sys
from arduinoIF import Arduino
import serial
from time import sleep
from wlanIF import Wlan

# Helpers
flush = sys.stdout.flush

# Init Wlan
wlan = Wlan()
flush()

# Connect arduino
arduino = Arduino()
arduino.connect()
flush()


while True:
    print("Vahti-Jussi vahtii...")
    msg = arduino.read()
    #msg = "k"
    #print(msg)
    if msg:
        print("Nyt tuli asiakas!")
        flush()
        wlan.broadcast("jussi:GO")
        flush()
        sleep(2)
    else:
        #print("Ei")
        wlan.broadcast("jussi:NO")
        flush()
