#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wlanIF import Wlan
import os
from time import sleep
import sys
import signal
from tkinter import *
from subprocess import Popen, PIPE
import signal

wlan = Wlan()
dir = '/home/pi/robokerho/samples/transcripts/'
texts = os.listdir(dir)
print(texts)
root = Tk()
root.configure(bg="black", cursor="none")
root.attributes('-fullscreen', True)
# TODO: set correct size and pads. 4 lines is enough?
text = Text(
    root,
    bg="black",
    fg="white",
    border=-10,
    padx=(root.winfo_screenwidth()/10),
    font=("Piboto", int(root.winfo_screenwidth()/31)),
    wrap=WORD,
    cursor="none"
)
text.tag_configure("center", justify='center')
text.tag_add("center", "1.0", "end")
text.pack(
    expand=True,
    fill='both',
    pady=(root.winfo_screenheight()/3, root.winfo_screenheight()/4-10),
)
root.update_idletasks()

# TODO: resolve interrupt for Tk.root()

def update():
    text.update_idletasks()
    text.see("1.0")

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
        file = open(dir+searchString, 'r', encoding='utf-8')
        lines = file.readlines()
        while lines:
            hear = wlan.listen()
            if hear: 
                time = int(hear[0].decode().split(':')[2])
                comp = int(lines[0].split(':')[0])
                
                if time >= comp-0: # set reduction value to match wlan print lag
                    text.delete("1.0", END)
                    update()
                    text.insert("1.0", lines.pop(0).split(':')[1], "center")
                    update()
                if lines[0].split(':')[1] == '':
                    sleep(6)
                    text.delete("1.0", END)
                    update()
                    break
        previous = searchString
