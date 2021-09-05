from wlanIF import Wlan
from arduinoIF import Arduino


# Init Wlan
wlan = Wlan()

# Init Arduino
arduino = Arduino()
arduino.connect()



def speak(amp):
    print(amp)

def resetMotors():
    arduino.write('kv' + str(90))
    arduino.write('ko' + str(90))
    arduino.write('mm' + str(0))
    arduino.write('ex' + str(500))
    arduino.write('')


# Main loop
while(True):    
    wlan.broadcast('snoozing')
    wlan.listen()
    if(wlan.veke):
        print('Nyt meikä!')
        speak(wlan.veke)
    resetMotors()
    

