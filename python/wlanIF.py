from socket import *

class Wlan:
    def listen(self):
        ear = socket(AF_INET, SOCK_DGRAM)    
        ear.bind(('', 12345))
        ear.settimeout(3)
        try:
            hear = ear.recvfrom(1024)
            while hear[0].decode().startswith('playing:') or hear[0].decode().startswith('veke'):
                print('Hear?', hear)
                hear = ear.recvfrom(1024)
                return hear

        except:
            print('I hear nothing')   
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
