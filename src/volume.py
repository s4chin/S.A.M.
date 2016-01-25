import os

#http://stackoverflow.com/a/21868267
def volume_up(value = 5):
    os.system("amixer -D pulse sset Master "+str(value)+"%+ -q")

def volume_down(value = 5):
    os.system("amixer -D pulse sset Master "+str(value)+"%- -q")
