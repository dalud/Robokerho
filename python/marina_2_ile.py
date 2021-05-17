import sounddevice as sd
import soundfile as sf
from os import listdir
import os
from random import random
from time import sleep
import serial
from socket import *

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

def listen():
   print('I am listening')
   ear = socket(AF_INET, SOCK_DGRAM)   
   ear.bind(('', 12345))
   ear.settimeout(10)

   try:
      hear = ear.recvfrom(1024)
      print('Hear?', hear)
      while hear[0].decode().startswith('playing'):
         print('Hear?', hear)
         #sout(...)
         sleep(1)
         print('Listening:', str(hear[1]))
         hear = ear.recvfrom(1024)
   except:
      print('I hear nothing')
   ear.close()

def speak():
   # Cast die
   alea = (int)(random()*len(samples))
   sout('Alea est:' + str(alea))

   # Play sound
   data, fs = sf.read(dir+samples[alea], dtype='float32')    
   sd.play(data, fs)

   # Broadcast
   mouth = socket(AF_INET, SOCK_DGRAM)
   mouth.setblocking(False)
   mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)   
   while sd.get_stream().active:
      sout('playing:' + samples[alea])
      mouth.sendto(bytes('playing:' + samples[alea], encoding='utf-8'),('255.255.255.255',12345))
   mouth.close()

def broadcast(msg):
   mouth = socket(AF_INET, SOCK_DGRAM)
   mouth.setblocking(False)
   mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
   mouth.sendto(bytes(msg, encoding='utf-8'),('255.255.255.255',12345))

def sout(msg):
   # usb.write('clr'.encode())
   sleep(1)    
   print(msg)    
   #for part in msg:
       #usb.write(part.encode())

while True:
   broadcast('snoozing')   
   listen()   
   speak()   
