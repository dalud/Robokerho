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
lap = 0
dir = '/home/pi/robokerho/samples/tukholma4'

# Get samples for adlib program
samples = os.listdir("/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan")
print(samples)
flush()

# Init Wlan
wlan = Wlan()
flush()

# Init Sound
sound = Sound()
flush()

# Select robo
robo = Ile()
flush()
robo.resetMotors()

# Functions
def signal_term_handler(signal, frame):
    print("STOPPED")
    flush()
    sound.stop()
    robo.resetMotors()
    sys.exit()
    start(['sudo', 'kill', '-9', str(os.getpid())])

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

def speak(sample):
    sound.play(sample)
    
    while sound.active():
        with sound.stream() as stream:
            robo.speak(stream, sample)
            flush()

            if(robo.vekeActive(stream) > .4):
                wlan.broadcast('veke:' + str(robo.vekeActive(stream)))
                robo.resetMotors() # Make sure none get locked HIGH
            else:
                wlan.broadcast('playing:' + sample)
                flush()
    robo.resetMotors()

# Adlib a random sample
def adlib():
    global lap

    if lap >= 2:
        print("TV päälle!")
        wlan.broadcast("VIDEO")
        sleep(1)
        wlan.broadcast("VIDEO")
        sleep(2)
        lap = 0
    else:
        if not wlan.listen():
            # Pick random sample
            alea = (int)(random()*len(samples))

            # Play the sample
            speak("/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/"+samples[alea])
            flush()
            lap = lap+1
            sleep(2)

# Watch TV and react
def watch(time):
            # Milestones
            chunk = 3000 # window of opportunity to proc scene

            # 0:06
            mile = 5000
            if(time>mile and time<(mile+chunk)): scene1()

            # 1:17
            mile = 65000#77000
            if(time>mile and time<(mile+chunk)): scene2()

            # 1:57
            mile = 117000
            if(time>mile and time<(mile+chunk)): scene3()

            # 2:42
            mile = 162000
            if(time>mile and time<(mile+chunk)): scene4()

            # 4:24
            mile = 263000
            if(time>mile and time<(mile+chunk)): scene5()

            # 5:18
            mile = 318000
            if(time>mile and time<(mile+chunk)): scene6()

            # 5:46
            mile = 346000
            if(time>mile and time<(mile+chunk)): scene7()

            # 6:48
            mile = 408000
            if(time>mile and time<(mile+chunk)): scene8()

            # 8:15
            mile = 495000
            if(time>mile and time<(mile+chunk)): scene9()

            # 9:47
            mile = 587000
            if(time>mile and time<(mile+chunk)): scene10()

            # 10:38
            mile = 638000
            if(time>mile and time<(mile+chunk)): scene11()

# Scenes
def scene1():
    speak(dir + '/0_06.wav')
    flush()
    sleep(1)

def scene2():
    speak(dir + '/1_17.wav')
    flush()
    sleep(1)

def scene3():
    speak(dir + '/1_57.wav')
    flush()
    sleep(1)
    
def scene4():
    speak(dir + '/2_42.wav')
    flush()
    sleep(1)

def scene5():
    speak(dir + '/4_24.wav')
    flush()
    sleep(1)

def scene6():
    speak(dir + '/5_18.wav')
    flush()
    sleep(1)

def scene7():
    speak(dir + '/5_46.wav')
    flush()
    sleep(1)

def scene8():
    speak(dir + '/6_48.wav')
    flush()
    sleep(1)

def scene9():
    speak(dir + '/8_15.wav')
    flush()
    sleep(1)

def scene10():
    speak(dir + '/9_47.wav')
    flush()
    sleep(1)

def scene11():
    speak(dir + '/10_38.wav')
    flush()
    sleep(2)


# Main loop
while(True):
    flush()
    try:
        hear = wlan.listen()
        if hear and 'TV' in hear[0].decode():
            # Watch TV with parsed time code
            if hear[0].decode().split(':')[1]:
                watch(int(hear[0].decode().split(':')[1]))
        else: adlib()
    except KeyboardInterrupt:
        print("User exit")
        flush()
