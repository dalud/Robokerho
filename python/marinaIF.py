from arduinoIF import Arduino
from random import random
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# Niskat
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
# Polvi
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)


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
            #self.arduino.write('ml' + str(amp_L))
            self.moveNiskat()
            self.movePolvi()
            pass

    def resetMotors(self):
        self.arduino.write('ml' + str(0))
        self.arduino.write('')
        self.resetNiskat()
        self.resetPolvi()
        pass

    def resetNiskat(self):
        GPIO.output(7, GPIO.LOW)
        
    def moveNiskat(self):
        GPIO.output(7, GPIO.HIGH)

    def resetPolvi(self):
        GPIO.output(11, GPIO.LOW)
        
    def movePolvi(self):
        GPIO.output(11, GPIO.HIGH)

    def resetEyes(self):
        pass
        
    def vekeActive(self, stream):
        return 0

