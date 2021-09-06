from wlanIF import Wlan
from os import listdir
import os
from random import random
from soundIF import Sound
from ileIF import Ile


# Get samples
<<<<<<< HEAD
# dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
dir = '/home/pi/robokerho/samples/marina/'
=======
dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
#dir = '/home/pi/robokerho/samples/marina/'
>>>>>>> c2ebbd0b1f6a7817bee7b918453ff6cf5c28788a
samples = os.listdir(dir)
print(samples)

robo = Ile()

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
        with sound.stream() as stream:
            robo.speak(stream, samples[alea])            
            wlan.broadcast('playing:' + samples[alea])
            robo.resetMotors() # Make sure none get locked HIGH
    robo.resetEyes()

# Main loop
while(True):    
    wlan.broadcast('snoozing')
    wlan.listen()
    speak()
