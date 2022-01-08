from wlanIF import Wlan
from arduinoIF import Arduino
from random import random
from time import sleep
import sys
import signal
import os
import subprocess
from threading import Thread


# Helpers
flush = sys.stdout.flush
ON_POSIX = 'posix' in sys.builtin_module_names

# Init Wlan
wlan = Wlan()
flush()

# Init Arduino
arduino = Arduino()
arduino.connect()
flush()

def signal_term_handler(signal, frame):
    resetMotors()
    print("STOPPED")
    start(['sudo', 'kill', '-9', str(os.getpid())])
    stop()
    
signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

def speak(amp):
    arduino.write('mm' + amp) # Kädet integrated into mm ?
    arduino.write('ex' + amp)
    # Kaulat
    arduino.write('kv' + amp)
    arduino.write('ko' + amp)

    # Blink
    if(random() < .2):
        arduino.write('b')
        sleep(.3)


def resetMotors():
    arduino.write('ex' + str(500))
    arduino.write('z')
    arduino.write('')
    flush()
resetMotors()

def start(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1, close_fds=ON_POSIX)
    t = Thread(target=enqueue_output, args=(process.stdout, q))
    t.daemon = True
    t.start()

def stop():
    print("STOPPED")    
    wlan.stop()
    resetMotors()
    sys.exit()
    start(['sudo', 'kill', '-9', str(os.getpid())])


# Main loop
while True:
    flush()
    try:
        if("veke" in wlan.listen()[0].decode()):
            speak(wlan.listen()[0].decode().split(':')[1])
            flush()
        else:
            resetMotors()
    
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        stop()

    except:
        pass
