#!/usr/bin/env python

import sys
import os
from tkinter import *
from subprocess import Popen, PIPE
import signal

# Utils
root = Tk()
root.attributes('-fullscreen', True)
text = Text(
    root,
    bg="black",
    fg="white",
    padx=(root.winfo_screenwidth()/5),
    pady=(root.winfo_screenheight()/3),
    border=-10,
    font=("Arial", 33),
    wrap=WORD
)
text.tag_configure("center", justify='center')
text.tag_add("center", "1.0", "end")
text.pack(expand=True, fill='both')
root.update_idletasks()

def signal_term_handler(signal, frame):
    print('Keyboard interrupt')
    process.kill()
    Popen(['killall', 'python'])
    #Popen(['sudo', 'kill', '-9', str(os.getpid())])
    sys.exit()    

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

process = Popen(['sudo', 'python', '/home/pi/robokerho/python/subtitler.py'], stdout=PIPE, stderr=PIPE)

while True:
        if process.stdout:
            for line in process.stdout:
                if str(line).find("#CLR#") > 0:
                    text.delete("1.0", END)
                else:
                    text.insert("1.0", line, "center")
                    text.see("1.0")
                    text.update_idletasks()
        if process.stderr:
            for line in process.stderr:
                print(line)
                text.insert("1.0", line, "center")
                text.see("1.0")
                text.update_idletasks()
