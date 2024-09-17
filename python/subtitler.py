from wlanIF import Wlan
import os
from time import sleep
import sys
import signal

wlan = Wlan()
flush = sys.stdout.flush
dir = '/home/pi/robokerho/samples/transcripts/'
texts = os.listdir(dir)
br = 10 # How many line breaks to clr. Set according to font size. Obsolete if padx, pady aet?
print(texts)
flush()

def signal_term_handler(signal, frame):
    print("SIGTERM from wlan")
    wlan.stop()
    sys.exit()

signal.signal(signal.SIGTERM, signal_term_handler)

def getSearchString():
    hear = wlan.listen()
    flush()
    if hear:
        searchString = "not found"
        data = hear[0].decode().split(':')
        if 'veke' in data:
            searchString = data[3].replace('wav', 'txt')
        else:
            searchString = data[1].replace('wav', 'txt')
        print(searchString)
        flush()
        return searchString

previous = ""

while True:
    searchString = getSearchString()
    if searchString in texts and searchString != previous:
        file = open(dir+searchString, 'r', encoding='utf-8')
        lines = file.readlines()
        while lines:
            hear = wlan.listen()
            if hear: 
                time = int(hear[0].decode().split(':')[2])
                comp = int(lines[0].split(':')[0])
                #print(time)
                if time >= comp-0: # set reduction value to match wlan print lag
                    #print("\n"*br)
                    print("#CLR#")
                    print(lines.pop(0).split(':')[1])
                    flush()
            if lines[0].split(':')[1] == '':
                sleep(6)
                #print("\n"*br)
                print("#CLR#")
                flush()
                break 
        previous = searchString
