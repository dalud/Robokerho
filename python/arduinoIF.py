import serial
from serial.tools import list_ports
from time import sleep


class Arduino:
    def __init__(self):
        self.arduino = False
        self.i = 0
    
    def connect(self):        
        while(not self.arduino):
            try:                
                self.arduino = serial.Serial(str(list_ports.comports()[self.i]).split()[0], 9600, timeout=1)
                print('Arduino:', arduino)
            except:
                print('Connecting Arduino via USB. i =', self.i)
                self.i += 1

    def write(self, msg):        
        #if(not(self.arduino.is_open)):
        #self.arduino.open()
        #print('Is serial open?', self.arduino.is_open)
        self.arduino.write(msg.encode())
        self.arduino.write('\n'.encode())
        #self.arduino.close()
        sleep(.01)
