import serial
from time import sleep


class Arduino:
    def __init__(self):
        self.arduino = False
    
    def connect(self):        
        while(not self.arduino):
            try:
                USB_PORT = "/dev/ttyACM1" #TODO: write getter()
                self.arduino = serial.Serial(USB_PORT, 9600, timeout=1)
            except:
                print('Connecting Arduino via USB...')

    def write(self, msg):
        self.arduino.write(msg)
        sleep(.04)
        
