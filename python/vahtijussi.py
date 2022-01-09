from wlanIF import Wlan
import sys
import configparser
import signal

# Helpers
flush = sys.stdout.flush

# Read config
conf = configparser.ConfigParser()
conf.read('/home/pi/robokerho/config')

# Init Wlan
wlan = Wlan()
flush()

def signal_term_handler(signal, frame):
    print("STOPPED")
    sys.exit()

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)


# Main loop
while(True):
    #wlan.listen()
    cmd = input("Master:")
    print(cmd)
    wlan.broadcast(cmd)
    flush()
