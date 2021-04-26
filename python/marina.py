from tkinter import *
import tkSnack
from random import random
from time import sleep
import serial


#try:
   #usb = serial.Serial(USB_PORT, 9600, timeout=1)
#except:
   #print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   #print("Exiting program.")
   #exit()
usb = False
while(not usb):
   try:
      USB_PORT = "/dev/ttyACM0" #TODO: write getter()
      usb = serial.Serial(USB_PORT, 9600, timeout=1)
   except:
      print('Connecting USB...')

root = Tk()
tkSnack.initializeSnack(root)

samples = [    
    '/home/pi/robokerho/samples/marina/1 Felicidad.wav',
    '/home/pi/robokerho/samples/marina/2 Enredadera.wav',
    '/home/pi/robokerho/samples/marina/3 Jaula.wav',
    '/home/pi/robokerho/samples/marina/4 Vomito.wav',    
    '/home/pi/robokerho/samples/marina/5 Jacaranda.wav',
    '/home/pi/robokerho/samples/marina/6 Polvo.wav',
    '/home/pi/robokerho/samples/marina/7 Polvo 2.wav',
    '/home/pi/robokerho/samples/marina/8 Caminante.wav',
    '/home/pi/robokerho/samples/marina/9 Caminante 2.wav',
    '/home/pi/robokerho/samples/marina/10 Creatura 1.wav',
    '/home/pi/robokerho/samples/marina/11 Creatura 2.wav',
    '/home/pi/robokerho/samples/marina/12 Tu aire.wav',
    '/home/pi/robokerho/samples/marina/13 Secreto.wav',
    '/home/pi/robokerho/samples/marina/14 llave.wav',    
    '/home/pi/robokerho/samples/marina/15 vergüenza.wav',
    '/home/pi/robokerho/samples/marina/16 inmunoglobina.wav',
    '/home/pi/robokerho/samples/marina/17 arbol menstrual.wav',
    '/home/pi/robokerho/samples/marina/18 auuuuu.wav',
    '/home/pi/robokerho/samples/marina/19 A la verga.wav',
    '/home/pi/robokerho/samples/marina/20 One more .wav',
    '/home/pi/robokerho/samples/marina/21 Who are you.wav',
    '/home/pi/robokerho/samples/marina/22 Laugh Cry.wav',
    "/home/pi/robokerho/samples/marina/23 i don't feel good.wav",
    '/home/pi/robokerho/samples/marina/24 miss my country.wav',
    '/home/pi/robokerho/samples/marina/25 hate people.wav',
    '/home/pi/robokerho/samples/marina/26 crying.wav',
    '/home/pi/robokerho/samples/marina/27 crying y voz.wav',
    '/home/pi/robokerho/samples/marina/28 niña fantasma.wav',
    '/home/pi/robokerho/samples/marina/29 cryng tristeza.wav',
    '/home/pi/robokerho/samples/marina/30 amor.wav',
    '/home/pi/robokerho/samples/marina/31 corazoncito.wav',    
    '/home/pi/robokerho/samples/marina/32 suicidio.wav',
    '/home/pi/robokerho/samples/marina/33 diosa .wav',
    '/home/pi/robokerho/samples/marina/34 olas de silencio .wav',
    '/home/pi/robokerho/samples/marina/35 angustia.wav',
    '/home/pi/robokerho/samples/marina/36 dicen que lo sano.wav',
    '/home/pi/robokerho/samples/marina/37 crying hombre cruel.wav',
    '/home/pi/robokerho/samples/marina/38 contenta.wav',
    '/home/pi/robokerho/samples/marina/39 chiquilla.wav',
    '/home/pi/robokerho/samples/marina/40 adolescente.wav',
    '/home/pi/robokerho/samples/marina/42 quiero saber.wav',    
    '/home/pi/robokerho/samples/marina/43 soap  .wav',
    '/home/pi/robokerho/samples/marina/44 dance  .wav',
    '/home/pi/robokerho/samples/marina/45 cuarentena .wav',
    '/home/pi/robokerho/samples/marina/46 cabezas calvas .wav',
    '/home/pi/robokerho/samples/marina/47 gracias song.wav',
    '/home/pi/robokerho/samples/marina/48 tired .wav',
    '/home/pi/robokerho/samples/marina/49 moment dad .wav',
    '/home/pi/robokerho/samples/marina/50 meille.wav',
]

def sout(msg):
    usb.write('clr'.encode())
    sleep(1)    
    print(msg)    
    for part in msg:
        usb.write(part.encode())

snd = tkSnack.Sound()
while(True):
    alea = (int)(random()*len(samples))
    sout(["Alea est:", str(alea)])
    snd.read(samples[alea])
    sout(['Playing:', samples[alea].rsplit('/home/pi/robokerho/samples/marina/')[1]])
    snd.play(blocking=1)
    slp = (int)(random()*100)
    sout(["Sleeping for:", str(slp)])
    sleep(slp)
