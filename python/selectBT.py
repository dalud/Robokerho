import configparser
import subprocess
import sys

# Read config
parser = configparser.ConfigParser()
parser.read('../config')

print("Running configuration for " + parser.get('env', 'name'))

# Audio configuration
try:
    if(parser.get('env', 'bt')):
        # Pair bluetooth device
        paired = subprocess.run(['bluetoothctl', 'paired-devices'], capture_output=True).stdout
        print("Bluetooth found paired " + paired.decode())
        connectReturn = 1
        i = 3
        while(connectReturn and i > 0):
            print("Bluetooth connecting to paired " + paired.decode())
            print("Retries left: " + str(i))
            connect = subprocess.run(['bluetoothctl', 'connect', parser.get('env', 'bt')])
            connectReturn = connect.returncode
            i = i-1
            if i == 0:
                print("Giving up...")
                break
                
        print("Bluetooth connection successful!")
        print("================================")

        # Select audio sink
        sinkReturn = "not"
        x = 0
        while ("not" in sinkReturn) and (x < 10):
            print("Selecting audio sink")
            for i in range(10, 1, -1):
                sinkReturn = subprocess.run(['pacmd', 'set-default-sink', str(i)], capture_output=True).stdout.decode()
                print(sinkReturn)

                if not "not" in sinkReturn:
                    print("Sink " + str(i) + " selected successfully!")
                    print("=============================")
                    break

                if (i < 2):
                    print("Don't want no Analog or HDMI.")
                    print("Starting over...")
                    i = 10
            x = x+1
        print("DONE")
except:
    print("No audio configuration")
