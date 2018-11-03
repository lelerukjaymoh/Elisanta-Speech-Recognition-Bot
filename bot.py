import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambiet_noise(source)
        print('Listeninig')
        audio = r.listen(source)

    try:
        message = r.recognize_google((audio))
        print(message)

        if 'hello' in message:
            speech = ('Hello master, How can i assist you')
            tts = gTTS(text=speech, lang='en')
            tts.save('C:\\Users\\Jaymoh\\Music\\elisanta.mp3')
            mixer.music.load('C:\\Users\\Jaymoh\\Music\\elisanta.mp3')
            mixer.music.play()

        if 'who are you' in message:
            speech = ('My name is Elisanta. I am a speech bot created by Jaymoh. How could i help?')
            tts = gTTS(text=speech, lang='eng')
            tts.save('C:\\Users\\Jaymoh\\Music\\elisanta.mp3')
            mixer.music.load('C:\\Users\\Jaymoh\\Music\\elisanta.mp3')
            mixer.music.play()

        if 'can u speak swahili':
            speech = ('Yes i can. Habari yako. Although my developer is currently working on my accent')
            tts = gTTS(text=speech, lang='eng')
            tts.save('C:\\Users\\Jaymoh\\Music\\elisanta.mp3')
            mixer.music.load('C:\\Users\\Jaymoh\\Music\\elisanta.mp3')
            mixer.music.play()

    except Exception as e:
        print(e)
