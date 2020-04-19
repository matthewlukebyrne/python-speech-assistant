import speech_recognition as sr 
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime



# Initialize (Used to recognize speech)
r = sr.Recognizer()

# Functionality to capture the voice data
# Then the creation of the function indented called "record_audio"
def record_audio(ask = False):

    # Browser Search
    if ask:
        alexa_speak(ask)

    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        # Wrapped in a try (essectially a if statement) for noise exception
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak("Sorry I did not get that!")
        except sr.RequestError:
            alexa_speak("Sorry this service is down...")
        return voice_data


# Define a function for vouce control
def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)

    # Print what she says as well as voice
    print(audio_string)
    os.remove(audio_file)

# A question and a response
def respond(voice_data):
    if 'name' in voice_data:
        alexa_speak('I am a cheap ass version of Alexa')
    if 'time' in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to browse for?')
        # A query with the letter "q" concatenating on
        url = 'https://google.com/search?q=' + search
        # Then the browser fetches the function and swings it over to the page
        webbrowser.get().open(url)
        alexa_speak("I found this page for " + search)

    # Google Map find
    if 'location' in voice_data:
        location = record_audio('What is location?')
        # A query with the location concatenating on with ampersamp
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        # Then the browser fetches the function and swings it over to the page
        webbrowser.get().open(url)
        alexa_speak("Here is the location of " + location + ' it does not look cool to be honest!')
    # Exit on command
    if 'exit' in voice_data:
        alexa_speak("bye human")
        exit()

time.sleep(1)
alexa_speak("Hello my darling master!")
# A while loop to wait to talk
while 1:
    # This variable now stores the voice data
    voice_data = record_audio()             
    respond(voice_data)