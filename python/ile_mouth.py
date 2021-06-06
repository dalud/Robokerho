import sounddevice as sd
import soundfile as sf
import serial
from time import sleep

#filename = '/home/pi/robokerho/samples/Hurjajuttu/Puhe 006HalvintaKaljaa.wav'
filename = '/media/pi/EMTII/samples/ile/Hurjajutut_LeftRightPan/02_josjokuhuutaasulle.wav'
data, fs = sf.read(filename, dtype='float32')
mouthVel = 150 # scale according to mechanics

sd.play(data, fs)

#arduino = True
arduino = False
while(not arduino):
   try:
      USB_PORT = "/dev/ttyACM0" #TODO: write getter()
      arduino = serial.Serial(USB_PORT, 9600, timeout=1)
   except:
      print('Connecting USB...')

while sd.get_stream().active:    
   with sd.Stream(sd.default.samplerate, 0, sd.default.device, 2) as stream:      
      amp = stream.read(128)[0] # increase blocksize for better accuracy     
      #print(amp)
      L = []
      R = []
      for i in range(len(amp)):         
         L.append(amp[i][0])
         R.append(amp[i][1])
      amp_L = round(max(L)*mouthVel, 1)
      amp_R = round(max(R)*mouthVel, 1)      

      print('L:', amp_L, 'R:', amp_R)
      # Left audio channel
      if(amp_L):
         arduino.write('mL'.encode())
         arduino.write(str(amp_L).encode())
         arduino.write('\n'.encode())
      # R
      if(amp_R):
         arduino.write('mR'.encode())
         arduino.write(str(amp_R).encode())
         arduino.write('\n'.encode())
      
      sleep(.03)
   arduino.write(0)
   arduino.write('\n'.encode())
