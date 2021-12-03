import RPi.GPIO as GPIO

# Vedä GPIOt alas
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.output(29, GPIO.LOW)
GPIO.setup(31, GPIO.OUT)
GPIO.output(31, GPIO.LOW)
GPIO.setup(32, GPIO.OUT)
GPIO.output(32, GPIO.LOW)
GPIO.setup(33, GPIO.OUT)
GPIO.output(33, GPIO.LOW)
GPIO.setup(35, GPIO.OUT)
GPIO.output(35, GPIO.LOW)
GPIO.setup(36, GPIO.OUT)
GPIO.output(36, GPIO.LOW)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, GPIO.LOW)
GPIO.setup(38, GPIO.OUT)
GPIO.output(38, GPIO.LOW)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)


# Select bluetooth device
exec(open('selectBT.py', 'r').read())
