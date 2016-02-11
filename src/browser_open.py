import webbrowser

# https://docs.python.org/2/library/webbrowser.html
# http://askubuntu.com/a/618490

def open_site(sitename):
    webbrowser.open("http://" + sitename + ".com")

def web_search(sitename, query):
    if sitename == "wikipedia":
        webbrowser.open("https://en.wikipedia.org/wiki/Special:Search/{}".format(query))
    else:
        webbrowser.open("https://" + sitename + ".com/search?q={}".format(query))
