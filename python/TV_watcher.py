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
    sound.play('/home/pi/robokerho/samples/stockholm/0_00.wav')
    while sound.active(): print("scene1: playing 0:00")
    flush()

def scene2():
    sound.play('/home/pi/robokerho/samples/stockholm/0_22.wav')
    while sound.active(): print("scene2: playing 0:22")
    flush()

def scene3():
    sound.play('/home/pi/robokerho/samples/stockholm/0_40.wav')
    while sound.active(): print("scene3: playing 0:40")
    flush()
    
def scene4():
    sound.play('/home/pi/robokerho/samples/stockholm/1_04_2.wav')
    while sound.active(): print("scene4: playing 1:04 (2)")
    flush()

def scene5():
    sound.play('/home/pi/robokerho/samples/stockholm/1_34.wav')
    while sound.active(): print("scene5: playing 1:34")
    flush()

def scene6():
    sound.play('/home/pi/robokerho/samples/stockholm/2_43.wav')
    while sound.active(): print("scene6: playing 2:43")
    flush()

def scene7():
    sound.play('/home/pi/robokerho/samples/stockholm/4_05.wav')
    while sound.active(): print("scene7: playing 4:05")
    flush()

def scene8():
    print("scene8: playing 7:08")
    sound.play('/home/pi/robokerho/samples/stockholm/7_08.wav')
    while sound.active(): print("scene8: playing 7:08")
    flush()

def scene9():
    sound.play('/home/pi/robokerho/samples/stockholm/7_28.wav')
    while sound.active(): print("scene9: playing 7:28")
    flush()

def scene10():
    sound.play('/home/pi/robokerho/samples/stockholm/8_14.wav')
    while sound.active(): print("scene10: playing 8:14")
    flush()

def scene11():
    sound.play('/home/pi/robokerho/samples/stockholm/8_50.wav')
    while sound.active(): print("scene11: playing 8:50")
    flush()

def scene12():
    sound.play('/home/pi/robokerho/samples/stockholm/9_46.wav')
    while sound.active(): print("scene12: playing 9:46")
    flush()

def scene13():
    sound.play('/home/pi/robokerho/samples/stockholm/10_40.wav')
    while sound.active(): print("scene13: playing 10:40")
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

            # Milestones (what is a good chunk length?)
            chunk = 2000

            # 0:00
            mile = 100
            if(time>mile and time<(mile+chunk)): scene1()

            # 0:22
            mile = 22000
            if(time>mile and time<(mile+chunk)): scene2()

            # 0:40
            mile = 56000#40000
            if(time>mile and time<(mile+chunk)): scene3()

            # 1:04
            mile = 104000
            if(time>mile and time<(mile+chunk)): scene4()

            # 1:34
            mile = 131000
            if(time>mile and time<(mile+chunk)): scene5()

            # 2:43
            mile = 163000
            if(time>mile and time<(mile+chunk)): scene6()

            # 4:05
            mile = 247500
            if(time>mile and time<(mile+chunk)): scene7()

            # 7:08
            mile = 428000
            if(time>mile and time<(mile+chunk)): scene8()

            # 7:28
            mile = 450000
            if(time>mile and time<(mile+chunk)): scene9()

            # 8:14
            mile = 497000
            if(time>mile and time<(mile+chunk)): scene10()

            # 8:50
            mile = 530000
            if(time>mile and time<(mile+chunk)): scene11()

            # 9:46
            mile = 587000
            if(time>mile and time<(mile+chunk)): scene12()

            # 10:40
            mile = 636000
            if(time>mile and time<(mile+chunk)): scene13()
        
    except KeyboardInterrupt:
        print("User exit")
        flush()
