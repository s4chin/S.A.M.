import pyttsx

def say(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()
