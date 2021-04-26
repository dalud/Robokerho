from tkinter import *
import tkSnack

root = Tk()
tkSnack.initializeSnack(root)

snd = tkSnack.Sound()
snd.read('/home/pi/robokerho/samples/marina/36 dicen que lo sano.wav')
snd.play(blocking=0)
          
