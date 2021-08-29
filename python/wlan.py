from socket import *

# Listen
def listen():
    print('I am listening')
    ear = socket(AF_INET, SOCK_DGRAM)
    ear.bind(('', 12345))
    data = ear.recvfrom(1024)    
    print('I hear:', data)

# Speak
def speak():
    print('I am speaking')
    mouth = socket(AF_INET, SOCK_DGRAM)
    mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    mouth.sendto(b'this is ...',('255.255.255.255',12345))

while True:
    speak()
    listen()


