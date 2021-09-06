from arduinoIF import Arduino
from wlanIF import Wlan
from os import listdir
import os
from random import random
from soundIF import Sound


# Get samples
# dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
dir = '/home/pi/robokerho/samples/marina/'
samples = os.listdir(dir)
print(samples)

# Init Arduino
arduino = Arduino()
arduino.connect()

# Init Wlan
wlan = Wlan()

# Init Sound
sound = Sound()

def speak():
    # Pick random sample
    alea = (int)(random()*len(samples))

    # Play the sample
    sound.play(dir+samples[alea])

    while sound.active():
        print('playing:' + samples[alea])
        wlan.broadcast('playing:' + samples[alea])    

# Main loop
while(True):    
    wlan.broadcast('snoozing')
    wlan.listen()
    speak()
