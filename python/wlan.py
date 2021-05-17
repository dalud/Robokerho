from socket import *

# Listen
def listen():
    ear = socket(AF_INET, SOCK_DGRAM)
    ear.bind(('', 12345))    
    data = ear.recvfrom(1024)
    print('I hear:', data)

# Speak
def speak():
    mouth = socket(AF_INET, SOCK_DGRAM)
    mouth.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    mouth.sendto(b'this is Ile',('255.255.255.255',12345))

while True:
    speak()
    listen()


