import configparser
import subprocess
import sys

# Read config
parser = configparser.ConfigParser()
parser.read('../config')

flush = sys.stdout.flush

print("Running configuration for", parser.get('env', 'name'))
flush()

# Audio configuration
try:
    if(parser.get('env', 'bt')):
        # Pair bluetooth device
        paired = subprocess.Popen(['bluetoothctl', 'paired-devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.read()
        print("Bluetooth found paired", paired)
        flush()
        connectReturn = 1
        i = 3
        while(connectReturn and i > 0):
            print("Bluetooth connecting to paired", paired)
            print("Retries left:", i)
            flush()
            connect = subprocess.run(['bluetoothctl', 'connect', parser.get('env', 'bt')])
            connectReturn = connect.returncode
            i = i-1
            if i == 0:
                print("Giving up...")
                flush()
                break
                
        print("Bluetooth connection successful!")
        print("================================")
        flush()

        # Select audio sink
        sinkReturn = "not"
        x = 0
        while ("not" in sinkReturn) and (x < 5):
            print("Selecting audio sink")
            flush()
            for i in range(10, 1, -1):
                sinkReturn = subprocess.run(['pacmd', 'set-default-sink', str(i)], capture_output=True).stdout.decode()
                print(sinkReturn)

                if not "not" in sinkReturn:
                    print("Sink", i, "selected successfully!")
                    print("=============================")
                    flush()
                    break

                if (i < 2):
                    print("Don't want no Analog or HDMI.")
                    print("Starting over...")
                    flush()
                    i = 10
            x = x+1
        print("DONE")
except:
    print("No audio configuration")
