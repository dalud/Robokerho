import RPi.GPIO as GPIO

# Vedä GPIOt alas
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

# Select bluetooth device
exec(open('selectBT.py', 'r').read())
