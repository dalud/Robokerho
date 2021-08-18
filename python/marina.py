import sounddevice as sd
import soundfile as sf
from os import listdir
import os
from random import random
from time import sleep
from socket import *
import serial
from serial.tools import list_ports


arduino = False
i = 0

while(not arduino):    
    try:                
        arduino = serial.Serial(str(list_ports.comports()[i]).split()[0], 9600, timeout=1)
    except:
        print('Connecting Arduino via USB. i =', i)
        i += 1

#dir = '/home/pi/robokerho/samples/marina/'
dir = '/home/pi/robokerho/samples/ile/Hurjajutut_LeftRightPan/'
samples = os.listdir(dir)
print(samples)

mouthVel_L = 1023 # scale according to mechanics
mouthVel_R = 1023 # 1023 max X/Y value for silmat, 500 = lepo

pause = .3 # Amp threshold interpreted as pause
dly = .01 # Universal delay

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

            print('Playing:', samples[alea], 'L:', amp_L, 'R:', amp_R)
            # Left audio channel
            if(amp_L > pause):
                arduino.write('ml'.encode())
                arduino.write(str(amp_L).encode())
                arduino.write('\n'.encode())
                sleep(dly)
                # Move eyes
                arduino.write('ex'.encode())
                arduino.write(str(amp_L).encode())
                arduino.write('\n'.encode())
                sleep(dly)
            # Right audio channel
            if(amp_R > pause):
                arduino.write('mr'.encode())
                arduino.write(str(amp_R).encode())
                arduino.write('\n'.encode())
                sleep(dly)
            # Blink
            # if(amp_L < pause and amp_R < pause):            
            if(random() < .05):
                arduino.write('b'.encode())            
                arduino.write('\n'.encode())
                sleep(.15)
            # Reset eyes
            if(amp_L < pause):
                resetEyes()
        
        mouth.sendto(bytes('playing:' + samples[alea], encoding='utf-8'),('255.255.255.255',12345))
        resetMotors()
    resetEyes()
    mouth.close()
   

# TODO: error prone if network not available
def broadcast(msg):
    mouth = socket(AF_INET, SOCK_DGRAM)    
    mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    mouth.setblocking(False)
    mouth.sendto(bytes(msg, encoding='utf-8'),('255.255.255.255',12345))
    mouth.close()

def resetMotors():
    arduino.write('ml'.encode())
    arduino.write(0)
    arduino.write('\n'.encode())
    sleep(dly)
    arduino.write('mr'.encode())
    arduino.write(0)
    arduino.write('\n'.encode())
    sleep(dly)
    arduino.write(''.encode())
    arduino.write('\n'.encode())
    sleep(dly)       
    arduino.write(''.encode())
    arduino.write('\n'.encode())
    sleep(dly)

def resetEyes():
    arduino.write('ex500'.encode())
    arduino.write('\n'.encode())
    sleep(dly)

while(True):    
    broadcast('snoozing')
    listen()
    speak()
