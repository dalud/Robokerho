from socket import *
import signal
import sys
#import configparser

# Read config
#conf = configparser.ConfigParser()
#conf.read('/home/pi/robokerho/config')

def signal_term_handler(signal, frame):
    print("SIGTERM from wlan")
    sys.exit()

signal.signal(signal.SIGTERM, signal_term_handler)

# Select robo
#robo = conf.get('env', 'robo')

class Wlan:
    def listen(self):
        ear = socket(AF_INET, SOCK_DGRAM)    
        ear.bind(('', 12345))
        ear.settimeout(1)
        
        try:
            hear = ear.recvfrom(1024)
            #print('Hear:', hear)

            while ("playing" in hear[0].decode()) or ("veke" in hear[0].decode()) or ("jussi" in hear[0].decode()) or ("TV" in hear[0].decode()) or ("VIDEO" in hear[0].decode()):
                return hear
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            sys.exit()
        except:
            #print('I hear nothing')
            #return 0
            return
        ear.close()

    # TODO: error prone if network not available
    def broadcast(self, msg):
        mouth = socket(AF_INET, SOCK_DGRAM)    
        mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        mouth.setblocking(False)
        try:
            mouth.sendto(bytes(msg, encoding='utf-8'),('255.255.255.255',12345))
        except:
            pass
        mouth.close()

    def stop(self):
        kill = socket(AF_INET, SOCK_DGRAM)
        kill.close()
