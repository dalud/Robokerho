from random import random
from os import listdir
import os

files = os.listdir('/robokerho/python')
print(files)

alea = (int)(random()*len(files))

while(True):
    print(files[alea])
    alea = (int)(random()*len(files))

lotr = '/home/pi/kikkelis/kokkelis'
print(lotr.rsplit('/home/pi'))

# inheritance
class Robohemian:
    def __init__(self, name):
        self.name = name

    def sout(self):
        print('My name is ', self.name)
