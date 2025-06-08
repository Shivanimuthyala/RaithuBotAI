# 📁 AgriBot_AI_Chatbot/voice/speech_utils.py
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

LANG_MAP = {"en": "en", "te": "te"}


def recognize_speech():
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("🗣️ Recognized:", text)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand."


def speak(text, lang="en"):
    if lang == "te":
        text = translator.translate(text, src='en', dest='te').text
    engine.say(text)
    engine.runAndWait()

