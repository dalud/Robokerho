from wlanIF import Wlan
from os import listdir
import os
from random import random
from soundIF import Sound
from ileIF import Ile
from marinaIF import Marina
import sys

# Get samples
#dir = '/home/pi/robokerho/samples/marina/'
#dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
dir = '/home/pi/robokerho/samples/hurjajuttu_lasten/'
samples = os.listdir(dir)
print(samples)

robo = Ile()
#robo = Marina()

# Init Wlan
wlan = Wlan()

# Init Sound
sound = Sound()

def speak():
    # Pick random sample
    alea = (int)(random()*len(samples))

    # Play the sample
    sound.play(dir+samples[alea])# Init Wlan
    #sound.play('/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/hurjajuttu 64 v-tuttaa kaikki.wav')
    
    while sound.active():
        with sound.stream() as stream:
            robo.speak(stream, samples[alea])
            wlan.broadcast('playing:' + samples[alea])

            if(robo.vekeActive(stream) > .4):
                wlan.broadcast('veke:' + str(robo.vekeActive(stream)))
                robo.resetMotors() # Make sure none get locked HIGH
    robo.resetMotors()

# Main loop
while(True):    
    try:
        robo.resetMotors()
        wlan.broadcast('snoozing')
        wlan.listen()
        speak()
    # TODO: except general error
    except KeyboardInterrupt:
        print("User exit")
        robo.resetMotors()
        sys.exit()
