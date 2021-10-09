from socket import *

class Wlan:
    def __init__(self):
        self.veke = 0

    def listen(self):
        print('I am listening')        
        ear = socket(AF_INET, SOCK_DGRAM)    
        ear.bind(('', 12345))
        ear.settimeout(10)
        try:
            hear = ear.recvfrom(1024)
            print('Hear?', hear)
            while hear[0].decode().startswith('playing:'):
                print('Hear?', hear)         
                hear = ear.recvfrom(1024)
            if hear[0].decode().startswith('veke:'):
                self.veke = hear[0].decode().split(':')[1]
                print(self.veke)
                return self.veke
        except:
            print('I hear nothing')   
        ear.close()
        self.veke = False

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

    def veke(self):
        return self.veke
