import os

#https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Using_the_NetworkManager_Command_Line_Tool_nmcli.html

def wifi_on():
    os.system("nmcli radio wifi on")

def wifi_off():
    os.system("nmcli radio wifi off")
