import subprocess

def say(text):
    return subprocess.call("espeak -s 155 -a 200 '"+text+"'", shell=True)
