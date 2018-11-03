from gtts import gTTS
import pyglet
import time
import os

def tts(text,lang):
    file = gTTS(text=text, lang=lang)
    filename = '/tmp/temp.wav'
    file.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)