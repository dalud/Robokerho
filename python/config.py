import configparser
from ileIF import Ile
from marinaIF import Marina


# Read config
conf = configparser.ConfigParser()
conf.read('/home/pi/robokerho/config')

# Select robo
robo = conf.get('env', 'robo')
if(robo == 'ile'):
    robo = Ile()    
elif(robo == 'marina'):
    robo = Marina()
else:
    print("No suitable robot class found. Exiting.")
    sys.exit(1)
    
# Reset motors
robo.resetMotors()

# Select bluetooth device
exec(open('/home/pi/robokerho/python/selectBT.py', 'r').read())
