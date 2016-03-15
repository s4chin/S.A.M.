import wolframalpha
import tts
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('../config.ini')

client = wolframalpha.Client(parser.get('wolframalpha', 'key'))

def wolfram(query):
    res = client.query(query)
    try:
        tts.say(res.pods[0].text)
    except:
        try:
            tts.say(res.pods[1].text)
        except:
            tts.say("Sorry, I don't get it.")
