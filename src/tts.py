import os

def say(text):
    return os.system("espeak  -s 155 -a 200 '"+text+"'")
