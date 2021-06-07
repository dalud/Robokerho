from arduinoIF import Arduino
from wlanIF import Wlan
from os import listdir
import os
from random import random
from soundIF import Sound


dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
samples = os.listdir(dir)
print(samples)

# Init Arduino
arduino = Arduino()
arduino.connect()
#arduino.write('ml'.encode() + str(20).encode() + '\n'.encode())

# Init Wlan
wlan = Wlan()
#wlan.listen()
#wlan.broadcast('HORO!')

# Pick random sample
alea = (int)(random()*len(samples))

# Init Sound
sound = Sound()
sound.play(dir+samples[alea])
while sound.active():
    print('playing:' + samples[alea])
    wlan.broadcast('playing:' + samples[alea])
wlan.broadcast('snoozing')

