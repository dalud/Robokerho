import sounddevice as sd
import soundfile as sf


filename = '/home/pi/robokerho/samples/Hurjajuttu/Puhe 006HalvintaKaljaa.wav'
data, fs = sf.read(filename, dtype='float32')  
mouthVel = 90 #scale according to mouth motor
sd.play(data, fs)

while sd.get_stream().active:    
    with sd.Stream() as stream:
        amp = round(stream.read(1024)[0].max(), 1)*mouthVel
        print(amp)
        
    
