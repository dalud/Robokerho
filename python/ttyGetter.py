import serial
from serial.tools import list_ports

from time import sleep


#devices = list_ports.comports()
#print(str(devices[0]))

#USB_PORT = str(devices[0]).split()
#print('DEV:', str(devices[0]).split()[0])
#arduino = serial.Serial(USB_PORT[0], 9600, timeout=1)


arduino = False
#arduino = True
i = 0

while(not arduino):    
    try:
        print('Trystä päivää. i =', i)
                
        arduino = serial.Serial(str(list_ports.comports()[i]).split()[0], 9600, timeout=1)
        #sleep(.1)
        arduino.write('s'.encode())
        arduino.write('\n'.encode())
    except:
        print('Connecting Arduino via USB. i =', i)
        i += 1
