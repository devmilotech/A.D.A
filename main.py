import speech_recognition as sr
import pyttsx3
from music import Play, Stop
import tkinter as tk

recognizer = sr.Recognizer()
engine = pyttsx3.init()

wakewords = ["ada", "aiden", "either", "eden"]

def listen():
    with sr.Microphone() as source:
        recognizer.energy_threshold = 200
        recognizer.dynamic_energy_threshold = False

        print("Listening...")

        try:
            audio = recognizer.listen(
                source,
                timeout=None,
                phrase_time_limit=5
            )

            return recognizer.recognize_google(audio).lower().strip()

        except sr.UnknownValueError:
            return ""
        except sr.RequestError as error:
            print(error)
            return ""

def say(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

def desktop():
    app = tk.Tk()
    app.attributes('-fullscreen', True)
    app.mainloop()

while True:
    text = listen()
    print("You:", text)

    words = text.split()

    if words and words[0].strip(".,!?;:") in wakewords:

        command = text.split(maxsplit=1)
        command = command[1] if len(command) > 1 else ""

        if not command:
            say("At your service sir")
            command = listen()

        if "hello" in command:
            say("Hello!")

        elif "drop my needle" in command:
            Play()

        elif "mute" in command:
            Stop()

        elif "open" in command and "desktop" in command:
            say("Opening the desk view sir")
            desktop()
