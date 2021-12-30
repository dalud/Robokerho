from wlanIF import Wlan
from os import listdir
import os
from random import random
from soundIF import Sound
from ileIF import Ile
from marinaIF import Marina
import sys
import configparser
from time import sleep
import signal


# Helpers
flush = sys.stdout.flush

# Read config
conf = configparser.ConfigParser()
conf.read('/home/pi/robokerho/config')

# Get samples
dir = conf.get('env', 'dir')
samples = os.listdir(dir)
print(samples)
flush()

# Select robo
robo = conf.get('env', 'robo')
if(robo == 'ile'):
    robo = Ile()
    flush()
elif(robo == 'marina'):
    robo = Marina()
    flush()
else:
    print("No suitable robot class found. Exiting.")
    sys.exit(1)

robo.resetMotors()

# Init Wlan
wlan = Wlan()

# Init Sound
sound = Sound()

def signal_term_handler(signal, frame):
    print("STOPPED")
    sound.stop()
    robo.resetMotors()
    sys.exit()

signal.signal(signal.SIGTERM, signal_term_handler)

def speak():
    # Pick random sample
    alea = (int)(random()*len(samples))

    # Play the sample
    sound.play(dir+samples[alea])
    #sound.play('/home/pi/robokerho/samples/marina/14 llave.wav')

    while sound.active():
        with sound.stream() as stream:
            robo.speak(stream, samples[alea])
            flush()
            wlan.broadcast('playing:' + samples[alea])

            if(robo.vekeActive(stream) > .4):
                wlan.broadcast('veke:' + str(robo.vekeActive(stream)))
                robo.resetMotors() # Make sure none get locked HIGH
    robo.resetMotors()

# Main loop
while(True):
    try:
        wlan.broadcast('snoozing')

        if not wlan.listen():
            flush()
            speak()
            sleep(4)

    # TODO: except general error
    except KeyboardInterrupt:
        print("User exit")
        sound.stop()
        robo.resetMotors()
        sys.exit()
