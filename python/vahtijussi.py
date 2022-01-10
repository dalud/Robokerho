from wlanIF import Wlan
import sys
import configparser
import signal

# Helpers
flush = sys.stdout.flush

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
    if cmd:
        wlan.broadcast('jussi:' + cmd)
    else:
        wlan.broadcast('jussi:' + 'NO')
    flush()
