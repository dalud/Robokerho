import sounddevice as sd
import soundfile as sf
from os import listdir
import os
from random import random
from time import sleep
import serial
from socket import *

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
   
#try:
   #usb = serial.Serial(USB_PORT, 9600, timeout=1)
#except:
   #print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   #print("Exiting program.")
   #exit()
usb = True
while(not usb):
   try:
      USB_PORT = "/dev/ttyACM0" #TODO: write getter()
      usb = serial.Serial(USB_PORT, 9600, timeout=1)
   except:
      print('Connecting USB...')

dir = '/home/pi/robokerho/samples/hurjajuttu/'
samples = os.listdir(dir)
print(samples)

def sout(msg):
    # usb.write('clr'.encode())
    sleep(1)    
    print(msg)    
    #for part in msg:
        #usb.write(part.encode())
    s.sendto(bytes(msg, encoding='utf-8'),('255.255.255.255',12345))

while True:
    alea = (int)(random()*len(samples))
    sout('Alea est:' + str(alea))
    data, fs = sf.read(dir+samples[alea], dtype='float32')    
    sd.play(data, fs)
    # status = sd.wait()  # Wait until file is done playing
    while sd.get_stream().active:
       sout('playing:' + samples[alea])
    slp = (int)(random()*100)
    sout('sleeping for:' + str(slp))
    sleep(slp)
