import sounddevice as sd
import soundfile as sf
from os import listdir
import os
from random import random
from time import sleep
from socket import *
import serial


arduino = False
while(not arduino):
   try:
      USB_PORT = "/dev/ttyACM0" #TODO: write getter()
      arduino = serial.Serial(USB_PORT, 9600, timeout=1)
   except:
      print('Connecting Arduino via USB...')

#dir = '/home/pi/robokerho/samples/marina/'
dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
samples = os.listdir(dir)
print(samples)
mouthVel_L = 150 # scale according to mechanics
mouthVel_R = 500 # scale according to mechanics

def listen():
   print('I am listening')
   ear = socket(AF_INET, SOCK_DGRAM)    
   ear.bind(('', 12345))
   ear.settimeout(10)

   try:
      hear = ear.recvfrom(1024)
      print('Hear?', hear)
      while hear[0].decode().startswith('playing:'):
         print('Hear?', hear)         
         hear = ear.recvfrom(1024)         
   except:
      print('I hear nothing')   
   ear.close()

def speak():
   # Cast die
   alea = (int)(random()*len(samples))

   # Play sound
   data, fs = sf.read(dir+samples[alea], dtype='float32')      
   sd.play(data, fs)

   # Broadcast
   mouth = socket(AF_INET, SOCK_DGRAM)    
   mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
   mouth.setblocking(False)      
   while sd.get_stream().active:
      with sd.Stream(sd.default.samplerate, 0, sd.default.device, 2) as stream:
         amp = stream.read(128)[0] # increase blocksize for better accuracy     
         #print(amp)
         L = []
         R = []
         for i in range(len(amp)):         
            L.append(amp[i][0])
            R.append(amp[i][1])
         amp_L = round(max(L)*mouthVel_L, 1)
         amp_R = round(max(R)*mouthVel_R, 1)      

         print('L:', amp_L, 'R:', amp_R)
         # Left audio channel
         if(amp_L):
            arduino.write('ml'.encode())
            arduino.write(str(amp_L).encode())
            arduino.write('\n'.encode())
         # R
         if(amp_R):
            arduino.write('mr'.encode())
            arduino.write(str(amp_R).encode())
            arduino.write('\n'.encode())
         
         sleep(.04)
      arduino.write('ml'.encode())
      arduino.write(0)
      arduino.write('\n'.encode())
      arduino.write('mr'.encode())
      arduino.write(0)
      arduino.write('\n'.encode())
      
      mouth.sendto(bytes('playing:' + samples[alea], encoding='utf-8'),('255.255.255.255',12345))
   mouth.close()

def broadcast(msg):
   mouth = socket(AF_INET, SOCK_DGRAM)    
   mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
   mouth.setblocking(False)
   mouth.sendto(bytes(msg, encoding='utf-8'),('255.255.255.255',12345))
   mouth.close()

while(True):    
   broadcast('snoozing')
   listen()
   speak()
