import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import uuid
import webbrowser
def listen():
    '''obtain audio from the microphone'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("hey guy start talking")
       audio = r.listen(source,phrase_time_limit=5)
    data=''
    try:
        data=r.recognize_google(audio,language='en-US')
        print(" you said " + data)
    except sr.UnknownValueError:
        print("i could not understand audio")
    except sr.RequestError as e:
        print('microphone not working')
    return data
    '''tts =gTTs(data)
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')
listen()'''
def respond(String):
    '''function'''
    tts=gTTS(text=String)
    tts.save('Speech.mp3')
    filename='speech%s.mp3'%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def virtualassistant(data):
    '''game'''
    if 'how are you' in data:
        listening=True
        respond('fine this is vignesh number one four twenty from lower of regina')
    elif 'time' in data:
        listening=True
        respond(time.ctime())
    elif 'you thinking' in data:
        listening=True
        respond('weekend plan')
    elif 'open google' in data.lower():
        listening =True
        url = 'https://www.google.com/'
        webbrowser.open(url)
        respond('success')
    elif 'locate' in data:
        listening=True
        webbrowser.open('https://www.google.com/maps/search/'+
                        data.replace('locate',""))
        result='located'
        respond('Located {}'.format(data.replace(
            "locate","")))
    elif 'who are you' in data:
        listening=True
        respond('i am sunnyleone wife of vignesh')
    elif 'stop talking' in data:
        listening=False
        respond('okay take care')
    try:
        return listening
    except:
        print('stopped')
        

respond('hey guys this is vignesh number one four twenty lover of regina')
listening=True
while listening==True:
    data=listen()
    listening=virtualassistant(data)
    
