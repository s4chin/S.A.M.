import os.path, sys
import json
from src import brightness
from src import browser_open
from src import open_app
from src import tts
from src import volume
from src import wifi

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

import time

CLIENT_ACCESS_TOKEN = '2c15be66aea04971996b82207f616d94'
SUBSCRIPTION_KEY = '908cf30d-603b-4669-b06b-8114b7c9c2e2'

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
            volume.volume_up()
        elif task["parameters"]["module"] == "brightness":
            brightness.brightness_up()
    elif task["action"] == "device.decrease":
        if task["parameters"]["module"] == "volume":
            volume.volume_down()
        elif task["parameters"]["module"] == "brightness":
            brightness.brightness_down()
    elif task["action"] == "device.switch_on":
        if task["parameters"]["module"] == "wifi":
            wifi.wifi_on()
    elif task["action"] == "switch_off":
        if task["parameters"]["module"] == "wifi":
            wifi.wifi_off()
    elif task['metadata']['speech'] != "":
        # print task['metadata']['speech']
        tts.say(task['metadata']['speech'])
    else:
        tts.say("sorry...")

if __name__ == '__main__':
    interface()
