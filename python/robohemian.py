from wlanIF import Wlan
import os
from random import random
from soundIF import Sound
from ileIF import Ile
from marinaIF import Marina
import sys
import configparser
from time import sleep
import signal
from datetime import datetime


# Helpers
flush = sys.stdout.flush
go = True

# Read config
conf = configparser.ConfigParser()
conf.read('/home/pi/robokerho/config')

# Get samples
dir = conf.get('env', 'dir')
samples = os.listdir(dir)
played = []
samples.sort()
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
flush()

# Init Sound
sound = Sound()
flush()

def signal_term_handler(signal, frame):
    print("STOPPED")
    flush()
    sound.stop()
    robo.resetMotors()
    sys.exit()
    start(['sudo', 'kill', '-9', str(os.getpid())])

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

def speak():
    # Pick random sample
    alea = (int)(random()*len(samples))

    # Don't repeat yourself
    while played.count(alea):
        print("Täytyy arpoa uus...")
        alea = (int)(random()*len(samples))
        if len(played) == len(samples):
            print("Kaikki meni jo!")
            played.clear()

    # Play the sample
    #sound.play(dir+samples[alea])
    sound.play(dir+samples[1])

    # Get start time
    st = datetime.timestamp(datetime.now())

    while sound.active():
        # Calculate running time
        rt = int(datetime.timestamp(datetime.now())-st)
        #print(rt)
        with sound.stream() as stream:
            #robo.speak(stream, samples[alea])
            robo.speak(stream, samples[1])
            flush()

            if(robo.vekeActive(stream) > .4):
                wlan.broadcast('veke:' +str(robo.vekeActive(stream)) +':' +str(rt) +':' +samples[1])
                robo.resetMotors() # Make sure none get locked HIGH
            else:
                #wlan.broadcast('playing:' + samples[alea] + str(rt))
                wlan.broadcast('playing:' +samples[1] +':' +str(rt))
                flush()
    robo.resetMotors()

# Main loop
while(True):
    print("Aktiv: ", go)
    flush()
    try:
        hear = wlan.listen()
        if hear and 'GO' in hear[0].decode():
            print("Nyt pitäis aktivoitua")
            sleep(1)
            go = True
        if hear and 'NO' in hear[0].decode():
            robo.resetMotors()
            print("Nyt pitäis passivoitua")
            go = False

        if go and not wlan.listen():
            speak()
            flush()
            sleep(15)

    except KeyboardInterrupt:
        print("User exit")
        flush()
        sound.stop()
        robo.resetMotors()
        sys.exit()
