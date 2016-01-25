import webbrowser

# https://docs.python.org/2/library/webbrowser.html

def open_site(sitename):
    webbrowser.open("http://" + sitename + ".com")
