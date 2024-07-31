from wlanIF import Wlan
import os

wlan = Wlan()
dir = 'C:/robokerho/samples/ile/transcripts/'
texts = os.listdir(dir)
print(texts)

while True:
    hear = wlan.listen()
    if hear:
        data = hear[0].decode().split(':')
        #print(data)
        searchString = data[1].replace('wav', 'txt')
        print(searchString)
        if searchString in texts:
            #print('Löytyy!')
            file = open(dir+searchString, 'r')
            raw_lines = file.readlines()
            #print(raw_lines)
            times = []
            lines = []
            for line in raw_lines:
                times.append(line.split(':')[0])
                lines.append(line.split(':')[1])
            #print(times)
            #print(lines)
            while lines:
                hear = wlan.listen()
                if hear:
                    #print(hear[0].decode())
                    time = hear[0].decode().split(':')[2]
                    #print(time)
                    if time >= times[0] and time < times[1]:
                        print(lines.pop(0))
                        times.pop(0)
