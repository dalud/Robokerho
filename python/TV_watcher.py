from wlanIF import Wlan
import sys
from time import sleep


# Helpers
flush = sys.stdout.flush

# Init Wlan
wlan = Wlan()
flush()

# Scenes
def scene1():
    print("###########################")
    print("THE OCEAN BLAA BLAA BLAA...")
    print("###########################")
    flush()
    sleep(1)

def scene2():
    print("#################################")
    print("TÄMÄ ON HYVÄ BIISI, BY THE WAY...")
    print("#################################")
    flush()
    sleep(3)
    print("###################")
    print("- NIIN MUUTEN ONKI!")
    print("###################")
    flush()
    sleep(1)


def scene3():
    print("############")
    print("WHO ARE YOU?")
    print("############")
    flush()
    sleep(1)
    print("################")
    print("WHO AM I TO YOU?")
    print("################")
    flush()
    sleep(1)
        
def scene4():
    print("#########")
    print("DELFIINI!")
    print("#########")
    flush()
    sleep(1)

def scene5():
    print("####################")
    print("KIVA TÄMÄ VIULUSOOLO")
    print("####################")
    flush()
    sleep(5)
    print("###############")
    print("- NIIN KYLLÄ ON")
    print("###############")
    flush()
    sleep(2)
    print("###########")
    print("- TOSI KIVA")
    print("###########")
    flush()
    sleep(1)



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
            chunk = 500

            # The Ocean
            mile = 10500
            if(time>mile and time<(mile+chunk)): scene1()

            # The Song
            mile = 23000
            if(time>mile and time<(mile+chunk)): scene2()

            # The Chorus
            mile = 47500
            if(time>mile and time<(mile+chunk)): scene3()

            # The Dolphin
            mile = 74000
            if(time>mile and time<(mile+chunk)): scene4()

            # The Solo
            mile = 115000
            if(time>mile and time<(mile+chunk)): scene5()
        
    except KeyboardInterrupt:
        print("User exit")
        flush()
