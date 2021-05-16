from socket import *

# Listen
with socket(AF_INET, SOCK_DGRAM) as s:
    s.bind(('', 12345))

    while True:
        data = s.recvfrom(1024)
        print('I hear:' + data[0].decode())
