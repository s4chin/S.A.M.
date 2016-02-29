import webbrowser

# https://docs.python.org/2/library/webbrowser.html
# http://askubuntu.com/a/618490

def open_site(sitename):
    url = "http://" + sitename + ".com"
    webbrowser.open(url)

def web_search(sitename, query):
    if sitename == "wikipedia":
        webbrowser.open("https://en.wikipedia.org/wiki/Special:Search/{}".format(query))
    elif sitename == "youtube":
        webbrowser.open("https://www.youtube.com/results?search_query={}".format(query))
    else:
        webbrowser.open("https://" + sitename + ".com/search?q={}".format(query))
