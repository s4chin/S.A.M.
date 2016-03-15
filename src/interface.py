import os.path, sys
import json
from ConfigParser import SafeConfigParser
from src import brightness
from src import browser_open
from src import open_app
from src import tts
from src import volume
from src import wifi
from src import wolfram

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

import time

parser = SafeConfigParser()
parser.read('../config.ini')

CLIENT_ACCESS_TOKEN = parser.get('api-ai', 'token')
SUBSCRIPTION_KEY = parser.get('api-ai', 'key')

def interface(query):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)

    request = ai.text_request()

    request.lang = 'en' # optional, default value equal 'en'

    request.query = query

    response = request.getresponse()
    data = json.load(response)
    task = data['result']

    if task["action"] == 'device.increase':
        if task["parameters"]["module"] == "volume":
            volume.volume_up(task["parameters"]["number"])
        elif task["parameters"]["module"] == "brightness":
            brightness.brightness_up(task["parameters"]["number"])
    elif task["action"] == "device.decrease":
        if task["parameters"]["module"] == "volume":
            volume.volume_down(task["parameters"]["number"])
        elif task["parameters"]["module"] == "brightness":
            brightness.brightness_down(task["parameters"]["number"])
    elif task["action"] == "device.switch_on":
        if task["parameters"]["module"] == "wifi":
            wifi.wifi_on()
    elif task["action"] == "switch_off":
        if task["parameters"]["module"] == "wifi":
            wifi.wifi_off()
    elif task["action"] == "browse.open":
        browser_open.open_site(task["parameters"]["website"])
    elif task["action"] == "web.search":
        browser_open.web_search((task["parameters"]["service_name"]).lower(), task["parameters"]["q"])
    elif task["action"] == "media.video_search":
        browser_open.web_search((task["parameters"]["service_name"]).lower(), task["parameters"]["q"])
    elif task['metadata']['speech'] != "":
        tts.say(task['metadata']['speech'])
    else:
        wolfram.wolfram(query)

if __name__ == '__main__':
    interface()
