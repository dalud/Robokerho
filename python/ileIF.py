from arduinoIF import Arduino
from random import random
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# Kaula
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
# Oikea käsi
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
# Suu
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)


class Ile:
    def __init__(self):
        self.mouthVel_L = 1023 # scale according to mechanics
        self.mouthVel_R = 1023 # 1023 max X/Y value for silmat, 500 = lepo
        self.pause = 10 # Amp threshold interpreted as mute

        # Init Arduino
        self.arduino = Arduino()
        self.arduino.connect()

    def speak(self, stream, sample):
        amp = stream.read(128)[0] # increase blocksize for better accuracy
        #print(amp)
        L = []
        R = []
        for i in range(len(amp)): 
            L.append(amp[i][0])
            R.append(amp[i][1])
        amp_L = round(max(L)*self.mouthVel_L, 1)
        amp_R = round(max(R)*self.mouthVel_R, 1)      

        print('Playing:', sample, 'L:', amp_L, 'R:', amp_R)
        # Left audio channel (Tortsua)
        if(amp_L > self.pause):
            # Move kaula
            self.moveKaula()

            #Move mouth
            self.arduino.write('ml' + str(amp_L)) #deprecated? Use GPIO
            self.moveMouth()            

            # Move eyes
            self.arduino.write('ex' + str(amp_L))
            #self.arduino.write('ey' + str(amp_L/3))
                # Blink
            if(random() < .1):
                self.arduino.write('b')
                sleep(.3)

            # Move arm
            self.moveArm()
        
    def vekeActive(self, stream):
        amp = stream.read(128)[0] # increase blocksize for better accuracy
        R = []
        for i in range(len(amp)):         
            R.append(amp[i][1])
        amp_R = round(max(R)*self.mouthVel_R, 1)      

        return (amp_R)

    def resetMotors(self):
        self.arduino.write('ml' + str(0))
        self.arduino.write('')
        self.resetKaula()
        self.resetMouth()
        self.resetEyes()
        self.resetArm()

    def resetEyes(self):
        self.arduino.write('ex500')
        self.arduino.write('ey500')
        self.arduino.write('')

    def resetKaula(self):
        GPIO.output(7, GPIO.LOW)

    def moveKaula(self):
        GPIO.output(7, GPIO.HIGH)

    def resetArm(self):
        GPIO.output(11, GPIO.LOW)

    def moveArm(self):
        GPIO.output(11, GPIO.HIGH)

    def resetMouth(self):
        GPIO.output(12, GPIO.LOW)

    def moveMouth(self):
        GPIO.output(12, GPIO.HIGH)
        
