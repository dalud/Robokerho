import sounddevice as sd
import soundfile as sf

class Sound:
    def play(self, sample):
        data, fs = sf.read(sample, dtype='float32')      
        sd.play(data, fs)

    def active(self):
        return sd.get_stream().active

    def stream(self):
        return sd.Stream(sd.default.samplerate, 0, sd.default.device, 2)
        
