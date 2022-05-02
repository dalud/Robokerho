from wlanIF import Wlan
import sys
from time import sleep
from soundIF import Sound
        

# Helpers
flush = sys.stdout.flush

# Init Wlan
wlan = Wlan()
flush()

# Init Sound
sound = Sound()
flush()


# Scenes
def scene1():
    sound.play('/home/pi/robokerho/samples/tukholma3/0_06.wav')
    while sound.active(): print("scene1: playing 0:06")
    flush()

def scene2():
    sound.play('/home/pi/robokerho/samples/tukholma3/1_17.wav')
    while sound.active(): print("scene2: playing 1:17")
    flush()

def scene3():
    sound.play('/home/pi/robokerho/samples/tukholma3/1_57.wav')
    while sound.active(): print("scene3: playing 1:57")
    flush()
    
def scene4():
    sound.play('/home/pi/robokerho/samples/tukholma3/2_42.wav')
    while sound.active(): print("scene4: playing 2:42")
    flush()

def scene5():
    sound.play('/home/pi/robokerho/samples/tukholma3/4_24.wav')
    while sound.active(): print("scene5: playing 4:24")
    flush()

def scene6():
    sound.play('/home/pi/robokerho/samples/tukholma3/5_18.wav')
    while sound.active(): print("scene6: playing 5:18")
    flush()

def scene7():
    sound.play('/home/pi/robokerho/samples/tukholma3/5_46.wav')
    while sound.active(): print("scene7: playing 5:46")
    flush()

def scene8():
    sound.play('/home/pi/robokerho/samples/tukholma3/6_48.wav')
    while sound.active(): print("scene8: playing 6:48")
    flush()

def scene9():
    sound.play('/home/pi/robokerho/samples/tukholma3/8_15.wav')
    while sound.active(): print("scene9: playing 8:15")
    flush()

def scene10():
    sound.play('/home/pi/robokerho/samples/tukholma3/9_47.wav')
    while sound.active(): print("scene10: playing 9:47")
    flush()

def scene11():
    sound.play('/home/pi/robokerho/samples/tukholma3/10_38.wav')
    while sound.active(): print("scene10: playing 10:38")
    flush()


# Main loop
while(True):
    flush()
    try:
        hear = wlan.listen()
        if hear and 'TV' in hear[0].decode():
            #Parse time code
            try: time = int(wlan.listen()[0].decode().split(':')[1])
            except: continue

            # Milestones
            chunk = 2000 # window of opportunity to proc scene

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

    except KeyboardInterrupt:
        print("User exit")
        flush()
