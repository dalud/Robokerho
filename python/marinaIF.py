from arduinoIF import Arduino
from random import random
from time import sleep


class Marina:
    def __init__(self):
        self.mouthVel_L = 1023 # scale according to mechanics
        self.mouthVel_R = 1023 # 1023 max X/Y value for silmat, 500 = lepo
        self.pause = .3 # Amp threshold interpreted as pause
        #self.dly = .01 # Universal delay

        # Init Arduino
        self.arduino = Arduino()
        self.arduino.connect()

    def speak(self, stream, sample):
        amp = stream.read(128)[0] # increase blocksize for better accuracy        
        L = []
        R = []
        for i in range(len(amp)):         
            L.append(amp[i][0])
            R.append(amp[i][1])
        amp_L = round(max(L)*self.mouthVel_L, 1)
        amp_R = round(max(R)*self.mouthVel_R, 1)      

        print('Playing:', sample, 'L:', amp_L, 'R:', amp_R)
        if(amp_L > self.pause):
            self.arduino.write('ml' + str(amp_L))
            pass

    def resetMotors(self):
        self.arduino.write('ml' + str(0))
        self.arduino.write('')
        pass

    def resetEyes(self):
        pass
        
