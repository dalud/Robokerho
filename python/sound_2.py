import sounddevice as sd
import soundfile as sf

filename = '/home/pi/robokerho/samples/hurjajuttu/Puhe 006HalvintaKaljaa.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
# status = sd.wait()  # Wait until file is done playing
while sd.get_stream().active:
    with sd.Stream() as stream:
        print(round(stream.read(1024)[0].max(), 1)*10)
