import datetime
import speech_recognition as sr
import pyttsx3
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Guten Morgen!")
    
    elif hour>=12 and hour<18:
        speak("Guten Abend")

    else:
        speak("Gute Nacht")

    speak("i am jarvid sir. please tell me how can i help you")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,Language = 'en-in')
        print(f"user said:{query}",)

    except Exception as e:
        print("say that again please")
        return "None"
    return query 


if __name__ == "__main__":
    wishMe()
    takeCommand()
