import re, time

import speech_recognition as sr
from src.tts import say
from src import interface

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def gstt():
    r = sr.Recognizer()
    m = sr.Microphone()
    isAwake = False
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                if isAwake: # If SAM is supposed to respond
                    if findWholeWord('see you later')(value):
                        # If user says Bye bye Sam to close down sam
                        say("Bye sir.")
                        isAwake = False
                    else: # If user says something else
                        interface.interface(value)
                elif findWholeWord('wake up')(value):
                    # If SAM isn't awake, then wake him up
                    say('Hello, sir.')
                    isAwake = True
                else:
                    # If SAM isn't awake, nor does the user want to wake him up
                    # SAM doesn't do anything
                    pass
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
