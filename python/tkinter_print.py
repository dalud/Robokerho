#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from tkinter import *
from subprocess import Popen, PIPE
import signal

# Utils
root = Tk()
root.configure(bg="black", cursor="none")
root.attributes('-fullscreen', True)
text = Text(
    root,
    bg="black",
    fg="white",
    border=-10,
    padx=(root.winfo_screenwidth()/10),
    font=("Piboto", int(root.winfo_screenwidth()/31)),
    #font=("Piboto", int(root.winfo_screenwidth()/31)),
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
def signal_term_handler(signal, frame):
    print('Keyboard interrupt')
    process.kill()
    Popen(['killall', 'python'])
    #Popen(['sudo', 'kill', '-9', str(os.getpid())])
    sys.exit()    

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)

process = Popen(['sudo', 'python', '/home/pi/robokerho/python/subtitler.py'], stdout=PIPE, stderr=PIPE)

def update():
    text.update_idletasks()
    text.see("1.0")

while True:
        if process.stdout:
            for line in process.stdout:
                if str(line).find("#CLR#") > 0:
                    text.delete("1.0", END)
                    update()
                else:
                    text.insert("1.0", line, "center")
                    update()
        if process.stderr:
            for line in process.stderr:
                print(line)
                text.insert("1.0", line, "center")
                update()
