import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    tme = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The Current Time is"+tme)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The Current Date is"+day+month+year)
  


def wish():
    speak("Welcome Back sir ")
    time()
    date()

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Sir")
    if hour >= 18 and hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
    try:
        print("Recognizing")
        a = "You said " + r.recognize_google(audio)
        print(a)




    except Exception as e:
        print(e)
        speak("Say again")

        return "None"
    return a


if __name__ == "__main__":
    wish()
    while True:
        command = take_command().lower()
        print(command)
        if "date" in command:
            date()
        elif "time" in command:
            time()
        elif "offline" in command:
            speak("Bye Sir")
            quit()
        elif "wikipedia" in command:
            speak("Searching")
            command = command.replace("wikipedia", "")
            wiki_result = wikipedia.summary(command, sentences=2)
            speak(wiki_result)
