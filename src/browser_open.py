# https://docs.python.org/2/library/webbrowser.html
# input as: python browser_open.py youtube
from sys import argv
import webbrowser
sitename = argv[1]
webbrowser.open("http://" + sitename + ".com")
