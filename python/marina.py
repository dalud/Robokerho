import sounddevice as sd
import soundfile as sf
from os import listdir
import os
from random import random
from time import sleep
import serial
from socket import *

ear = socket(AF_INET, SOCK_DGRAM)
ear.bind(('', 12345))

        #if not data:
            #break
        #print(data)

usb = False
while(not usb):
   try:
      USB_PORT = "/dev/ttyACM0" #TODO: write getter()
      usb = serial.Serial(USB_PORT, 9600, timeout=1)
   except:
      print('Connecting USB...')

dir = '/home/pi/robokerho/samples/marina/'
samples = os.listdir(dir)
print(samples)


def sout(msg):
    usb.write('clr'.encode())
    sleep(1)    
    print(msg)    
    #for part in msg:
       #usb.write(part.encode())
    usb.write(msg.encode())

def speak():
    alea = (int)(random()*len(samples))
    sout('alea est:' + str(alea))
    data, fs = sf.read(dir+samples[alea], dtype='float32')  
    sout('playing:' + samples[alea])
    sd.play(data, fs)

while(True):
    hear = ear.recvfrom(1024)
    print('Hear:', hear)
        
    while hear[0].decode().startswith('playing:'):
       sout('Listening:' + str(hear[1]))
       hear = ear.recvfrom(1024)

    speak()
    
    #status = sd.wait()  # Wait until file is done playing
    #slp = (int)(random()*100)
    #sout('sleeping for:' + str(slp))
    #sleep(slp)
