import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pywhatkit as kit
import pyautogui

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice to female
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)  # Adjust speaking rate as needed

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Zara, your voice assistant. How can I assist you today?")

def take_command():
    """Takes voice input from the user and converts it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand audio, please say that again.")
        return "None"
    return command.lower()

def tell_time():
    """Tells the current time"""
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    """Tells the current date"""
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

def open_website(site):
    """Opens a specified website"""
    webbrowser.open(site)
    speak(f"Opening {site}")

def search_google(query):
    """Searches for a query on Google"""
    kit.search(query)
    speak(f"Searching for {query} on Google")

def tell_about_person(person):
    """Provides information about a person from Wikipedia"""
    try:
        info = wikipedia.summary(person, sentences=2)
        speak(f"According to Wikipedia, {info}")
    except Exception as e:
        speak("Sorry, I couldn't find information on that person.")

def launch_application(app_path):
    """Launches an application"""
    try:
        subprocess.Popen(app_path)
        speak("Application launched successfully.")
    except Exception as e:
        speak("Sorry, I could not launch the application.")

def play_music(song):
    """Plays a song on YouTube"""
    speak(f"Playing {song} on YouTube")
    kit.playonyt(song)

def take_note():
    """Takes a note and saves it in a text file"""
    speak("What would you like me to note down?")
    note = take_command()
    with open("important_notes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {note}\n")
    speak("Note taken successfully.")

def take_screenshot(filename="screenshot"):
    """Takes a screenshot and saves it with a custom filename"""
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{filename}.png")
    speak(f"Screenshot saved as {filename}.png")

# Main function to handle commands
def main():
    greet_user()
    while True:
        command = take_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "launch" in command:
            speak("Please tell me the name of the application.")
            app_name = take_command()
            app_paths = {
                "notepad": "C:\\Windows\\notepad.exe",
                "calculator": "C:\\Windows\\System32\\calc.exe"
            }
            if app_name in app_paths:
                launch_application(app_paths[app_name])
            else:
                speak("Sorry, I don't know that application.")
        elif "open" in command:
            if "website" in command:
                speak("Which website would you like to open?")
                site = take_command().replace(" ", "")
                open_website(f"https://{site}.com")
        elif "search" in command:
            speak("What would you like to search for?")
            query = take_command()
            search_google(query)
        elif "tell me about" in command:
            person = command.replace("tell me about", "").strip()
            tell_about_person(person)
        elif "play music" in command:
            speak("What song would you like to hear?")
            song = take_command()
            play_music(song)
        elif "take note" in command:
            take_note()
        elif "screenshot" in command:
            speak("Please provide a naimport pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pywhatkit as kit
import pyautogui

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice to female
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)  # Adjust speaking rate as needed

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Zara, your voice assistant. How can I assist you today?")

def take_command():
    """Takes voice input from the user and converts it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand audio, please say that again.")
        return "None"
    return command.lower()

def tell_time():
    """Tells the current time"""
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    """Tells the current date"""
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

def open_website(site):
    """Opens a specified website"""
    webbrowser.open(site)
    speak(f"Opening {site}")

def search_google(query):
    """Searches for a query on Google"""
    kit.search(query)
    speak(f"Searching for {query} on Google")

def tell_about_person(person):
    """Provides information about a person from Wikipedia"""
    try:
        info = wikipedia.summary(person, sentences=2)
        speak(f"According to Wikipedia, {info}")
    except Exception as e:
        speak("Sorry, I couldn't find information on that person.")

def launch_application(app_path):
    """Launches an application"""
    try:
        subprocess.Popen(app_path)
        speak("Application launched successfully.")
    except Exception as e:
        speak("Sorry, I could not launch the application.")

def play_music(song):
    """Plays a song on YouTube"""
    speak(f"Playing {song} on YouTube")
    kit.playonyt(song)

def take_note():
    """Takes a note and saves it in a text file"""
    speak("What would you like me to note down?")
    note = take_command()
    with open("important_notes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {note}\n")
    speak("Note taken successfully.")

def take_screenshot(filename="screenshot"):
    """Takes a screenshot and saves it with a custom filename"""
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{filename}.png")
    speak(f"Screenshot saved as {filename}.png")

# Main function to handle commands
def main():
    greet_user()
    while True:
        command = take_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "launch" in command:
            speak("Please tell me the name of the application.")
            app_name = take_command()
            app_paths = {
                "notepad": "C:\\Windows\\notepad.exe",
                "calculator": "C:\\Windows\\System32\\calc.exe"
            }
            if app_name in app_paths:
                launch_application(app_paths[app_name])
            else:
                speak("Sorry, I don't know that application.")
        elif "open" in command:
            if "website" in command:
                speak("Which website would you like to open?")
                site = take_command().replace(" ", "")
                open_website(f"https://{site}.com")
        elif "search" in command:
            speak("What would you like to search for?")
            query = take_command()
            search_google(query)
        elif "tell me about" in command:
            person = command.replace("tell me about", "").strip()
            tell_about_person(person)
        elif "play music" in command:
            speak("What song would you like to hear?")
            song = take_command()
            play_music(song)
        elif "take note" in command:
            take_note()
        elif "screenshot" in command:
            speak("Please provide a name for the screenshot file.")
            filename = take_command()
            take_screenshot(filename)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()me for the screenshot fileimport pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pywhatkit as kit
