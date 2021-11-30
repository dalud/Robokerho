import sys

def print(arg):
    sys.stdout.write(arg + '\n')
    sys.stdout.flush()
    
while True:
    print("still running...")
