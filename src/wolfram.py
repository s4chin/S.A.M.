import wolframalpha
import tts
client = wolframalpha.Client('XWPJXW-4GV3RL493T')

def wolfram(query):
    res = client.query(query)
    try:
        tts.say(res.pods[1].text)
    except:
        tts.say(res.pods[0].text)