import pyautogui

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice to female
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)  # Adjust speaking rate as needed

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Zara, your voice assistant. How can I assist you today?")

def take_command():
    """Takes voice input from the user and converts it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand audio, please say that again.")
        return "None"
    return command.lower()

def tell_time():
    """Tells the current time"""
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    """Tells the current date"""
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

def open_website(site):
    """Opens a specified website"""
    webbrowser.open(site)
    speak(f"Opening {site}")

def search_google(query):
    """Searches for a query on Google"""
    kit.search(query)
    speak(f"Searching for {query} on Google")

def tell_about_person(person):
    """Provides information about a person from Wikipedia"""
    try:
        info = wikipedia.summary(person, sentences=2)
        speak(f"According to Wikipedia, {info}")
    except Exception as e:
        speak("Sorry, I couldn't find information on that person.")

def launch_application(app_path):
    """Launches an application"""
    try:
        subprocess.Popen(app_path)
        speak("Application launched successfully.")
    except Exception as e:
        speak("Sorry, I could not launch the application.")

def play_music(song):
    """Plays a song on YouTube"""
    speak(f"Playing {song} on YouTube")
    kit.playonyt(song)

def take_note():
    """Takes a note and saves it in a text file"""
    speak("What would you like me to note down?")
    note = take_command()
    with open("important_notes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {note}\n")
    speak("Note taken successfully.")

def take_screenshot(filename="screenshot"):
    """Takes a screenshot and saves it with a custom filename"""
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{filename}.png")
    speak(f"Screenshot saved as {filename}.png")

# Main function to handle commands
def main():
    greet_user()
    while True:
        command = take_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "launch" in command:
            speak("Please tell me the name of the application.")
            app_name = take_command()
            app_paths = {
                "notepad": "C:\\Windows\\notepad.exe",
                "calculator": "C:\\Windows\\System32\\calc.exe"
            }
            if app_name in app_paths:
                launch_application(app_paths[app_name])
            else:
                speak("Sorry, I don't know that application.")
        elif "open" in command:
            if "website" in command:
                speak("Which website would you like to open?")
                site = take_command().replace(" ", "")
                open_website(f"https://{site}.com")
        elif "search" in command:
            speak("What would you like to search for?")
            query = take_command()
            search_google(query)
        elif "tell me about" in command:
            person = command.replace("tell me about", "").strip()
            tell_about_person(person)
        elif "play music" in command:
            speak("What song would you like to hear?")
            song = take_command()
            play_music(song)
        elif "take note" in command:
            take_note()
        elif "screenshot" in command:
            speak("Please provide a naimport pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pywhatkit as kit
import pyautogui

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice to female
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 150)  # Adjust speaking rate as needed

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the time of day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Zara, your voice assistant. How can I assist you today?")

def take_command():
    """Takes voice input from the user and converts it to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Could not understand audio, please say that again.")
        return "None"
    return command.lower()

def tell_time():
    """Tells the current time"""
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    """Tells the current date"""
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {date}")

def open_website(site):
    """Opens a specified website"""
    webbrowser.open(site)
    speak(f"Opening {site}")

def search_google(query):
    """Searches for a query on Google"""
    kit.search(query)
    speak(f"Searching for {query} on Google")

def tell_about_person(person):
    """Provides information about a person from Wikipedia"""
    try:
        info = wikipedia.summary(person, sentences=2)
        speak(f"According to Wikipedia, {info}")
    except Exception as e:
        speak("Sorry, I couldn't find information on that person.")

def launch_application(app_path):
    """Launches an application"""
    try:
        subprocess.Popen(app_path)
        speak("Application launched successfully.")
    except Exception as e:
        speak("Sorry, I could not launch the application.")

def play_music(song):
    """Plays a song on YouTube"""
    speak(f"Playing {song} on YouTube")
    kit.playonyt(song)

def take_note():
    """Takes a note and saves it in a text file"""
    speak("What would you like me to note down?")
    note = take_command()
    with open("important_notes.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {note}\n")
    speak("Note taken successfully.")

def take_screenshot(filename="screenshot"):
    """Takes a screenshot and saves it with a custom filename"""
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{filename}.png")
    speak(f"Screenshot saved as {filename}.png")

# Main function to handle commands
def main():
    greet_user()
    while True:
        command = take_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "launch" in command:
            speak("Please tell me the name of the application.")
            app_name = take_command()
            app_paths = {
                "notepad": "C:\\Windows\\notepad.exe",
                "calculator": "C:\\Windows\\System32\\calc.exe"
            }
            if app_name in app_paths:
                launch_application(app_paths[app_name])
            else:
                speak("Sorry, I don't know that application.")
        elif "open" in command:
            if "website" in command:
                speak("Which website would you like to open?")
                site = take_command().replace(" ", "")
                open_website(f"https://{site}.com")
        elif "search" in command:
            speak("What would you like to search for?")
            query = take_command()
            search_google(query)
        elif "tell me about" in command:
            person = command.replace("tell me about", "").strip()
            tell_about_person(person)
        elif "play music" in command:
            speak("What song would you like to hear?")
            song = take_command()
            play_music(song)
        elif "take note" in command:
            take_note()
        elif "screenshot" in command:
            speak("Please provide a name for the screenshot file.")
            filename = take_command()
            take_screenshot(filename)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()me for the screenshot file.")
            filename = take_command()
            take_screenshot(filename)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main().")
            filename = take_command()
            take_screenshot(filename)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
