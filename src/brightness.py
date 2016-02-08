import os

#http://askubuntu.com/questions/240857/what-commands-will-change-my-screens-brightness

def brightness_up(b = 10):
    os.system("xbacklight +" + str(b) +"%")

def brightness_down(b = 10):
    os.system("xbacklight -" + str(b) +"%")
