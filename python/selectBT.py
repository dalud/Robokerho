import configparser
import subprocess

# Read config
parser = configparser.ConfigParser()
parser.read("../config")
print("Running configuration for", parser.get("env", "name"))

# Pair bluetooth device
paired = subprocess.run(["bluetoothctl", "paired-devices"], capture_output=True).stdout
print("Bluetooth found paired", paired.decode())
connectReturn = 1
while(connectReturn):
    print("Bluetooth connecting to paired", paired.decode())
    connect = subprocess.run(["bluetoothctl", "connect", parser.get("env", "bt")])
    #print(connect)
    connectReturn = connect.returncode
print("Bluetooth connection successful!")
print("================================")
# Select audio sink
sinkReturn ="not"
while "not" in sinkReturn:
    print("Selecting audio sink")
    for i in range(10, 0, -1):
        print
        sinkReturn = subprocess.run(["pacmd", "set-default-sink", str(i)], capture_output=True).stdout.decode()
        print(sinkReturn)
        if not "not" in sinkReturn:
            print("Sink", i, "selected successfully!")
            print("===========================")
            break

