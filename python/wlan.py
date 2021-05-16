from socket import *

# Listen
with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind(('', 12345))

    while True:
        data = s.recvfrom(1024)
        print('I hear:' + data[0].decode())

# Speak
s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    try:        
        s.sendto(b'this is testing',('255.255.255.255',12345))
    except:
        print('No one listening')


