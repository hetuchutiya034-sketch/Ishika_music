from gtts import gTTS
import os

def tts(text, filename):
    tts = gTTS(text, lang='hi')
    file = f"{filename}.mp3"
    tts.save(file)
    return file
