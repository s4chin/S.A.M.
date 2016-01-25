import os

#http://askubuntu.com/questions/240857/what-commands-will-change-my-screens-brightness

def brightness_inc(b = 10):
    os.system("xbacklight +" + str(b) +"%")

def brightness_dec(b = 10):
    os.system("xbacklight +" + str(b) +"%")
