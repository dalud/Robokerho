from wlanIF import Wlan
import os

wlan = Wlan()
dir = 'C:/robokerho/samples/ile/transcripts/'
texts = os.listdir(dir)
print(texts)

def getSearchString():
    hear = wlan.listen()
    if hear:
        searchString = "not found"
        data = hear[0].decode().split(':')
        if 'veke' in data:
            searchString = data[3].replace('wav', 'txt')
        else:
            searchString = data[1].replace('wav', 'txt')
        print(searchString)
        return searchString

previous = ""

while True:
    searchString = getSearchString()
    if searchString in texts and searchString != previous:
        file = open(dir+searchString, 'r')
        lines = file.readlines()
        while lines:
            hear = wlan.listen()
            if hear:
                time = int(hear[0].decode().split(':')[2])
                comp = int(lines[0].split(':')[0])
                if time >= comp-0: # set reduction value to match wlan print lag
                    print("\n\n\n\n\n\n\n\n\n\n\n\n")
                    print(lines.pop(0).split(':')[1])
        previous = searchString
