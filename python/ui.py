import PySimpleGUI as ui
import configparser
import subprocess
import sys
import os
from threading import Thread
from queue import Queue, Empty

# Utils
#stdout = ""
process = None
ON_POSIX = 'posix' in sys.builtin_module_names
q = Queue()

def enqueue_output(out, queue):
    for line in iter(out.readline, '\n'):
        queue.put(line)
    out.close()
    
# Read config file
parser = configparser.ConfigParser()
parser.read('../config')

# Build UI
layout = [[ui.Text("Robohemian: "+parser.get('env', 'name'), font="arial 16 bold")],
          [ui.Button("CONFIG"), ui.Button("RUN"), ui.Button("STOP"), ui.Button("X")],
          [ui.Multiline(reroute_stdout=True, reroute_stderr=True, auto_refresh=True, autoscroll=True, expand_x=True, expand_y=True, no_scrollbar=True)]]
window = ui.Window("Robohemian: "+parser.get('env', 'name'), layout, size=(420, 320), default_button_element_size=(10, 5), auto_size_buttons=False, resizable=True)

# Main loop
while True:
    event, values = window.read(10)
    window.maximize()
    #print(event, process)

    if event == "CONFIG":
        #process = subprocess.Popen(['python3', 'config.py'], stdout=subprocess.PIPE, text=True, bufsize=1)
        #process = ui.execute_command_subprocess('robo', 'python3', 'config.py')
        #process = os.system('python3 config.py')
        process = subprocess.Popen(['python3', 'config.py'], stdout=subprocess.PIPE, text=True, bufsize=1, close_fds=ON_POSIX)
        t = Thread(target=enqueue_output, args=(process.stdout, q))
        t.daemon = True
        t.start()
        #print(process)

    if event == "RUN":
        exec(open('robohemian.py', 'r').read())

    if event == "STOP":
        process.stdout.close()
        process.terminate()

    if event == "X" or event == ui.WIN_CLOSED:
        break

    try: line = q.get_nowait()
    except Empty:
        continue
    else: print(line)
        
    #if(process):
        #print(process)
        #for line in iter(process.stdout.readline, ''):
            #print(line)
        #process.stdout.close()
        #process.terminate()
        #process = None

window.close()
