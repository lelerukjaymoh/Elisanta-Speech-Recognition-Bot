import speech_recognition as sr
import text2speech

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something')
    audio = r.listen(source)
    print('Done')

try:
    text = r.recognize_google(audio)
    print('Elisanta thinks you said: \n' + text)
    lang = 'en'

    text2speech.tts(text, lang)

except Exception as e:
    print(e)
