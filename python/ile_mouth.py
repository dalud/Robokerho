import sounddevice as sd
import soundfile as sf
import serial
from time import sleep

filename = '/home/pi/robokerho/samples/hurjajuttu/Puhe 006HalvintaKaljaa.wav'
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)

#usb = True
arduino = False
while(not arduino):
   try:
      USB_PORT = "/dev/ttyACM0" #TODO: write getter()
      arduino = serial.Serial(USB_PORT, 9600, timeout=1)
   except:
      print('Connecting USB...')

while sd.get_stream().active:    
    with sd.Stream() as stream:
        amp = round(stream.read(1024)[0].max(), 1)*90 #TODO: scale according to mechanics
        print(amp)
        arduino.write(str(amp).encode())
        arduino.write('\n'.encode())
        sleep(.015)
        
    
